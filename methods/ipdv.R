# function to calculate jitter via 4th method

getJitter <- function(delays){
    jitter <- vector()
    jitter[1] <- 4
    for (i in 2:length(delays)){
        jitter[i] <- abs(delays[i-1] - delays[i])
    }
    return(jitter)
}
