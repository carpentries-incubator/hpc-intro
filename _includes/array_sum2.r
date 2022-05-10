library(doParallel)

num_cpus <- strtoi(Sys.getenv('SLURM_CPUS_PER_TASK', unset = "1")) 
slurm_array_task_id <- strtoi(Sys.getenv('SLURM_ARRAY_TASK_ID', unset = "-1"))
size_array <- 20000
print_progress <- interactive()
 

registerDoParallel(num_cpus)    
set.seed(slurm_array_task_id)

sprintf("Using %i cpus to sum [ %e x %e ] matrix.",num_cpus,size_array,size_array)

results <- foreach(z=0:size_array) %dopar% {
    percent_complete= z*100/size_array
    if (print_progress && percent_complete%%1==0){
        cat(sprintf(" %i%% done...\r", percent_complete))
    }
    sum(rnorm(size_array))
}
sprintf("Seed '%s' sums to %f", slurm_array_task_id,  Reduce("+",results))
