library(ggplot2)
setwd("~/Dropbox/code/londoncraigslist/munge/comparison")
mw <- read.table("cleanedm4w:w4mtitle.txt",header=T)
cs <- read.table("cleanedcas:stptitle.txt",header=T)
m <- merge(cs, mw)
attach(m)
ms <- m[order(-m4wt),]
mss <- head(ms, 20)