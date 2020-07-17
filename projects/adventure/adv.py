from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)



# Fill this out with directions to walk
traversal_path = []

# Used when current room already visited to go back to previous room
opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

def traverse(room, seen=None):

    # create a set when the function is called the first time
    if seen is None:

        seen = set()

    path = []
    room = player.current_room

    # Iterate over possible directions
    for direction in room.get_exits():

        player.travel(direction)
        room = player.current_room

        # If the room was seen, turn around = take the opposite of the direction 
        # that was travelled
        if room in seen:

            player.travel(opposite[direction])

        # Otherwise, add room to seen and direction to path
        else:

            seen.add(room)
            path.append(direction)

            # Recursively call function again on this room and add to path
            path = path + traverse(room, seen)
            player.travel(opposite[direction])
            path.append(opposite[direction])

    return path



traversal_path = traverse(player.current_room)

print(traversal_path)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
