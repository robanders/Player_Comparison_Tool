from math import*
from scipy import spatial
import sql

dataSetI = [3,45,7,2]
dataSetII = [2,54,13,15]
dataSetIII = [7,2,1,3]

test_data = [30,900,8.1,15.5,.524,6.1,10.9,.563,2.0,4.6,.433,6.8,9.1,.755,11.8,3.2,2.8,2.7,25.1] #danny granger's last season
test_data2 = [32,868,3.5,8.1,.426,2.2,4.5,.485,1.3,3.6,.354,1.1,2.1,.533,4.4,6.7,2.1,0.2,9.3]


#To get cosine similarity, subtract the distance from 1
result = 1 - spatial.distance.cosine(dataSetI, dataSetII)
result2 = 1 - spatial.distance.cosine(dataSetI, dataSetIII)
result3 = 1 - spatial.distance.cosine(dataSetII, dataSetIII)

def Similarity(prospect, comparison):
    score_list = []
    sim_score = 1 - spatial.distance.cosine(prospect, comparison)
    return sim_score

def main():
    score_list = []
    for data in sql.read_from_db(): #creating a list of similarity scores with input test_data
        score_list.append(Similarity(test_data, data[6:]))
        sorted_score_list = sorted(score_list)
    print sorted_score_list[::-1] #possible scope issue here & sliced to return the reverse of the sorted list
                                  #so that the highest similarity scores appear first

    sql.c.close()
    sql.conn.close()


main()
