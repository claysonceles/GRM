
#bla = read.csv("group_size_mit.csv", head = F) 
bla = read.csv("../teste.csv", head = F) 
#print(min(bla$V1))

lambda = 1/mean(bla$V1)
kkk = hist(bla$V1,breaks=seq(0,max(bla$V1)+3600,by=3600))

print(1/lambda)

bla2 = read.csv("../teste.csv", head = F)
kkk2 = hist(bla2$V1,breaks = seq(0,max(bla2)+3600,by=3600))

a = kkk$density
b = kkk2$density

png("group_size1.png")
plot(kkk$mids,a,main="PDF",xlab="Group Size")
lines(kkk2$mids,b,col="red",lwd=3)
dev.off()

a = cumsum(kkk$density)
b = cumsum(kkk2$density)

png("group_size3.png")
plot(kkk$mids,a,main="CDF",xlab="Group Size",type="l")
lines(kkk2$mids,b,col="red",lwd=3)
dev.off()

a = 1-cumsum(kkk$density)
b = 1-cumsum(kkk2$density)

png("group_size2.png")
plot(kkk$mids,a, main="ECCDF Dartmouth",log="xy",xlab="Group Size",type="l")
lines(kkk2$mids,b,col="red",lwd=2)
dev.off()

require("poweRlaw")

moby = round(bla$V1 +1)
m_pl = displ$new(moby)
pars = estimate_pars(m_pl)
est = estimate_xmin(m_pl)
#print(m_pl)
#est = estimate_xmin(m_pl)
#print(est)
#m_pl$setXmin(est)

m_pl$setPars(pars)
png("pl_fit.png")
plot(m_pl, main="CCDF Dartmouth",xlab="Group Size",type="l", col="red", lwd=2)
points(kkk$mids,a,lwd=2)
dev.off()
