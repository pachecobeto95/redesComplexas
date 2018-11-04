from grafo import Grafo

g = Grafo()
mountedGraph = g.mountGraph('./networks/test.txt')
properties = g.setProperties(mountedGraph, './networks/notas.txt')