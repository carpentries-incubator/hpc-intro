library(doParallel)

num_cpus <- strtoi(Sys.getenv('SLURM_CPUS_PER_TASK', unset = "1")) 
size_array <- 20000

registerDoParallel(num_cpus)

sprintf("Using %i cpus to sum [ %e x %e ] matrix.",num_cpus,size_array,size_array)

results <- foreach(z=0:size_array) %dopar% {
    p_complete= z*100/size_array
    if (p_complete%%1==0){
        print(sprintf("%i%% done...", p_complete))
    }
    sum(rnorm(size_array))
}
sprintf("Sum is '%f'.", Reduce("+",results))