#include <iostream>
#include <map>

using std::cout;
using std::endl;
using std::map;


class Node {
  public:
    Node();
  private:
    map<Node*, bool> edges_map;
    vector <Node*> edges;
    bool
}

class Edges {
  public:
    Edges(int id);
    void addEdgeTo(int node);
  private:
    map<int, bool> connected_to;
    vector
    bool node_exists;
    int m_id;
}

Edges::Edges(int id) :node_exists(true) {}

void Edges::addEdgeTo(int node) {
  connected_to[node] = true;
}

class Graph {
  public:
    Graph();
    void addNode();
    void addEdge(int node1, int node2);
    int get_last();
  private:
    map<int, Edges> graph;
    int last_node;
};

Graph::Graph() :last_node(-1) {
}

void Graph::addNode() {
  graph[++last_node] = new Edges();
}

void Graph::addEdge(int node1, int node2) {
  graph[node1].connected_to[node2] = true;
  graph[node2].connected_to[node1] = true;
}

int Graph::get_last() {
  return last_node;
}

