library(doParallel)

num_cpus <- 2
size_array <- 20000 

registerDoParallel(num_cpus)    

sprintf("Using %i cpus to sum [ %e x %e ] matrix.",num_cpus,size_array,size_array)

results <- foreach(z=0:size_array) %dopar% {
    percent_complete= z*100/size_array
    if (percent_complete%%1==0){
        cat(sprintf(" %i%% done...\r", percent_complete))
    }
    sum(rnorm(size_array))
}
sprintf("Sums to %f",  Reduce("+",results))
