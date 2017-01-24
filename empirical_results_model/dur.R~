dt = read.csv("/home/ivan/Dropbox/mestrado/datasets2/dartmouth/1200_sample.csv", head = F, sep = " ")
#kkk = hist(bla$V3,breaks=seq(0,max(bla$V3)+60,by=60))
#dt = dt[dt$V4<3600*24,]
dt_s = hist(dt$V4,breaks=seq(0,max(dt$V4)+60,by=60))
dt_p = 1-cumsum(dt_s$counts/sum(dt_s$counts))


bla = read.csv("../contacts_test.csv",sep=" ",head=F)
bla = bla[bla$V4>600,]
bla = hist(bla$V4,breaks=seq(0,max(bla$V4)+60,by=60))
y = 1-cumsum(bla$counts/sum(bla$counts))
x = bla$mids

#bla = read.csv("./teste_ContactTimesReport.txt",sep=" ",head=F)
#bla = read.csv("../contacts_test.txt",sep=" ",head=F)
#x = bla$V1
#y = bla$V2

#y2 = 1 - cumsum(y)/sum(y)

x_lim = max(c(max(dt_s$mids),max(x)))

x3 = c(1,dt_s$mids)
y3 = c(1,dt_p)
png("dur_one.png")
plot(x,y,col="blue",xlim=c(1000,x_lim),ylim=c(0.00000001,1),log="xy")#,log="xy")
points(x3,y3,pch=2,col="red")
legend("topright", c("GRM-100","Dartmouth"),col = c("blue","red"), pch=c(1,2))
dev.off()
