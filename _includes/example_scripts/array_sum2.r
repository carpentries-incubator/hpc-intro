#!/usr/bin/env Rscript

library(doParallel)

num_cpus <- strtoi(Sys.getenv('SLURM_CPUS_PER_TASK', unset = "1")) 
size_x <-60000 # This on makes memorier
size_y <-20000 # This one to make longer

# Time = (size_x/n) * size_y + c
# Mem  = (size_x * n) * c1 + size_y * c2

print_progress <- interactive() # Whether to print progress or not.

seed <- strtoi(Sys.getenv('SLURM_ARRAY_TASK_ID', unset = "0"))
set.seed(seed)

registerDoParallel(num_cpus)

sprintf("Using %i cpus to sum [ %e x %e ] matrix.",num_cpus,size_x,size_y)

results <- foreach(z=0:size_x) %dopar% {
    p_complete= z*100/size_x
    if (print_progress && percent_complete%%1==0){
        cat(sprintf(" %i%% done...\r", percent_complete))
    }
    sum(rnorm(size_y))
}
sprintf("Seed '%s' sums to %f", seed,  Reduce("+",results))
