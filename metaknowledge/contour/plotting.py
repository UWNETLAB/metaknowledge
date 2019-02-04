#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi
import math

def quickVisual(G, showLabel = False):
    """Just makes a simple _matplotlib_ figure and displays it, with each node coloured by its type. You can add labels with _showLabel_. This looks a bit nicer than the one provided my _networkx_'s defaults.

    # Parameters

    _showLabel_ : `optional [bool]`

    > Default `False`, if `True` labels will be added to the nodes giving their IDs.
    """
    colours = "brcmykwg"
    f = plt.figure(1)
    ax = f.add_subplot(1,1,1)
    ndTypes = []
    ndColours = []
    layout = nx.spring_layout(G, k = 4 / math.sqrt(len(G.nodes())))
    for nd in G.nodes(data = True):
        if 'type' in nd[1]:
            if nd[1]['type'] not in ndTypes:
                ndTypes.append(nd[1]['type'])
            ndColours.append(colours[ndTypes.index(nd[1]['type']) % len(colours)])
        elif len(ndColours) > 1:
            raise RuntimeError("Some nodes do not have a type")
    if len(ndColours) < 1:
        nx.draw_networkx_nodes(G, pos = layout, node_color = colours[0], node_shape = '8', node_size = 100, ax = ax)
    else:
        nx.draw_networkx_nodes(G, pos = layout, node_color = ndColours, node_shape = '8', node_size = 100, ax = ax)
    nx.draw_networkx_edges(G, pos = layout, width = .7, ax = ax)
    if showLabel:
        nx.draw_networkx_labels(G, pos = layout, font_size = 8, ax = ax)
    plt.axis('off')
    f.set_facecolor('w')

def graphDensityContourPlot(G, iters = 50, layout = None, layoutScaleFactor = 1, overlay = False, nodeSize = 10, axisSamples = 100, blurringFactor = .1, contours = 15, graphType = 'coloured'):
    """Creates a 3D plot giving the density of nodes on a 2D plane, as a surface in 3D.

    Most of the options are for tweaking the final appearance. _layout_ and _layoutScaleFactor_ allow a pre-layout graph to be provided. If a layout is not provided the [networkx.spring_layout()](https://networkx.github.io/documentation/latest/reference/generated/networkx.drawing.layout.spring_layout.html) is used after _iters_ iterations. Then, once the graph has been laid out a grid of _axisSamples_ cells by _axisSamples_ cells is overlaid and the number of nodes in each cell is determined, a gaussian blur is then applied with a sigma of _blurringFactor_. This then forms a surface in 3 dimensions, which is then plotted.

    If you find the resultant image looks too banded raise the the _contours_ number to ~50.

    # Parameters

    _G_ : `networkx Graph`

    > The graph to be plotted

    _iters_ : `optional [int]`

    > Default `50`, the number of iterations for the spring layout if _layout_ is not provided.

    _layout_ : `optional [networkx layout dictionary]`

    > Default `None`, if provided will be used as a layout of the graph, the maximum distance from the origin along any axis must also given as _layoutScaleFactor_, which is by default `1`.

    _layoutScaleFactor_ : `optional [double]`

    > Default `1`, The maximum distance from the origin allowed along any axis given by _layout_, i.e. the layout must fit in a square centered at the origin with side lengths 2 * _layoutScaleFactor_

    _overlay_ : `optional [bool]`

    > Default `False`, if `True` the 2D graph will be plotted on the X-Y plane at Z = 0.

    _nodeSize_ : `optional [double]`

    > Default `10`, the size of the nodes dawn in the overlay

    _axisSamples_ : `optional [int]`

    > Default 100, the number of cells used along each axis for sampling. A larger number will mean a lower average density.

    _blurringFactor_ : `optional [double]`

    > Default `0.1`, the sigma value used for smoothing the surface density. The higher this number the smoother the surface.

    _contours_ : `optional [int]`

    > Default 15, the number of different heights drawn. If this number is low the resultant image will look very banded. It is recommended this be raised above `50` if you want your images to look good, **Warning** this will make them much slower to generate and interact with.

    _graphType_ : `optional [str]`

    > Default `'coloured'`, if `'coloured'` the image will have a destiny based colourization applied, the only other option is `'solid'` which removes the colourization.

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
