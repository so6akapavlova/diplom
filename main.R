# script to calculate jitter and draw plots
image_dir = "images"

arguments <- commandArgs(trailingOnly=TRUE)
stopifnot(length(arguments) > 1)
quantiles <- numeric()
method_list <- c("jitter_min", "jitter_mean", "jitter_first", "ipdv")
line_colors <- c("green", "blue", "red", "yellow")
filename <- arguments[1]

stopifnot(exists("filename"))
stopifnot(file.exists(filename))

delays <- as.integer(readLines(filename))
endY = max(delays) + 0.05 * (max(delays) - min(delays)) / 0.9


dir.create(image_dir, showWarnings = FALSE)
image_name = file.path(image_dir, paste(basename(filename), ".png", sep=""))
png(image_name)
plot(x=0, y=1, xlim=c(0, length(delays)), ylim=c(1 , endY), type="n", xlab="package number", ylab="jitter", log="y")

for (method_number in arguments[2:length(arguments)]){
    if (strtoi(method_number) %in% seq(1:4)){
        method_script <- paste("methods/", method_list[strtoi(method_number)], ".R", sep="")
        source(method_script)
        values <- getJitter(delays)
        quantiles <- c(quantiles, round(quantile(values[2:length(values)], probs=0.99, names = FALSE)/1000 ,digits = 2))
        points(1:length(values), values, type="l", col=line_colors[strtoi(method_number)])
    } else {
        print(paste("There are no method with number ", method_number, ". Please use numbers from 1 to 4", sep=""))
    }
}
write(c(basename(filename), quantiles), file="quantiles.txt", append=TRUE)
garbage <- dev.off()
