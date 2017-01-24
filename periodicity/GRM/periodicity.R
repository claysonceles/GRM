suppressMessages(library(splines))



bla = read.csv("ict.csv",head=F)
bla = bla[bla$V1>0,]
bla = bla[bla< 400]
a = hist(bla,breaks = seq(0,400,by=1))
png("periodicity.png")
plot(a$mids,a$counts/sum(a$counts),type="l",xlim = c(0,400),xlab = "Time(h)", ylab="Frequency of group reencounters")
abline(v=seq(24,720,by=24),lty=3,col="red",lwd=1)
abline(v=seq(7*24+2,720,by=7*24),lty=2,col="green",lwd=1)
dev.off()

png("auto_corr.png")
acf(a$counts/sum(a$counts), lag.max = 400,xlab="lag (h)",ylab="Auto-Correlation Function", main="")
abline(v=seq(24,720,by=24),lty=3,col="red",lwd=1)
abline(v=seq(7*24+2,720,by=7*24),lty=2,col="green",lwd=1)
dev.off()
