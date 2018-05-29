# function to calculate jitter via 2nd method

jitterMean <- function(delays){
    jitter = vector()
    jitter[1] = 2
    for (i in 2:length(delays)){
        meanDealay = mean(delays[1:i-1])
	    jitter[i] = sample[i] - meanDealay
    }
    return(jitter)
}

