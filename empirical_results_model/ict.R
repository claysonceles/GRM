bla = read.csv("./teste_InterContactTimesReport.txt",sep=" ",head=F)
x = bla$V1
y = bla$V2
y2 =  1-cumsum(y)/sum(y)

bla2 = read.csv("./ict_real.csv", head = F) 
bla2 = bla2[bla2>1200]
#bla2 = bla2$V1
kkk2 = hist(bla2,breaks=seq(0,max(bla2)+10*3600,by=10*3600))
a4 = 1-cumsum(kkk2$counts/sum(kkk2$counts))

a4 = c(1,a4)

png("ict_one.png")
plot(x,y2,col="blue",ylim=c(0.00000001,1),xlim=c(10000,10000000), log="xy")
points(c(1,kkk2$mids),a4,pch=2,col="red")
legend("topright", c("GRM-100","Dartmouth"),col = c("blue","red"), pch=c(1,2))
dev.off()
