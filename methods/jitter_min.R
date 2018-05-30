# function to calculate jitter via 1st method

getJitter <- function(delays){
    jitter <- numeric()
    jitter[1] <- 1
    for (i in 2:length(delays)){
        minDealay <- min(delays[1:i-1])
	    jitter[i] <- delays[i] - minDealay
    }
    return(jitter)
}
