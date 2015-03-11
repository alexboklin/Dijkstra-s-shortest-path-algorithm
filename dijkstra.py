import time
import argparse

def main(no_path = 1000000):   

    start = time.process_time()

    parser = argparse.ArgumentParser(description='Calculates shortest paths and distances from the source node.')
    parser.add_argument("-p", help="shortest paths (what nodes to take) to each node from the source", action="store_true")
    parser.add_argument("-d", help="shortest-path distances to each node from the source", action="store_true")
    parser.add_argument("-t", help="execution time", action="store_true")
    parser.add_argument("-i", help="default distance if there is no path between the source node and a given vertex", action="store_true")
    parser.add_argument("filename", help=".txt file to parse")
    args = parser.parse_args()

    with open(args.filename, 'r') as file:    
        data = file.readlines()

    # Extracting graph from the input file.
    # Format: {tail: [(head, edge length), (head, edge length), ... ], ...}
    graph = {i + 1: [tuple(int(k) for k in j.split(',')) for j in data[i].split()[1:]] for i in range(len(data))}

    source = int(input("Source node: "))
    visited = []
    visited.append(source)

    # Default distance if there is no path between the source node and a given vertex
    if args.i:
        no_path = int(input("Distance if there is no path between the source node and a given vertex : "))
    # Initialize a list of shortest-path distances to each node
    distances = [no_path if i != source - 1 else 0 for i in range(len(graph))]

    # Shortest paths (what nodes to take) to each node from the source
    paths = [[] for i in range(len(graph))] 

    while len(visited) < len(distances):

        # Where we can go to from already visited nodes.
        # Format: {tail: [(head, edge length), (head, edge length), ... ], ...}
        destinations = {}   

        for vertex in visited:
            outgoing = []    # keep track of outgoing paths and their lengths
            for pair in graph[vertex]:
                if pair[0] not in visited:
                    outgoing.append(pair)
            if outgoing:
                destinations[vertex] = outgoing

        # Nowhere to go, time to break out
        if not destinations:
            break
    
        # Calculate cumulative scores for all possible destinations to select the shortest path
        # Format: [(tail, head, cumulative distance from the source), ... ]
        scores = []

        for vertex in destinations:
            if vertex in visited:
                for pair in destinations[vertex]:
                    scores.append((vertex, pair[0], distances[vertex - 1] + pair[1]))
            else:
                for pair in destinations[vertex]:
                    scores.append((vertex, pair[0], pair[1]))

        # Find minimal score and what scores tuple contains it
        min_score, min_index = min((minimum, index) for (index, minimum) in enumerate([score[2] for score in scores]))

        # Update the list containing visited nodes
        visited.append(scores[min_index][1])

        # Update the list containing distances to each node from the source
        distances[scores[min_index][1] - 1] = min_score

        # Update the list containing the shortest paths to each node from the source
        paths[scores[min_index][1] - 1].extend(paths[scores[min_index][0] - 1])
        paths[scores[min_index][1] - 1].extend([scores[min_index][1]])

    paths = {i + 1: tuple(paths[i]) for i in range(len(paths))}
    if args.p:
        print("Shortest paths: {}".format(paths))

    distances = {i + 1: distances[i] for i in range(len(distances))}
    if args.d:
        print("Shortest-path distances: {}".format(distances))
    
    end = time.process_time()
    if args.t:
        print("The program ran in {} seconds".format(end - start))

if __name__ == "__main__":
    main()
