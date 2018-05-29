arguments = commandArgs(trailingOnly=TRUE)
filename = arguments[1]
stopifnot(exists("filename"))
stopifnot(file.exists(filename))

sample = as.integer(readLines(filename))
sample_size = length(sample)
endY = max(sample) + 0.05 * (max(sample) - min(sample)) / 0.9
startY = min(sample) - 0.05 * (max(sample) - min(sample)) / 0.9
step = (endY - startY) %% 10

# first method:
jitter_min = vector()
for (i in 2:length(sample)){
	minDealay = min(sample[1:i-1])
	jitter_min[i-1] = sample[i] - minDealay
}

# second method:
jitter_mean = vector()
for (i in 2:length(sample)) {
	meanForSample = mean(sample[1:i-1])
	jitter_mean[i-1] = abs(sample[i] - meanForSample)
    # print(jitter_mean[i-1])
}

jitter_first = vector()

for (i in 2:length(sample)) {
	jitter_first[i-1] = sample[i] - sample[2]
}

ipdv = vector()

for (i in 2:length(sample)) {
	ipdv[i-1] = abs(sample[i] - sample[i-1])
    # print(ipdv[i-1])
}
image_name = paste(basename(filename), ".png", sep="", collapse = NULL)
png(image_name)
plot(x=0, y=0, xlim=c(0, length(sample)), ylim=c(-10 , endY), type="n", xlab="package number", ylab="jitter")
# plot(x=0, y=0, xlim=c(0, length(sample)), ylim=c(1, endY), type="n", xlab="package number", ylab="jitter", log='y')

# plot(sample_sizes, seq(10, 150, 10), type="l", xlab="sample size", ylab="jitter, ms")


#plot(seq(100, 1000, 100), seq(0, 360, 40), type="n", xlab="sample size", ylab="jitter_mean")
points(1:length(jitter_mean), jitter_mean, type="l", col="green")

points(1:length(jitter_first), jitter_first, type="l", col="blue")

points(1:length(ipdv), ipdv, type="l", col="yellow")

dev.off()

print(quantile(jitter_mean, probs=0.99))
print(quantile(jitter_min, probs=0.99))
print(quantile(jitter_first, probs=0.99))
print(quantile(ipdv, probs=0.99))
# summa = sum(jitter_mean))
# print(summa)
