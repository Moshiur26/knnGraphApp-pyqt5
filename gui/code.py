import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import precision_recall_fscore_support


def get_accuracy(path):
    while True:
        try:

            #dataset_name = "hayes-roth.csv"
            #path = "E:/Subject/Capston/Farid Sir/Dataset/Classification-Datasets-master/"
            #data = pd.read_csv(path + dataset_name)
            data = pd.read_csv(path)
            data = np.asarray(data)
            X = data[:, :data.shape[1] - 1]
            X = X.astype(np.float)
            y = data[:, -1:]

            number_of_class = len(np.unique(y))
            mp_size = 90

            KS = np.arange(number_of_class, number_of_class+mp_size*1, 1)
            #KS = np.arange(1, mp_size + 1, 1)
            mp = np.zeros((1, mp_size * 2)).reshape(mp_size, 2)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=190)
            prf = []

            for j in range(mp_size):
                knn = KNeighborsClassifier(n_neighbors=KS[j])
                knn.fit(X_train, y_train)
                pridictions = knn.predict(X_test)
                accuracy = metrics.accuracy_score(y_test, pridictions)
                mp[j][0] = KS[j]
                mp[j][1] = accuracy
                print(mp[j][0])

            mp = np.asarray(mp)
            print("Code Run Successfully")
            break
        except:
            print("Get An Error")
            return np.asarray([1])
    return  mp

print(get_accuracy("E:/Subject/Capston/Farid Sir/Dataset/Classification-Datasets-master/wine.csv"))
#i= np.arange(0,90)
#plt.xlabel("Number")
#plt.ylabel("Accuracy")
#plt.plot(mp[:,0],mp[:,1],color='blue')
