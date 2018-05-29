# function to calculate jitter via 1st method

jitterMin <- function(delays){
    jitter = vector()
    jitter[1] = 1
    for (i in 2:length(delays)){
        minDealay = min(delays[1:i-1])
	    jitter[i] = sample[i] - minDealay
    }
    return(jitter)
}
