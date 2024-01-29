#R taxize
library(taxize)
file <- readLines('dataset_list.txt')

for (a in file) {
line <- tax_name(sci = a, get = c('order','family'), db = "ncbi")[1,c(3,4,2)]
write(as.character(line),file='dataset_order.txt',append=TRUE)
}
