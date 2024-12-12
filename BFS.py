# -*- coding: utf-8 -*-
"""task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16j38bDZkyEK7mLfH_yTF-P9IbcCsmwlt
"""

import threading
import queue #inporting

inp = open('/content/input2.txt',"r")
out = open('/content/output2.txt',"w")

x,y = list(map(int,inp.readline().split()))
adjL = [[] for i in range(x+1)] #creating adj list

for i in range(y):
  a,b = list(map(int,inp.readline().split()))
  adjL[a].append(b) #inputing all nodes into adj list
  adjL[b].append(a)

def BFS(G,S): #G = adhL and S = 1 , 1 is our fisrt vertex
  vertex = [0] * (x+1)
  Q = queue.Queue()
  vertex[S] = 1 #initializing the 1st vertex as visited
  Q.put(S) #enqueue first index
  out.write(f"{S}") #1st vertex is visited and printed
  while Q.qsize() != 0: #size compare of queue
    u = Q.get() #get function does the work of deqeue as well
    for i in G[u]:
      if vertex[i] ==0:
        vertex[i] = 1
        out.write(f" {i}") #now we visited i vertex and print
        Q.put(i) #enqueing new vertex

BFS(adjL,1) # calling the BFS

inp.close()
out.close()
