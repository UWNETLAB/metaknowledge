import metaknowledge
from .graphHelpers import _ProgressBar

import copy

#Based on Fast unfolding of communities in large networks http://arxiv.org/abs/0803.0476v2

def blondel(G, weightParameter = None, communityParameter = 'community'):
    if metaknowledge.VERBOSE_MODE:
        PBar = _ProgressBar(0, "Starting community detection")
        iterations = 1
        count = 0
    else:
        PBar = None
    communityDict = {}
    workingGrph = G.copy()
    for i, n in enumerate(G.nodes_iter()):
        workingGrph.node[n][communityParameter] = i
        communityDict[i] = [n]
    Qprevious = -2
    Qcurrent = modularity(workingGrph, weightParameter, communityParameter)
    communityToNode = copy.deepcopy(communityDict)
    while Qcurrent > Qprevious:
        m = get_m(G, weightParameter)
        newGrph = workingGrph.copy()
        for n, nDict in workingGrph.nodes_iter(data = True):
            if PBar:
                PBar.updateVal(count/len(workingGrph), "Processing sweep {0}, node {1} modularity is {2:.2f}".format(iterations, str(n), Qcurrent))
                count +=1
            current_com = nDict[communityParameter]
            currentMax = (0, current_com)
            for new_com in communityDict.keys():
                if new_com != current_com:
                    swapVal = deltaQswap(newGrph, n, new_com, communityDict, weightParameter, communityParameter, mVal = m)
                    if swapVal > currentMax[0]:
                        currentMax = (swapVal, new_com)
            if currentMax[0] > 0:
                newGrph.node[n][communityParameter] = currentMax[1]
                communityDict[current_com].remove(n)
                communityDict[currentMax[1]].append(n)
                if len(communityDict[current_com]) < 1:
                    del communityDict[current_com]
                try:
                    communityToNode[currentMax[1]] += communityToNode[current_com]
                    del communityToNode[current_com]
                except KeyError:
                    pass
        if PBar:
            PBar.updateVal(1, "Trimming sweep {0}, Q = {1:.1%}".format(iterations, Qcurrent))
            count = 0
            iterations += 1
        for com, nds in communityDict.items():
            if len(nds) > 1:
                for nd in nds[1:]:
                    merge_nodes(newGrph, nds[0], nd)
                communityDict[com] = [nds[0]]
        Qprevious = Qcurrent
        Qcurrent = modularity(newGrph, weightParameter, communityParameter)
        workingGrph = newGrph
    workingGrph = G.copy()
    if PBar:
        PBar.updateVal(1, "Done, updating graph")
    comNumList = list(communityToNode.keys())
    for ndcom, ndlst in communityToNode.items():
        for n in ndlst:
            workingGrph.node[n][communityParameter] = str(comNumList.index(ndcom))
    if PBar:
        PBar.finish("Done detecting communities in " + str(iterations) + " sweeps")
    return workingGrph

def modularity(G, weightParameter = None, communityParameter = 'community'):
    """
    Gets modularity of network, currently not tuned
    """
    m = 0
    kktot = 0
    Atot = 0
    for n_i in G.nodes_iter():
        for n_j in G.nodes_iter():
            A_ij = get_edgeVal(G, n_i, n_j, weightParameter)
            m += .5 * A_ij
            if G.node[n_i][communityParameter] == G.node[n_j][communityParameter]:
                Atot += A_ij
                kktot += get_kVal(G, n_i, weightParameter) * get_kVal(G, n_j, weightParameter)
    return ((Atot - 0.5 * kktot / m) / ( 2 * m))


def deltaQ(G, n, communitylst, weightParameter = 'weight', mCurrent = None):
    """
    Gets the change in modularity of a network by adding a single node, currently not tuned
    """
    if mCurrent:
        inversm = .5 / mCurrent
    else:
        inversm = .5 / get_m(G, weightParameter)
    Sigma_in = get_CommunityWeight(G, communitylst, weightParameter, internal = True)
    Sigma_tot = get_CommunityWeight(G, communitylst, weightParameter, internal = False)
    k_i = get_kVal(G, n, weightParameter)
    k_i_in = 0
    for e in G.edges_iter(communitylst, data = True):
        if e[1] == n:
            if weightParameter:
                k_i_in += e[2][weightParameter]
            else:
                k_i_in += 1
    dQ = Sigma_in + k_i_in - (Sigma_tot + k_i) * (Sigma_tot + k_i) * inversm
    dQ -= Sigma_in - Sigma_tot * Sigma_tot * inversm - k_i * k_i * inversm
    return dQ * inversm

def deltaQswap(G, n, newCom, comDict, weightParameter, communityParameter, mVal = None):
    oldCom = G.node[n][communityParameter]
    oldComlst = comDict[oldCom].copy()
    oldComlst.remove(n)
    oldDQ = deltaQ(G, n, oldComlst, weightParameter, mCurrent = mVal)
    newDQ = deltaQ(G, n, comDict[newCom], weightParameter, mCurrent = mVal)
    return newDQ - oldDQ

def merge_nodes(G, n1, n2):
    G.add_edges_from((n1, e[1], e[2]) for e in G.edges_iter(n2, data = True))
    G.remove_node(n2)

def get_m(G, weightParameter):
    m = 0
    if weightParameter:
        for e in G.edges_iter(data = True):
            m += e[2][weightParameter]
    else:
        return len(G.edges())
    return m

def get_kVal(G, n, weightParameter):
    """
    Helper function to get the total weight of all edges to a node
    """
    if weightParameter:
        retk = 0
        for e in G.edges_iter(n, data = True):
            retk += e[2][weightParameter]
    else:
        retk = len(G.edges(n))
    return retk


def get_CommunityWeight(G, community, weightParameter, internal = False):
    retTot = 0
    for e in G.edges_iter(community, data = True):
        if internal:
            if e[0] in community and e[1] in community:
                if weightParameter:
                    retTot += e[2][weightParameter]
                else:
                    retTot += 1
        else:
            if weightParameter:
                retTot += e[2][weightParameter]
            else:
                retTot += 1
    return retTot

def get_edgeVal(G, n1, n2, weightParameter):
    """
    Helper function to obtain the weight of the edge between two nodes, with exception handling, returns 0 if no edge is found
    """
    if weightParameter:
        try:
            valDict = G.edge[n1][n2]
        except KeyError:
            return 0
        else:
            return valDict[weightParameter]
    else:
        return 1
