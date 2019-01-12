# Python implementation of Kosaraju's algorithm to print all SCCs 
   
#This class represents a directed graph using adjacency list representation 
class Graph_SCC: 
   
    def __init__(self,dic): 
        self.V= len(dic.keys()) #No. of vertices 
        self.graph = dict(dic) # default dictionary to store graph 

    # function to add an edge to graph 
    def addEdge(self,u,v):
        l = self.graph.get(u,-1)
        if l == -1:
            self.graph[u]=[v]
        else:
            self.graph[u].append(v) 
   
    # A function used by DFS 
    def DFSUtil(self,v,visited,scc): 
        # Mark the current node as visited and print it 
        visited[v]= True
        scc.append(v)
        # print v, 
        #Recur for all the vertices adjacent to this vertex 
        if self.graph.get(v,-1)!=-1:
            for i in self.graph[v]: 
                if visited.get(i,False)==False: 
                    self.DFSUtil(i,visited,scc) 
        
  
    def fillOrder(self,v,visited, stack):
        # Mark the current node as visited  
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]:

            if visited.get(i,False)==False: 
                self.fillOrder(i, visited, stack)

        stack = stack.append(v) 
      
  
    # Function that returns reverse (or transpose) of this graph 
    def getTranspose(self): 
        g = Graph_SCC({}) 
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph:
            target_blocks = self.graph[i]
            for j in self.graph[i]: 
                g.addEdge(j,i) 
        return g 
  
   
   
    # The main function that finds and prints all strongly 
    # connected components 
    def getSCCs(self): 
          
        stack = []
        SCCs = []
        # Mark all the vertices as not visited (For first DFS) 
        visited = {} 
        # Fill vertices in stack according to their finishing 
        # times
        for i in self.graph:
            if visited.get(i,False) == False:
                self.fillOrder(i, visited, stack) 
  
        # Create a reversed graph 
        gr = self.getTranspose() 

        # print "O"
        # print self.graph
        # print len(self.graph.keys())
        # print "T"
        # print gr.graph
        # print len(gr.graph.keys())
        # print "S"
        # print stack
        # print len(stack)
        # Mark all the vertices as not visited (For second DFS) 
        visited ={} 
  
        # Now process all vertices in order defined by Stack 
        while stack: 
            i = stack.pop()
            scc = []
            if visited.get(i,False)==False:
                
                gr.DFSUtil(i, visited,scc)
                SCCs.append(scc)
        return SCCs

    def printSCCs(self):
        sccs = self.getSCCs()
        print sccs
    
