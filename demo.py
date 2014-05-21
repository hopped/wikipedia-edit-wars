import xml.sax
import wikiparser
import diff_match_patch as meyersdiff
import networkx as nx
import matplotlib.pyplot as plt
import hashlib

__author__ = 'Dennis Hoppe (hoppe.dennis@ymail.com)'


def main():
  parser = xml.sax.make_parser()
  handler = wikiparser.WikiParser()
  parser.setContentHandler(handler)
  parser.parse("wiki.xml")

  diff = meyersdiff.diff_match_patch()

  graph = nx.DiGraph()
  cachedDeletions  = []
  openDeletions    = []
  openInsertions   = []
  cachedInsertions = []
  startingPoints   = []

  revisions = handler.wikiArticle.revisions
  maxLength = len(revisions) - 1
  for revision in range(0,maxLength):
    text1 = revisions[revision].text
    text2 = revisions[revision + 1].text
    deltas = textCompare(text1, text2)
    for delta in deltas:
      graph.add_node(delta)
      if delta[0] == diff.DIFF_DELETE:
        cachedDeletions.append(delta)
        if len(openInsertions) == 0:
          continue;
        simDelta = getMostSimilarDelta(openInsertions, delta[1])
        if simDelta == None:
          continue
        graph.add_edge(delta, simDelta)
        openInsertions.remove(simDelta)
        if simDelta in startingPoints:
          startingPoints.remove(simDelta)
        startingPoints.append(delta)

      elif delta[0] == diff.DIFF_INSERT:
        cachedInsertions.append(delta)
        if len(openDeletions) == 0:
          continue;
        simDelta = getMostSimilarDelta(openDeletions, delta[1])
        if simDelta == None:
          continue
        graph.add_edge(delta, simDelta)
        openDeletions.remove(simDelta)
        if simDelta in startingPoints:
          startingPoints.remove(simDelta)
        startingPoints.append(delta)
      # fi
    # rof
    openInsertions[:0] = cachedInsertions
    openDeletions[:0] = cachedDeletions
    cachedInsertions = []
    cachedDeletions = []
  # rof

  print graph.number_of_nodes()
  print graph.number_of_edges()

  for vertex in startingPoints:
    if (len(nx.shortest_path(graph.reverse(), vertex))):
      print nx.shortest_path(graph.reverse(), vertex)

  #nx.draw(graph) # computational expensive operation
  #plt.show()

def textCompare(text1, text2):
  diff = meyersdiff.diff_match_patch()
  diffs = diff.diff_main(text1, text2, True)
  diff.diff_cleanupSemantic(diffs)
  return diffs

def getMostSimilarDelta(queue, delta):
  for otherDelta in queue:
    a = hashlib.md5(delta.encode("utf-8")).hexdigest()
    b = hashlib.md5(otherDelta[1].encode("utf-8")).hexdigest()
    if a == b:
      return otherDelta

if __name__ == "__main__":
  main()
