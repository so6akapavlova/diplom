# function to calculate jitter via 3rd method

jitterFirst <- function(delays){
    jitter = vector()
    jitter[1] = 3
    for (i in 2:length(delays)){
	    jitter[i] = sample[i] - delays[1]
    }
    return(jitter)
}

