"""
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands =
[[0, 1, 0, 1, 0],
[1, 1, 0, 1, 1],
[0, 0, 1, 0, 0],
[1, 0, 1, 0, 0],
[1, 1, 0, 0, 0]]
island_counter(islands) # returns 4

"""

# Vocab map
# island - 1s nodes
# nsew neighbors - edges
# binary array - this is the graph
# groups/connected/islands - connected components

# if we think of the matrix as a graph
# we can loop through it
# do a breadth first search on each 1
# mark all 1s we've found
# and skip 1s that have been visited
# and count how many times we do this
# the result will be the number of connected components/islands


