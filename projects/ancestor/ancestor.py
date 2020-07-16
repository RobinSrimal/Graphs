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

    # define starting point for while loop
    ancestors = [starting_node]

    while switch:

        switch = False

        temp = []

        # go through the list of current oldest ancestors
        for node in ancestors:

            # if an ancestor has parents    
            if graph[node]:

                # add those parents to temp    
                for parent in graph[node]:

                    temp.append(parent)
        
        # if temp is not empty we found an older generation of ancestors
        if temp:

            # therefore the while loop has to run another time 
            switch = True
            ancestors = temp
    
    # once the while loop is done return the minimum value of the oldest 
    # genration of ancestors that was found
    return min(ancestors)



    

    


    