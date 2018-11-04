from graph_tool.all import *

class Grafo(object):

	def __init__(self):
		self.g = Graph()

	def mountGraph(self, filename):
		nodeListOut = []
		nodeListIn = []
		with open(filename, 'r') as dataSet:
			for line in dataSet.readlines():
				self.g.add_vertex()
				nodeListOut.append(str(line.split(" ")[0]))
				nodeListIn.append(str(line.split(" ")[1]))
		#self.g.add_vertex(1 + max([max(nodeListOut),max(nodeListIn)]))
		for node in zip(nodeListOut, nodeListIn):
			self.g.add_edge(self.g.vertex(node[0]),self.g.vertex(node[1]))
		return self.g

	def setProperties(self, mountedGraph, filename):
		v_notas = mountedGraph.new_vertex_property("float")
		with open(filename, 'r') as propSet:
			for (propSetLine, vertice) in zip(propSet.readlines(), mountedGraph.vertices()):
				v_notas[vertice] = propSetLine.split(" ")[1] 
		mountedGraph.vertex_properties["age"] = v_notas
		return mountedGraph.properties
	

