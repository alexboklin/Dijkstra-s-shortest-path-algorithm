This is a straightforward O(mn) time implementation of Dijkstra's algorithm for undirected weighted graphs, a Python script supporting command-line arguments.

The input text file should contain an adjacency list representation of the graph. Each row should consist of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.

Default distance if there is no path between the source node and a given vertex is set as 1000000 (it can be changed).
