from math import*
from scipy import spatial

dataSetI = [3,45,7,2]
dataSetII = [2,54,13,15]
dataSetIII = [7,2,1,3]


#To get cosine similarity, subtract the distance from 1
result = 1 - spatial.distance.cosine(dataSetI, dataSetII)
result2 = 1 - spatial.distance.cosine(dataSetI, dataSetIII)
result3 = 1 - spatial.distance.cosine(dataSetII, dataSetIII)


print result,result2,result3