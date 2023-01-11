# # write a python program for the rabin karp algorithm

# q = 17
# text_list  = [2,3,7,0,4,3,3,2,6,8,7,3,5,6]

# pattern_list = [8,7,3,5]


# text_length = len(text_list)

# pattern_length = len(pattern_list)

# mod_list = []

# for i in range(0,text_length-pattern_length+1):
#     mod_list.append(text_list[i:i+pattern_length])

# print(mod_list)

# # find the mod of the pattern list

# # if pattern_list = [8,7,3,5]  then   pattern_sum = 8735
# def mod_of_list(pattern_list):

#     pattern_length = len(pattern_list)
#     pattern_sum = 0
#     for i in range(0,pattern_length):
#         pattern_sum = pattern_sum + pattern_list[i]*(10**(pattern_length-i-1))


#     # find the mod of pattern_sum with q
#     print(pattern_sum%q)

# mod_of_list(pattern_list)


# # for mod in mod_list:
# #     mod_of_list(mod)
# class InterviewBit:
#     V = 4;

#     def isSafeToColor(v, graphMatrix, color, c):
#         for i in range(V):
#             if graphMatrix[v][i] == 1 and c == color[i]:
#                 return False;
#         return True;

#     def graphColorUtil(graphMatrix, m, color, v):

#         if v == V:
#             return True;

#         for i in range(1, m + 1):
#             if isSafeToColor(v, graphMatrix, color, i):
#                 color[v] =i;
#                 if graphColorUtil(graphMatrix, m, color, v + 1):
#                     return True;
#                 color[v] = 0;

#         return false;

#     def printColoringSolution(color):
#         print("Color schema for vertices are: ")
#         for i in range(V):
#             print(color[i])
#     def graphColoring(graphMatrix, m):

#         color = [0]*(V)

#         if !graphColorUtil(graphMatrix, m, color, 0):
#             print("Color schema not possible")
#             return False;

#         printColoringSolution(color);
#         return True;

#    1.  Apply Graph coloring for using 3 colors for the graph using the algorithm. Also write the algorithm for Graph coloring


# graph have 5 vertices A B C D E and 7 edges

# A-B
# A-C
# B-D
# C-D
# D-E
# B-E
# A-E

graph_matrix = [
    [0,1,1,0,1],
    [1,0,0,1,1],
    [1,0,0,1,0],
    [0,1,1,0,1],
    [1,1,0,1,0]

]

color_list = ['red','green','blue']

def isSafeToColor(v, graphMatrix, color, c):
    for i in range(5):
        if graphMatrix[v][i] == 1 and c == color[i]:
            return False
    return True

def graphColorUtil(graphMatrix, m, color, v):

        if v == 5:
            return True

        for i in range(1, m + 1):
            if isSafeToColor(v, graphMatrix, color, i):
                color[v] =i
                if graphColorUtil(graphMatrix, m, color, v + 1):
                    return True
                color[v] = 0

        return False


def printColoringSolution(color):
    print("Color schema for vertices are: ")
    for i in range(5):
        print(color[i])

def graphColoring(graphMatrix, m):

        color = [0]*(5)

        if not graphColorUtil(graphMatrix, m, color, 0):
            print("Color schema not possible")
            return False

        printColoringSolution(color)
        return True


# we need to find all the possible color schema for the graph

graphColoring(graph_matrix,3)
