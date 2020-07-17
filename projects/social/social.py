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
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        
        # sanity checks
        if avg_friendships >= num_users:

            print("num_users has to be bigger than avg_friendships")

            return

        if avg_friendships == 1:

            if num_users%2 == 1:

                print("""input cannot be processed. If avg friendships is one, 
                num_users must be a multiple of 2.""")

                return
 
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users

        for user in range(num_users):

            self.add_user("Hans")

        total_friendships = (num_users*avg_friendships)//2


        while total_friendships > 0:

            user = random.randint(1,self.last_id)

            friend = random.randint(1,self.last_id)

            if user == friend:

                continue

            if friend in self.friendships[user]:

                continue

            if len(self.friendships[user]) >= avg_friendships*2:

                continue

            self.add_friendship(user, friend)

            total_friendships -= 1


        # Create friendships

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        

        q = Queue()

        q.enqueue([user_id])

        while q.size() > 0:
        
            path = q.dequeue()

            visited[path[-1]] = path

            for friend in self.friendships[path[-1]]:

                if friend not in visited:

                    q.enqueue(path + [friend])

        return visited

        # find shortest paths


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
