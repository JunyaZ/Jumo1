##########################################################################  
# Program :        _K Nearest Neighbors  (KNN)
# Programmed By:   Junya Zhao
# Input:
#             trainData: training dataset
#             k:number of neighbors
#             testData :new input tuple to classfiy
#             
# Output:     class to which t is assigned
#
# display :   value of K;
#             both the desired class and the computed class for each sample
#             desired class is the class label as given in the data set
#             computed class is what produces as the output for the sample
#	      the accuracy rate
#             number of misclassified test samples,
#             total number of test samples
#Trace folder: \\trace\Class\CSC-535-635\001\Junya009\hw2
############################################################################  

#---------------------------------Imports--------------------------------------      
import csv
import math
from random import shuffle
from operator import itemgetter
#---------------------------------Functions------------------------------------

#get the dataset
def GetDataset(filename, isTestData = True):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)# get a list of all values
    del(data[0]) # delete the header
    data = [list(map(int, d)) for d in data]
    if not isTestData:
        shuffle(data) #shuffle the data, in order to get the different order of samples
        #to make sure the neighbors does not always have same label
    return data
    print(data)
#Calculates the distance between samples
def Distance(testData, trainingData):
    distance= 0
    for i in range(len(testData)):
        distance += math.pow(testData[i] - trainingData[i],2)
    return math.sqrt(distance)

#get the accuracy of the result
def accuracy(TestData, outputset):
    rightLabel= 0
    WrongLabel = 0
    for i in range(len(TestData)):
        if TestData[i][0] == outputset[i]:
            rightLabel +=1
        else:
            WrongLabel +=1
    return [(rightLabel/len(outputset)*100), WrongLabel]

#get the weights for closest neighbors
def CalVotes(data):
    for i in data:
        vote = 1/i[1]
        i.append(vote)
    data.sort(key=itemgetter(2))
    return data[0][0]

# KNN Algorithm'''
def KNNclassify(testData, trainingData, k) :
    Outputdata= list()
    for newIN in testData:
        distance = list()
        for train in trainingData:
            distance.append([train[0], Distance(newIN[1:], train[1:])])
        distance.sort(key=itemgetter(1))
        neighbors = [distance[i] for i in range(k)]
        result = CalVotes(neighbors)
        Outputdata.append(result)
        
        print('Desired Class = ', newIN[0], "Computed Class = ", result)
    accuracy_result = accuracy(testData, Outputdata)
    print ('Accuracy Rate = ', accuracy_result[0])
    print('Number of mis-classified test samples = ', accuracy_result[1])
    print('Total number of test samples = ', len(testData))
#------------------------------------------------------------------------------

#---------------------------------Program Main---------------------------------

if __name__ == '__main__':
    Traing = 'MNIST_train.csv'
    TestDataSet = 'MNIST_test.csv'
    trainingData = GetDataset(Traing, False)
    testingData = GetDataset(TestDataSet)
    #for k in range(1,20):
        #print('\n\nK = ', k)
    KNNclassify(testingData,trainingData, 4)
#---------------------------------End of Program-------------------------------
