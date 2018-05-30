# function to calculate jitter via 3rd method

getJitter <- function(delays){
    jitter <- vector()
    jitter[1] <- 3
    for (i in 2:length(delays)){
	    jitter[i] <- abs(delays[i] - delays[1])
    }
    return(jitter)
}
