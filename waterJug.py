from collections import deque
 
def BFS(x, y, aim):
    map = {}
    isSolvable = False
    path = []
     
   
    q = deque()
     
    q.append((0, 0))
 # q lenth
    while (len(q) > 0):
         
       
        jug = q.popleft()

        if ((jug[0], jug[1]) in map):
            continue
 
      #checkt the jug constraints
        if ((jug[0] > x or jug[1] > y or
             jug[0] < 0 or jug[1] < 0)):
            continue
 
        path.append([jug[0], jug[1]])
 
        # Marking current state as visited
        map[(jug[0], jug[1])] = 1
 
        # If we reach aim , put ans=1
        if (jug[0] == aim or jug[1] == aim):
            isSolvable = True
             
            if (jug[0] == aim):
                if (jug[1] != 0):
                     
                    # Fill final state
                    path.append([jug[0], 0])
            else:
                if (jug[0] != 0):
 
                    # Fill final state
                    path.append([0, jug[1]])
 
            # Print the solution path
            sz = len(path)
            for i in range(sz):
                print("(", path[i][0], ",",
                           path[i][1], ")")
            break
 
        #If we haven't yet arrived at the final state, we can begin creating intermediate states in order to arrive at the solution state.
        q.append([jug[0], y]) # Fill jug2
        q.append([x, jug[1]]) # Fill jug1
 
        for z in range(max(x, y) + 1):
 
            # Pour amount z from jug2 to jug1
            c = jug[0] + z
            d = jug[1] - z
 
            #Check if this condition is feasible.
            if (c == x or (d == 0 and d >= 0)):
                q.append([c, d])
 
            # Pour amount z from jug 1 to jug2
            c = jug[0] - z
            d = jug[1] + z
 
            # Check if this condition is feasible.
            if ((c == 0 and c >= 0) or d == y):
                q.append([c, d])
         
        # Empty Jug2
        q.append([x, 0])
         
        # Empty Jug1
        q.append([0, y])
 
 
# run code
if __name__ == '__main__':
     
    jug1, jug2, aim = 4, 3, 2
    print("Data set")
     
    BFS(jug1, jug2, aim)