#!/usr/bin/python3

import shasta
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--segmentId', type=int, required=True)
arguments = parser.parse_args()

a = shasta.Assembler()
a.accessMarkers()
a.accessReadGraph()
a.accessMarkerGraphVertices()
a.accessMarkerGraphEdges()
a.accessAssemblyGraphVertices()
a.accessAssemblyGraphEdges()
a.accessAssemblyGraphEdgeLists()
a.accessAssemblyGraphSequences()
a.analyzeOrientedReadPathsThroughSegment(arguments.segmentId)

	





