# John McLevey
# University of Waterloo
# April 14, 2015

# note: this script is intended to be run from the command line (Rscript *.R) 
# to get a quick look at a graphml file created by RMY's co-citeMaker.py

library(igraph)
library(dplyr)
options(scipen=20)

wd <- getwd()
setwd(wd)

net <- read.graph("co-CiteNetwork.graphml", format = "graphml")
net <- as.undirected(net, mode = "collapse")
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
transitivity <- transitivity(net, type="global")
cliques <- clique.number(net)
degree_centralization <- centralization.degree(net, mode="all", normalize=TRUE)$centralization 
eigenvector_centralization <- centralization.evcent(net, directed=FALSE, scale=FALSE, normalized=TRUE)$centralization
#betweenness_centralization <- centralization.betweenness(net, directed = TRUE, nobigint = TRUE, normalized = TRUE)
# betweenness_centralization

wholenet_stats <- rbind(nodes, edges, isolates, components, comp1, comp2, cliques,
                        density, diameter, average_path_length, degree_centralization,
                        eigenvector_centralization, transitivity)
wholenet_stats
write.csv(wholenet_stats, file = "wholenet_stats.csv")

# test for power law distribution 
pdf("log_log_deg_dist.pdf")
plot(degree.distribution(net, cumulative = TRUE), 
	log="xy", col = rgb(0, 0, .5, .5), 
	xlab = "Degree", ylab = "Cumulative Probability") 
dev.off()

# centralities 

	# restrict to giant component 

g_net <- clusters(net)
g_net <- induced.subgraph(net, which(g_net$membership == which.max(g_net$csize)))
print("Restricted to giant component for analyzing centralities")
summary(g_net)

    # degree
degree <- degree(g_net)
print("top 20 degree centrality")
dc <- cbind(V(g_net)$id[order(-degree)][1:20], degree[order(-degree)][1:20])
colnames(dc) <- c("NODE", "DEGREE")
dc

    # betweenness centrality
betweenness <- betweenness(g_net)
print("top 20 betweenness centrality")
bc <- cbind(V(g_net)$id[order(-betweenness)][1:20], betweenness[order(-betweenness)][1:20])
colnames(bc) <- c("NODE", "BETWEENNESS_CENTRALITY")
bc


    # normalized betweenness centrality 
n <- vcount(g_net)
betweenness.norm <- betweenness(g_net)/(0.5*(n-1)*(n-2))  # undirected
print("top 20 betweenness centrality normalized")
bcn <- cbind(V(g_net)$id[order(-betweenness.norm)][1:20], betweenness.norm[order(-betweenness.norm)][1:20])
colnames(bcn) <- c("NODE", "BETWEENNESS_NORM_CENTRALITY")
bcn

    # eigenvector centrality
eigen <- evcent(g_net, directed = F, scale=F)$vector
ec <- cbind(V(g_net)$id[order(-eigen)][1:20], eigen[order(-eigen)][1:20])
colnames(ec) <- c("NODE", "EIGENVECTOR_CENTRALITY")
ec

	# closeness centrality 

close <- closeness(g_net, mode="all")
cc <- cbind(V(g_net)$id[order(-close)][1:20], close[order(-close)][1:20])
colnames(cc) <- c("NODE", "CLOSENESS_CENTRALITY")
cc

    # write centralities

write.table(dc, file = "cents_degree.csv", sep=",", row.names=F)
write.table(bc, file = "cents_betweenness.csv", sep=",", row.names=F)
write.table(bcn, file = "cents_betweenness_norm.csv", sep=",", row.names=F)
write.table(ec, file = "cents_eigenvector.csv", sep=",", row.names=F)

cents_all <- cbind(V(g_net)$id, degree, betweenness, betweenness.norm, eigen)
write.table(cents_all, file = "cents_all.csv", sep=",", row.names=F)

# glimpse(node_statistics)

# tie centrality scores to nodes 
V(g_net)$degree.R <- degree(g_net)
V(g_net)$betweenness.R <- betweenness(g_net)
V(g_net)$eigenvector.R <- evcent(g_net)$vector

# fast and greedy community detection 

print("Fast and greedy community detection")
fg <- fastgreedy.community(simplify(as.undirected(net)))
fast_greedy <- length(fg)

memb <- community.to.membership(net, fg$merges, steps=which.max(fg$modularity)-1)

colbar <- rainbow(length(fg))
col <- colbar[memb$membership+1]

# walk trap community detection

print("Walktrap community detection")
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
write.graph(net, format="edgelist", file="co-CiteNetwork.csv")
