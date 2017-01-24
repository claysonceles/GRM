
#bla = read.csv("group_size_mit.csv", head = F) 
bla = read.csv("../teste.csv", head = F) 
#print(min(bla$V1))
bla = bla[bla$V1 != 0,]

kkk = hist(bla,breaks=seq(0,max(bla)+60,by=60))


 
a = kkk$counts/sum(kkk$counts)

png("group_size1.png")
plot(kkk$mids,a,main="PDF",xlab="Group Size")
dev.off()

a2 = cumsum(a)

png("group_size3.png")
plot(kkk$mids,a2,main="CDF",xlab="Group Size",type="l")
dev.off()

a3 = 1-cumsum(a)

png("group_size2.png")
plot(kkk$mids,a3, main="ECCDF Dartmouth",log="xy",xlab="Group Size",type="l",xlim=c(100,100000),ylim=c(0.0001,1))
dev.off()

require("poweRlaw")

source("http://tuvalu.santafe.edu/~aaronc/powerlaws/plfit.r")

moby = round(bla)
fit = plfit(moby)
m_pl = displ$new(moby)
pars = estimate_pars(m_pl)


#print(m_pl)
#est = estimate_xmin(m_pl)
#print(est)
#m_pl$setXmin(est)

bla = rpldis(1000,600,alpha = 2.5)
kkk2 = hist(bla,breaks=seq(min(bla),max(bla)+60,by=60))

a4 = 1-cumsum(kkk2$counts/sum(kkk2$counts))

m_pl$setPars(pars)
png("pl_fit.png")
plot(kkk$mids,a3, main="ECCDF Dartmouth",log="xy",xlab="Group Size",type="l",xlim=c(100,100000),ylim=c(0.0001,1),col="red")
lines(kkk2$mids,a4,lwd=2)
legend("topright", c("empirical","fitting"),col = c("red","black"), lty=c(1,1))
dev.off()
