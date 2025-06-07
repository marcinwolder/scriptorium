from antlr4 import *
from antlr4.tree.Trees import Trees
import pydot
from antlr4.tree.Tree import TerminalNodeImpl

def tree_to_dot(tree, parser, outfile="tree.dot", to_png=False):
    """Export ANTLR parse tree to Graphviz .dot (and optionally .png)."""
    nodes, edges = [], []

    def walk(node, counter=[0]):
        my_id = counter[0]
        counter[0] += 1

        label = Trees.getNodeText(node, parser.ruleNames)
        nodes.append((my_id, label.replace('"', r'\"')))   # escape quotes

        if type(node) != TerminalNodeImpl:
            for child in node.getChildren():
                child_id = walk(child, counter)
                edges.append((my_id, child_id))
        return my_id

    walk(tree)

    g = pydot.Dot(graph_type="digraph", rankdir="TB")
    for node_id, label in nodes:
        g.add_node(pydot.Node(str(node_id), label=label, shape="box"))
    for src, dst in edges:
        g.add_edge(pydot.Edge(str(src), str(dst)))

    g.write(outfile)
    if to_png:
        g.write_png(outfile.replace(".dot", ".png"))