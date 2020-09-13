#!/usr/bin/env python3

import sys
                    
def sort(path):
    print ("path before sort:",path)
    for j in range(1,len(path)):
        key = path[j][2]
        key_list = path[j]
        i = j-1
        while(i >= 0 and path[i][2]>key):
            path[i+1] = path[i]
            i = i-1
        path[i+1] = key_list
     
    print ("path After sort:",path, "\n")
    return path
    

def path_finder(file,origin_city, destination_city):    #input.txt, K, B
    flag = 1
    path = []
    closed = []
    closed_nodes = []
    path.append(["",origin_city,int(0)])    #["", "K", 0]
    end = "END OF INPUT"
    
    while(flag):
        fopen = open(file,"r")

        if(path == []):   #No path: No Origin
            return []
        
        temp = path.pop(0) #Select the first City in path #["", "K", 0] #["K", "A", 7]
        
        #Check if Destination is reached
        if temp[1] == destination_city:  
            flag = 0    #Stop loop after this iteration
            
        if temp[1] not in closed:
            closed.append(temp[1])      #["K", "A"]
            closed_nodes.append(temp)   #[["", "K", 0], ["K", "A", 0]]
            count = 0
            
            #Find all adjacent cities and create possible paths
            for i in fopen:             #For every line
                if end in i:
                    break
                if temp[1] in i:        #If K is in this line
                    count = count + 1   #Increase neighbor count
                    i = i.split()
                    if temp[1] == i[0]:
                        i[2] = int(i[2]) + int(temp[2])
                        path.append(i)
                    elif temp[1] == i[1]:
                        switch = i[0]
                        i[0] = i[1]
                        i[1] = switch
                        
                        i[2] = int(i[2]) + int(temp[2]) #Edit this node's cost to be the total cost
                        path.append(i)
                        
            if count == 0 and path == []:
                return []   #No route
            
            path = sort(path)
                        
        fopen.close()    

    return closed_nodes
                
def backtracking(closed_nodes,destination_city):
   
    if closed_nodes == []: 
        print ("Distance: Infinite")
        print ("Route:\nNone")
        return
    
    closed_nodes = closed_nodes[::-1]
    route = []
#     print closed_nodes
#     flag = 1
#     while(flag):
    if closed_nodes[0][1] != destination_city:
        return
    temp = closed_nodes[0]
    route.append(temp)
    for node in closed_nodes:
        if temp[0] in node[1]:
            temp = node
            route.append(temp)
#     print 'Route: \n', route
    
    print ("\nDistance:", route[0][2],"km")
    print ("\nRoute:")
    prev_value = 0
    route = route[::-1]
    for node in range(1,len(route)):
        print (route[node][0], "to", route[node][1],",", route[node][2] - prev_value,"km")
        prev_value = route[node][2]
    

# ENTRYPOINT
f = sys.argv[1]
origin_city = sys.argv[2]
destination_city = sys.argv[3]
    
try:
    fopen = open(f,"r")
    flag = 1
except:
    print ("Invalid File Name")
    flag = 0

if flag == 1:
    print (f, origin_city, destination_city)
    
    closed_nodes = path_finder(f, origin_city, destination_city)
    
    backtracking(closed_nodes,destination_city)
