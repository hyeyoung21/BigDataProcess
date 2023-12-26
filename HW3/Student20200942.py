import sys
import os
import numpy as np
import operator

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0] #dataSet의 갯수 세기
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort() #간접정렬 숫자가 작은 순으로 인덱스값 리턴 
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]] #작은 순서대로 라벨 값 얻음
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1 #라벨 갯수 하나씩 더함
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0] #더 많은 값 리턴(라벨) 많은 순서대로 리턴했으니까

def trainingNumber(folder):
    file_list = os.listdir(folder)
    group = []
    labels = []
    for file_name in file_list:
        file_path = os.path.join(folder, file_name)
        training_number = file_name.split("_")[0] 
        labels.append(training_number) #무슨 숫자 training 했는지
        with open(file_path, 'r') as f:
            data = f.read() #데이터 읽기
            data_list = [float(num) for num in data.split()]
            group.append(data_list)

    return np.array(group), labels

def predictNumber(folder, training_data, training_labels, k) :
    error = 0
    entire = 0

    file_list = os.listdir(folder)
    for file_name in file_list:
        answer = file_name.split("_")[0] #정답 숫자
        file_path = os.path.join(folder, file_name)
        with open(file_path, 'r') as f:
            data = f.read() #데이터 읽기
            data_list = [float(num) for num in data.split()]
            p = classify0(data_list, training_data, training_labels, k)
            if p != answer :
                error += 1
            entire += 1
    rate = error / entire * 100
    print("K={}일 때는 {}%".format(k, rate))



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <training_folder> <data_folder>")
        sys.exit(1)

    training_folder = sys.argv[1]
    data_folder = sys.argv[2]

    group, labels = trainingNumber(training_folder)
    for i in range(1, 30) :
        predictNumber(data_folder, group, labels, i)
