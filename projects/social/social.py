# vertexes are people
# edges are friendship connections
# connected components are extended social network (friend groups)
# number of users between one user and another are degrees of seperation
import random

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
            
            friend_list = []
            for i in range(0, numUsers):
                friend_list.append(i)
                self.addUser(i)

            # Create friendships
            used_connections = []
            for i in range (0, int((numUsers*avgFriendships)/2)):
                found_random = False
                while found_random == False:
                    user1 = random.randint(1, numUsers)
                    user2 = random.randint(1, numUsers)
                    user_string = str(user1) + ", " + str(user2)
                    if user1 < user2 and user_string not in used_connections:
                        print("Unique string " +str(i+1) + ": " + user_string)
                        self.addFriendship(user1, user2)
                        used_connections.append(user_string)
                        found_random = True
            print(used_connections)




    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    print("Starting social graph for 10 users, avg is 2")
    # sg.addUser(0)
    # sg.addUser(1)
    # sg.addUser(2)
    # sg.addUser('angel')
    # sg.addFriendship(1,2)

    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
