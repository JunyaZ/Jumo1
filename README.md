# KNN classification
implement the KNN algorithm. used weighted voting in the implementation. In simple unweighted voting, once the k nearest neighbors are found, their distances from the test sample do not matter. One neighbor is one vote. In weighted voting, the vote of a neighbor is inversely proportional to its distance to the test sample. 

Use the given MNIST_train.cvs as the training data set and MNIST_test.csv as the test data set. There are 10 classes, with labels 0, 1, 2, …, 9, for this data set. The first attribute/column is the class label.

The output from your program will display the following:
value of K 
for each test sample, print both the desired class and the computed class
the accuracy rate
number of misclassified test samples
total number of test samples 
