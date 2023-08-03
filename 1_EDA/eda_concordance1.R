library(networkD3)
library(dplyr)
library(data.table)

# read data
data <-fread('/Users/smasarone/Documents/jupyter_notebooks_copy2/sankey2.csv')%>% as.data.frame()
data$V1<-NULL

names <-fread('/Users/smasarone/Documents/jupyter_notebooks_copy2/names2.csv')%>% as.data.frame()
names <-names[-1, ]
names$V1<-NULL

sankeyNetwork(Links = data, Nodes = names, Source = "source",
              Target = "target", Value = "value",NodeID = "V2",
              fontSize = 12, nodeWidth = 20)

# a big chunck of them are conserved

