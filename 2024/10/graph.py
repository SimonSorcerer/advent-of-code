GOAL_VERTEX_HEIGHT = 9

class DirectedGraph:
   def __init__(self):
      """
      Initializes a directed graph.

      Attributes:
      - graph_dict: A dictionary to store the adjacency list representation of the graph.
      """
      self.graph_dict = {}

   def add_vertex(self, vertex):
      """
      Adds a vertex to the graph if it doesn't already exist.

      Parameters:
      - vertex: The label of the vertex to be added.
      """
      if vertex not in self.graph_dict:
         self.graph_dict[vertex] = []

   def add_edge(self, from_vertex, to_vertex):
      """
      Adds a directed edge from one vertex to another in the graph.

      Parameters:
      - from_vertex: The label of the source vertex.
      - to_vertex: The label of the destination vertex.
      """
      self.graph_dict[from_vertex].append(to_vertex)

   def has_vertex(self, vertex):
      """
      Checks if a vertex is in the graph.

      Parameters:
      - vertex: The vertex to be checked.

      Returns:
      - True if the vertex is in the graph, False otherwise.
      """
      return vertex in self.graph_dict
   
   def traverse(self, start_vertex):
      """
      Traverses the graph in depth-first order starting from a given vertex.

      Parameters:
      - start_vertex: The vertex to start the traversal from.

      Returns:
      - A list of vertices in the order they were visited.
      """
      visited = []
      stack = [start_vertex]

      while stack:
         current_vertex = stack.pop()
         if current_vertex not in visited:
            visited.append(current_vertex)
            stack.extend(self.graph_dict[current_vertex])

      return visited

   def find_all_paths(self, start_vertex):
      """
      Finds all paths between two vertices in the graph.

      Parameters:
      - start_vertex: The vertex to start the search from.
      - goal_vertex: The vertex to search for.

      Returns:
      - A list of paths between the two vertices.
      """
      return self.depth_first_search([start_vertex], [])

   def depth_first_search(self, path, paths):
      """
      Performs a depth-first search on the graph starting from a given vertex.

      Parameters:
      - start_vertex: The vertex to start the search from.
      - goal_vertex: The vertex to search for.

      Returns:
      - A list of vertices in the order they were visited.
      """
      current_vertex = path[-1]
      neighbors = self.graph_dict[current_vertex]

      if len(neighbors) > 0:
         for neighbor in neighbors:
            paths = self.depth_first_search(path + [neighbor], paths)
      elif current_vertex[1] == GOAL_VERTEX_HEIGHT:
         paths.append(path)
      return paths

   def print_graph(self):
      """
      Prints the adjacency list representation of the directed graph.
      """
      for vertex in self.graph_dict:
         destinations = self.graph_dict[vertex]
         print(f"{vertex} --> {destinations}")