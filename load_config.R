##
## R script to chain-load hierarchical lesson configuration YAML files.
## Top-level configuration is typically "../config.yaml".
##

library(yaml)
library(knitr)

# -------------------------------------------------------------------
# Define placeholder config and snippets() early so it always exists
# -------------------------------------------------------------------
config <- NULL
snippets <- function(child_file) {
  stop("snippets() called before configuration was loaded.")
}

# -------------------------------------------------------------------
# Utility: Get the snippet directory next to a config file
# -------------------------------------------------------------------

get_snippet_subdir <- function(file, must_exist = TRUE) {
  full_file <- normalizePath(file)
  dir <- file.path(dirname(full_file), "snippets")
  
  if (must_exist && !dir.exists(dir)) {
    stop("Snippet directory does not exist: ", dir)
  }
  
  return(dir)
}

# -------------------------------------------------------------------
# Load lesson configuration
# -------------------------------------------------------------------
find_config <- function(paths, root) {
  for (p in paths) {
    candidate <- file.path(root, p)
    if (file.exists(candidate)) return(normalizePath(candidate))
  }
  stop("Could not find lesson configuration in any known location.")
}

get_rmd_dir <- function() {
  input <- tryCatch(knitr::current_input(), error = function(e) NULL)
  if (!is.null(input) && file.exists(input)) {
    # knitting: return the Rmd’s directory
    return(dirname(normalizePath(input)))
  }
  # NOT knitting (interactive or running script directly)
  return(normalizePath(getwd()))
}

rmd_dir <- get_rmd_dir()

config_file <- find_config(
  paths = c("config.yaml", "../config.yaml"),
  root  = rmd_dir
)
lesson_config <- yaml.load_file(config_file)
# message("Loaded lesson config")

# -------------------------------------------------------------------
# Validate required fields
# -------------------------------------------------------------------

if (is.null(lesson_config$default_config)) {
  stop("default_config is not defined in top-level configuration: ", config_file)
}

# -------------------------------------------------------------------
# Load fallback/default config
# -------------------------------------------------------------------
load_yaml_config <- function(config_path) {
  original_path <- config_path
  
  # Normalize path separators
  config_path <- normalizePath(config_path, winslash = "/", mustWork = FALSE)
  # If the original path doesn't exist, try removing the first segment
  if (!file.exists(config_path)) {
    parts <- strsplit(config_path, "/")[[1]]
    if (length(parts) > 1) {
      new_path <- paste(parts[-1], collapse = "/")
      if (file.exists(new_path)) {
        config_path <- new_path
      }
    }
  }
  # If file still doesn't exist, stop with an error
  if (!file.exists(config_path)) {
    stop("YAML file not found: ", original_path)
  }
  # Load YAML
  config <- yaml.load_file(config_path)
  # Return named list
  list(config = config, path_used = config_path)
}
result <- load_yaml_config(lesson_config$default_config)
config <- result$config
fallback_snippets <- get_snippet_subdir(result$path_used)

# -------------------------------------------------------------------
# Load optional custom config and merge
# -------------------------------------------------------------------

# Get environment variable
custom_config_file <- Sys.getenv("HPC_CARPENTRY_CUSTOMIZATION")

# If not set, fall back to lesson_config$custom_config (which may be NULL)
if (custom_config_file == "") {
  custom_config_file <- lesson_config$custom_config
}
if (!is.null(custom_config_file)) {
  result <- load_yaml_config(custom_config_file)
  custom_config <- result$config

  # merge: custom overrides default
  config <- utils::modifyList(config, custom_config)

  # snippet directory for custom configs does NOT have to exist
  main_snippets <- get_snippet_subdir(
    result$path_used,
    must_exist = FALSE
  )
} else {
  # no custom config → only fallback snippets available
  main_snippets <- fallback_snippets
}

# message("Main config snippets from ", main_snippets, ", fallbacks from ", fallback_snippets)
# -------------------------------------------------------------------
# snippets(): pick main-override version or fallback version
# -------------------------------------------------------------------

snippets <- function(child_file, render = TRUE) {

  # Construct absolute paths to the snippet candidates
  doc_paths <- list(
    main     = file.path(main_snippets, child_file),
    fallback = file.path(fallback_snippets, child_file)
  )

  # Determine which snippet to use and store a message
  msg <- NULL
  if (file.exists(doc_paths$main)) {
    msg <- paste("Using MAIN snippet:", doc_paths$main)
    path <- doc_paths$main
  } else if (file.exists(doc_paths$fallback)) {
    msg <- paste("Using FALLBACK snippet:", doc_paths$fallback)
    path <- doc_paths$fallback
  } else {
    stop("Snippet not found: ", child_file,
         "\nMain: ",     doc_paths$main,
         "\nFallback: ", doc_paths$fallback)
  }

  # Optionally render the child here
  if (render) {
    # Write message to R console with a newline
    cat(msg, "\n", file = stderr())

    # Render the child content into the document
    cat(knitr::knit_child(path, quiet = TRUE))

    return(invisible(NULL))
  } else {
    # Or return just the path if needed
    if (!is.null(msg)) message(msg)
    return(path)
  }
}
# -------------------------------------------------------------------
# End of script
# -------------------------------------------------------------------
