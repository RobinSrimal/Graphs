from collections import defaultdict, deque

def earliest_ancestor(ancestors, starting_node):
    
    # mapping children to their parents
    graph = defaultdict(lambda:set())

    for relation in ancestors:

        graph[relation[1]].add(relation[0])

    # if starting_node has no parents return -1
    if not graph[starting_node]:

        return -1

    switch = True

    ancestors = [starting_node]

    while switch:

        switch = False

        temp = []

        for node in ancestors:

            if graph[node]:

                switch = True

                for parent in graph[node]:

                    temp.append(parent)

        if temp:

            paths = temp

    return min(ancestors)



    

    


    