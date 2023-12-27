import sys
import os
import numpy as np
import operator

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

def makevector(filename) :
	data = np.zeros((1, 1024))
	f = open(filename)
	for i in range(32):
		line = f.readline()
		for j in range(32):
			data[0, 32 * i + j] = int(line[j])
	return data

def trainingNumber(folder):
    file_list = os.listdir(folder)
    group = np.zeros((len(file_list), 1024))
    labels = []
    i = 0
    for file_name in file_list:
        file_path = os.path.join(folder, file_name)
        training_number = file_name.split("_")[0]
        labels.append(training_number)
        data = makevector(file_path)
        group[i, :] = data
        i += 1
        
    return group, labels

def predictNumber(folder, training_data, training_labels, k):
    error = 0

    file_list = os.listdir(folder)
    for file_name in file_list:
        answer = file_name.split("_")[0]
        file_path = os.path.join(folder, file_name)
        data = makevector(file_path)
        p = classify0(data, training_data, training_labels, k)
        if p != answer:
            error += 1
    rate = error / len(file_list) * 100
    rate = int(rate)
    print(rate)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <training_folder> <data_folder>")
        sys.exit(1)

    training_folder = sys.argv[1]
    data_folder = sys.argv[2]

    group, labels = trainingNumber(training_folder)
    for i in range(1, 21) :
        predictNumber(data_folder, group, labels, i)
