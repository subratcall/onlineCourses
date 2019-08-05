myfunction <- function(){
  x<-rnorm(100)
  mean(x)
}

second <- function(x){
  x + rnorm(length(x))
}

#getwd to get working directory
#setwd to set working directory
x<-myfunction()
x_second<-second(x)
print(x_second)

X <- 1:100
X_second<-second(X)
print(X)

############
#data types#
############

numeric_dt <- c(0.6, 0.7)
print(numeric_dt)

#coercing
coercing <- c("a", 0.5)
print(coercing)

#list 
list_1 <- list(1, "a", TRUE)
print(list_1)

#matrix
m <- matrix(nrow = 3, ncol = 4)
print(m)

m <- matrix(1:4,nrow = 3, ncol = 4)
print(m)

m<- 1:10
dim(m)<-c(2,5)
print(m)

#matrix binding
x <- 1:3
y <- 10:12

print(cbind(x,y))
print(rbind(x,y))

#factors
x<-factor(c("yes", "yes", "no"))
print(x)

print(table(x))
print(table(unclass(x)))

#missing value
x <- c(1,2,NA,10,3,NaN)
print(is.na(x))

#Data Frames
x<-data.frame(foo=1:4, bar=c(T,T,F,F))
print(x)

#Data Types - Names
x<-1:3
print(names(x))

names(x)<-c("foo", "bar", "norf")
print(names(x))

x <-list(a=1,b=2,c=3)
print(x)

m <- matrix(1:4, nrow=2, ncol=2)
dimnames(m) <-list(c("a", "b"),c("c","d"))
print(m)

#reading tabular data
#d-putting
y <-data.frame(a=1,b="a")
dput(y)

dput(y, file="y.R")
new.y<-dget("y.R")
print(new.y)

#subsettings
x<-c("a","b","c")
print(x[1])
print(x[x>"a"])

x<-list(foo=1:4, bar = 0.6)
print(x[1])
print(x$bar)




