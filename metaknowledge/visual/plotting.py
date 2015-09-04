import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi

def quickGraph(G):
    nx.draw_spring(G)
    plt.show()



def graphDensityContourPlot(G, layout = None, layoutScaleFactor = 1, shifAxis = False, overlay = False, axisSamples = 100, blurringFactor = .1, contours = 15, nodeSize = 10, graphType = 'coloured', iters = 50):
    """
    Requires numpy and matplotlib
    
    graphType is either "coloured or "solid"
    """
    from mpl_toolkits.mplot3d import Axes3D


    if not isinstance(G, nx.classes.digraph.DiGraph) and not isinstance(G, nx.classes.graph.Graph):
        raise TypeError("{} is not a valid input.".format(type(G)))
    if layout is None:
        layout = nx.spring_layout(G, scale = axisSamples - 1, iterations = iters)
        grid = np.zeros( [axisSamples, axisSamples],dtype=np.float32)
        for v in layout.values():
            x, y = tuple(int(x) for x in v.round(0))
            grid[y][x] += 1
    elif isinstance(layout, dict):
        layout = layout.copy()
        grid = np.zeros([axisSamples, axisSamples],dtype=np.float32)
        multFactor = (axisSamples - 1) / layoutScaleFactor
        for k in layout.keys():
            if shifAxis:
                tmpPos = (layout[k]  + layoutScaleFactor / 2) * multFactor
            else:
                tmpPos = layout[k] * multFactor
            layout[k] = tmpPos
            x, y = tuple(int(x) for x in tmpPos.round(0))
            grid[y][x] += 1
    else:
        raise TypeError("{} is not a valid input.".format(type(layout)))

    fig = plt.figure()
    #axis = fig.add_subplot(111)
    axis = fig.gca(projection='3d')
    if overlay:
        nx.draw_networkx(G, pos = layout, ax = axis, node_size = nodeSize, with_labels = False, edgelist = [])
    grid = ndi.gaussian_filter(grid, (blurringFactor * axisSamples, blurringFactor * axisSamples))
    X = Y = np.arange(0, axisSamples, 1)
    X, Y = np.meshgrid(X, Y)
    if graphType == "solid":
        CS = axis.plot_surface(X,Y, grid)
    else:
        CS = axis.contourf(X, Y, grid, contours)
    axis.set_xlabel('X')
    axis.set_ylabel('Y')
    axis.set_zlabel('Node Density')
