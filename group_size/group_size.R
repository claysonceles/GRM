
bla = read.csv("group_size_dt.csv", head = F) 
kkk = hist(bla$V1,breaks=seq(0,max(bla$V1)+1,by=1))

a = kkk$density
print(min(bla$V1))

png("group_size1.png")
plot(kkk$mids,a,main="PDF",xlab="Group Size")
dev.off()

a = cumsum(kkk$density)

png("group_size3.png")
plot(kkk$mids,a,main="CDF",xlab="Group Size",type="l")
dev.off()

a3 = 1-cumsum(kkk$density)

png("group_size2.png")
plot(kkk$mids,a, main="ECCDF Dartmouth",log="xy",xlab="Group Size",type="l")
dev.off()

require("poweRlaw")

moby = round(bla$V1)
m_pl = displ$new(moby)

m_pl$setXmin(3)
pars = estimate_pars(m_pl)
m_pl$setPars(pars)



bla2 = read.csv("../fit.csv",head=F)
kkk2 = hist(bla2$V1,breaks=seq(min(bla2$V1),max(bla2$V1)+1,by=1))

a4 = 1-cumsum(kkk2$counts/sum(kkk2$counts))

m_pl$setPars(pars)
png("pl_fit.png")
plot(kkk$mids,a3, main="ECCDF Dartmouth",log="xy",xlab="Group Size",col="red",xlim = c(1,100),ylim=c(0.0001,1))
points(kkk2$mids,a4,lwd=2)
legend("topright", c("empirical","fitting"),col = c("red","black"), pch=c(1,1))
dev.off()
