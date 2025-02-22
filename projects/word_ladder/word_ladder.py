# Given two words (beginWord and endWord), and a dictionary's word list, return the 
# shortest transformation sequence from beginWord to endWord, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a 
# transformed word.

# Note:
# Return None if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.


# Breakdown
# Shortest - BFS
# One letter at a time - edges
# Word list/words - Vertexes
# Return none - path not found
# BeginWord and EndWord - Starting and ending vertices
# No duplicates
# Same length - don't ahve to do anything with different length words
# ^^ Connected componets
# Transofrmation sequence - path


# If we organize the word list in a graph
# with words as vertexes and edges between
# two words that are 1 letter different,
# then
# if we do a BFS from BeginWord to EndWord
# the resulting path will be
# transformation sequence

from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("ERROR: Vertex does not exist")

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        
        q = Queue()
        visited = set()
        q.enqueue([starting_vertex])
        
        while q.size() > 0:
            path = q.dequeue()
            current = path[-1]
            if current not in visited:
                print("BFS searching -> " + str(current))
                if current is destination_vertex:
                    return "BFS: " + str(path)
                visited.add(current)
                for next_vert in self.vertices[current]:
                    new_path = list(path) #path is a reference type so need to copy
                    new_path.append(next_vert)
                    q.enqueue(new_path)

        print("BFS: Path does not exist")
        return None


    def nearly_equal(self, string1, string2):
        count_diffs = 0
        for a, b in zip(string1, string2):
            if a!=b:
                if count_diffs: return False
                count_diffs += 1
        return True

    def make_edges(self):
        print("make edges")

        for word in self.vertices:
            for second_word in self.vertices:
                if self.nearly_equal(word, second_word) and word is not second_word:
                    self.add_edge(word, second_word)
        
        # for word in self.vertices:
        #     print(str(word) + " " + str(self.vertices[word]))
        
    def find_transformation(self, first_word, last_word):
        print(first_word, last_word)

if __name__ == '__main__':
    graph = Graph()

        # Add all words as a vertex inside our graph
    # text = open("/Users/angelbuenrostro/Python/Graphs/projects/word_ladder/words.txt", "r")
    # for word in text:
    #     if len(word) is 5 and word.islower():
    #         word_no_whitespace = word.split()
    #         graph.add_vertex(word_no_whitespace[0])
    # print("Number of vertices in word graph: "+ str(len(graph.vertices)))
    graph.add_vertex("box")
    graph.add_vertex("bot")
    graph.add_vertex("tot")
    graph.add_vertex("tat")
    graph.add_vertex("bat")
    graph.add_vertex("tab")
    graph.add_vertex("tap")
    graph.add_vertex("bar")
    graph.add_vertex("tax")
    graph.add_vertex("tex")
    graph.add_vertex("rex")
    graph.add_vertex("rep")
    graph.add_vertex("rap")
    graph.add_vertex("zap")

    graph.make_edges()

    for val in graph.vertices:
        print(val, graph.vertices[val])
    
    start = 'box'
    end = 'bat'


    # should print BOX -> BOT -> BAT
    print("Path for box to bat is: " + str(graph.bfs(start, end)))

    start = "box"
    end = "zap"
    print("Path for box to zap: " + str(graph.bfs(start, end)))