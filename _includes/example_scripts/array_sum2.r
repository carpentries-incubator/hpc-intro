library(doParallel)

num_cpus <- strtoi(Sys.getenv('SLURM_CPUS_PER_TASK', unset = "1")) 
size_array <- 20000
print_progress <- interactive() # Whether to print progress or not.

seed <- strtoi(Sys.getenv('SLURM_ARRAY_TASK_ID', unset = "0"))
set.seed(seed)

registerDoParallel(num_cpus)    

sprintf("Using %i cpus to sum [ %e x %e ] matrix.",num_cpus,size_array,size_array)

results <- foreach(z=0:size_array) %dopar% {
    percent_complete= z*100/size_array
    if (print_progress && percent_complete%%1==0){
        cat(sprintf(" %i%% done...\r", percent_complete))
    }
    sum(rnorm(size_array))
}
sprintf("Seed '%s' sums to %f", seed,  Reduce("+",results))
