bla = read.csv("first_trace.csv",head=F,sep=" ")
print("reading done")
bla = bla[order(bla$V1),]
bla$V5 = NULL
bla$V6 = NULL
write.table(bla,"sorted_trace.csv",sep =" ",row.names=F,col.names=F,na="")
