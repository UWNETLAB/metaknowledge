# John McLevey
# University of Waterloo
# April 14, 2015

# note: this script is intended to be run from the command line (Rscript *.R) 
# to get a quick look at a graphml file created by RMY's co-citeMaker.py
# hence all the print() 

library(igraph)
library(dplyr)

wd <- getwd()
setwd(wd)

net <- read.graph("co-CiteNetwork.graphml", format = "graphml")
net <- simplify(net, remove.multiple = TRUE, remove.loops = TRUE) 
summary(net)

sum(degree(net)==0) # no. of isolates 
net <- delete.vertices(net, which(degree(net)<1)) # delete isolates

# quick look  
nodes <- length(V(net))
edges <- length(E(net))
isolates <- sum(degree(net)==0)
components <- no.clusters(net) 

  # size of the two largest components 
net_num.components <- clusters(net)$no
net_components <- clusters(net, mode="weak")
net_compsize <- sort(net_components$csize, decreasing=TRUE)
comp1 <- net_compsize[1] 
comp2 <- net_compsize[2]

  # cohesion 
density <- graph.density(net)
diameter <- diameter(net)
average_path_length <- average.path.length(net) 
degree_centralization <- centralization.degree(net)$centralization 
eigenvector_centralization <- centralization.evcent(net, directed=FALSE)$centralization
transitivity <- transitivity(net, type="global")
cliques <- clique.number(net)

wholenet_stats <- rbind(nodes, edges, isolates, components, comp1, comp2, cliques,
                        density, diameter, average_path_length, degree_centralization,
                        eigenvector_centralization, transitivity)
wholenet_stats
write.csv(wholenet_stats, "wholenet_stats.csv")

# test for power law distribution 
pdf("log_log_deg_dist.pdf")
plot(degree.distribution(net, cumulative = TRUE), 
	log="xy", col = rgb(0, 0, .5, .5), 
	xlab = "Degree", ylab = "Cumulative Probability") 
dev.off()

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

# restrict to giant component 

print("pulling out the giant component...")

g_net <- clusters(net)
net <- induced.subgraph(net, which(g_net$membership == which.max(g_net$csize)))
summary(net)

# fast and greedy community detection 

fg <- fastgreedy.community(simplify(as.undirected(net)))
fast_greedy <- length(fg)

memb <- community.to.membership(net, fg$merges, steps=which.max(fg$modularity)-1)

colbar <- rainbow(length(fg))
col <- colbar[memb$membership+1]

# walk trap community detection

wc <- walktrap.community(net)
walktrap <- length(wc)
# modularity(wc)
# membership(wc)

V(net)$walktrap <- membership(wc)

community_detection <- rbind(fast_greedy, walktrap)
community_detection

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
