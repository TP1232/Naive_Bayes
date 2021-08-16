import time
import numpy as np
import random 
m = 100

X = np.random.rand(m,m)
Y = np.random.rand(m,m)
 
def mult(X, Y):
   result = [[0]*m]
   for z in range(len(Y[0])):
       for k in range(len(Y)):
           result[0][z] += X[0] * Y[k][z]

start = time.perf_counter()
for i in range(len(X[0])):
   mult(X[i], Y)
end = time.perf_counter()
 
print("Time without parallel prcessing", end - start)

import threading
import time
 

X = [[1]*m]*m
Y = [[1]*m]*m
 
def mult(X, Y):
   result = [[0]*m]
   for z in range(len(Y[0])):
       for k in range(len(Y)):
           result[0][z] += X[0] * Y[k][z]
   # print(f" {result}")
 
threads = list()
start = time.perf_counter()
for i in range(len(X[0])):
   x = threading.Thread(target = mult, args=(X[i], Y))
   threads.append(x)
   x.start()
 
for index, thread in enumerate(threads):
   thread.join()
end = time.perf_counter()
 
print("Time with threading", end - start)
 