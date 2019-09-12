# vertexes are people
# edges are friendship connections
# connected components are extended social network (friend groups)
# number of users between one user and another are degrees of seperation
import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # Add users
        if numUsers > avgFriendships:
            
            for i in range(0, numUsers):
                self.addUser(i)

            # Create friendships
            # Tracks previously made friendships
            used_connections = []
            # Counts number of friendships to make
            for i in range (0, int((numUsers*avgFriendships)/2)):
                new_connection = False
                while new_connection == False:
                    # not 0-numUsers, error occurs when adding friend with 0
                    user1 = random.randint(1, numUsers)
                    user2 = random.randint(1, numUsers)
                    user_string = str(user1) + ", " + str(user2)
                    # if 1 < 2 prevents reversed duplication of connection
                    if user1 < user2 and user_string not in used_connections:
                        print("Unique string " +str(i+1) + ": " + user_string)
                        self.addFriendship(user1, user2)
                        used_connections.append(user_string)
                        new_connection = True
            print(used_connections)

    def getAllSocialPaths(self, userID, originalID = None, visited = None):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # !!!! IMPLEMENT ME
        # BFS
        if visited is None:
            visited = {}  # Note that this is a dictionary, not a set
            visited[userID] = [userID]
            originalID = userID
        # Recursively find friendship path connection then return visited path at end
        for friend in self.friendships[userID]:
            if friend not in visited:
                path = self.findShortestPath(originalID, friend)
                print(str(friend) + " path: " + str(path))
                visited[friend] = path
                self.getAllSocialPaths(friend, originalID, visited)
        

        return visited


    def findShortestPath(self, start, goal):
        visited = set()
        q = Queue()
        q.enqueue([start])
        while q.size() > 0:
            path = q.dequeue()
            current = path[-1]
            if current not in visited:
                visited.add(current)
                if current == goal:
                    return path
                for neighbor in self.friendships[current]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)

if __name__ == '__main__':
    sg = SocialGraph()
    print("Starting social graph for 10 users, avg is 2")

    sg.populateGraph(10, 2)
    print("sg.friendships: " + str(sg.friendships))
    connections = sg.getAllSocialPaths(1)
    print("sg.getAllSocialPaths: " + str(connections))
