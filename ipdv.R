# Title     : TODO
# Objective : TODO
# Created by: sobakapavlova
# Created on: 27/05/2018
ipdv <- function(delays){
    jitter = vector()
    jitter[1] = 4
    for (i in 2:length(delays)){
        jitter[i] = abs(delays[i-1] - delays[i])
    }
    return(jitter)
}
