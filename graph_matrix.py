# -*- coding: utf-8 -*-
"""task1a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wv3TjoIFfr8uPjO-GkAfHX3-EIqD_Aq8
"""

inp = open('/content/input1a.txt',"r")
out = open('/content/output1a.txt',"w")

x,y = list(map(int,inp.readline().split()))

adjM = []
for i in range(x+1):
  adjM.append([0]*(x+1))


for i in range(y):
  a,b,c = list(map(int,inp.readline().split()))
  adjM[a][b] = c


for i in range(x+1):
  for j in range(x+1):
    out.write(f"{adjM[i][j]} ")
  out.write(f"\n")

inp.close()
out.close()

