from math import*
from scipy import spatial
import sql

test_data = [30,900,8.1,15.5,.524,6.1,10.9,.563,2.0,4.6,.433,6.8,9.1,.755,11.8,3.2,2.8,2.7,25.1] #danny granger's last season
test_data2 = [32,868,3.5,8.1,.426,2.2,4.5,.485,1.3,3.6,.354,1.1,2.1,.533,4.4,6.7,2.1,0.2,9.3]


def Similarity(prospect, comparison):
    sim_score = 1 - spatial.distance.cosine(prospect, comparison[6:])
    return sim_score

def main():
    score_list = []
    for data in sql.read_from_db(): #creating a list of similarity scores with input test_data
        score_list.append(Similarity(test_data2, data))
        sorted_score_list = sorted(score_list)
    print sorted_score_list[::-1] #possible scope issue here & sliced to return the reverse of the sorted list
                                  #so that the highest similarity scores appear first
    #interpret_results(sorted_score_list[::-1], data, test_data2)


    sql.c.close()
    sql.conn.close()

def interpret_results(sorted_score_list, data, test_data):
    print "sorted score list: ", sorted_score_list
    print "data: ", data
    print "test data: ", test_data
    return None

main()

#want to return a list of the top results along with what season/player the result came from