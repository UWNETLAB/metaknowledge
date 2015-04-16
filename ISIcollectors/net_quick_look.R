# John McLevey
# University of Waterloo
# April 14, 2015

library(igraph)
library(dplyr)

setwd("/Users/johnmclevey/Dropbox/Projects/writing/crs/porter_to_bourdieu/v2/data/canadian/split_years/t5")

net <- read.graph("co-CiteNetwork.graphml", format = "graphml")
net <- simplify(net, remove.multiple = TRUE, remove.loops = TRUE) 
summary(net)

sum(degree(net)==0) # no. of isolates 
net <- delete.vertices(net, which(degree(net)<1)) # delete isolates

# quick look  

print("no. of components:")
no.clusters(net) # no. of components 

print("no. of nodes:")
length(V(net)) # no. of vertices

print("no. of edges:")
length(E(net)) # no. of edges

print("no. of isolates:")
sum(degree(g18)==0)

  # test for power law distribution 
pdf("log_log_deg_dist.pdf")
plot(degree.distribution(net, cumulative = TRUE), 
     log="xy", xlab = "Degree", ylab = "Cumulative Probability",
     col = "red", type = "o")
dev.off()

# cohesion 
print("density:")
graph.density(net)

print("diameter:")
diameter(net)

print("average path length:")
average.path.length(net) 

print("degree centralization:")
centralization.degree(net)$centralization 

print("eigenvector centralization:")
centralization.evcent(net, directed=FALSE)$centralization

print("transitivity:")
transitivity(net, type="global")

print("number of cliques:")
clique.number(net)

# centralities 

    # normalized degree centrality
n <- vcount(net)
degree.norm <- degree(net)/(n-1)

    # betweenness centrality
betweennesscent <- betweenness(net)
names(betweennesscent) <- V(net)$name
ind <- order(-betweennesscent)
# betweennesscent[ind][1:20] # show top 20 betweenness scores

    # normalized betweenness centrality
n <- vcount(net)
betweenness.norm <- betweenness(net)/(0.5*(n-1)*(n-2))  # undirected
ind <- order(-betweenness.norm)
# betweenness.norm[ind][1:20]

    # eigenvector centrality
eigenvectorcent <- igraph::evcent(net)$vector
ind <- order(-eigenvectorcent)
# eigenvectorcent[ind][1:20] # show top 20 eigenvector scores

    # write out 
net_node_stats <- cbind(V(net)$id, degree, degree.norm, betweenness.norm, eigenvectorcent)
write.csv(net_node_stats, "net_node_stats.csv")

# glimpse(node_statistics)

# tie centrality scores to nodes 
V(net)$degree.R <- degree(net)
V(net)$betweenness.R <- betweenness(net)
V(net)$eigenvector.R <- igraph::evcent(net)$vector

# fast and greedy community detection 

fg <- fastgreedy.community(simplify(as.undirected(net)))
print("fast and greedy community detection, number of communities:")
length(fg)

memb <- community.to.membership(net, fg$merges, steps=which.max(fg$modularity)-1)
#memb

#plot(fg, net, vertex.label = NA)

colbar <- rainbow(length(fg))
col <- colbar[memb$membership+1]

# walk trap community detection

wc <- walktrap.community(net)
# modularity(wc)
# membership(wc)

V(net)$walktrap <- membership(wc)

# quick plot

#print("time for fg layout")

#lay <- layout.fruchterman.reingold(net, niter=1000, coolexp=0.5,
#                                   area=vcount(net)^2.3,
#                                   repulserad=vcount(net)^2.8)

#lay <- layout.fruchterman.reingold(net, niter=1000, coolexp=0.5,
#                                   area=vcount(net)^2.3,
#                                   repulserad=vcount(net)^2.8)

#pdf(file="net_walktrap.pdf")
#plot(net, layout = lay, vertex.size = 2, edge.width = .5, 
#     vertex.label = NA, vertex.color = membership(wc), vertex.frame.color = NA)
#dev.off()

#pdf(file = "net_fastgreedy.pdf")
#set.seed(3952)
#par(mar=c(0,0,0,0)+.1) # reduce extra whitespace
#plot(net, layout = lay, vertex.size = 2, edge.width = .5, 
#     vertex.label = NA, vertex.color = col, vertex.frame.color = NA)
#dev.off()

# for visone 

write.graph(net, format="graphml", file="co-CiteNetwork.graphml")
