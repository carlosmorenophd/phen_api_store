# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Support Vector Machine (SVM)

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, precision_recall_fscore_support
from matplotlib.colors import ListedColormap
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder


def print_hi(file):
    # Importing the dataset
    dataset = pd.read_csv(file)
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    transform_input = SimpleImputer(missing_values=np.nan, strategy='mean')
    # transform_input.fit(x)
    # x = transform_input.transform(x)
    # print(x)
    # Splitting the dataset into the Training set and Test set
    transform_input.fit(x)
    x = transform_input.transform(x)
    # le = LabelEncoder()
    # y = le.fit_transform(y)
    print(y)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)
    # x_train = transform_input.fit_transform(x_train)
    # x_test = transform_input.transform(x_test)
    # y_train = transform_input.fit_transform(y_train)
    # y_test = transform_input.transform(y_test)
    # print(x_train)
    # print(y_train)
    # print(x_test)
    # print(y_test)

    # Feature Scaling

    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)
    # print(x_train)
    # print(x_test)

    # Training the SVM model on the Training set

    classifier = SVC(kernel='linear', random_state=0)
    classifier.fit(x_train, y_train)

    # Predicting a new result
    # print(classifier.predict(sc.transform([[30, 87000]])))

    # Predicting the Test set results
    y_prediction = classifier.predict(x_test)
    # print(np.concatenate((y_prediction.reshape(len(y_prediction), 1), y_test.reshape(len(y_test), 1)), 1))

    # Making the Confusion Matrix

    cm = confusion_matrix(y_test, y_prediction)
    print('Matriz Confusion')
    print(cm)
    accuracy = accuracy_score(y_test, y_prediction)
    print(accuracy)
    roc = roc_auc_score(y_test, y_prediction,  pos_label=2)
    print('ROC')
    print(roc)
    f = precision_recall_fscore_support(y_test, y_prediction, average='macro')
    print('F')
    print(f)

    # Visualising the Training set results

    # x_set, y_set = sc.inverse_transform(x_train), y_train
    # x1, x2 = np.meshgrid(np.arange(start=x_set[:, 0].min() - 10, stop=x_set[:, 0].max() + 10, step=0.25),
    #                      np.arange(start=x_set[:, 1].min() - 1000, stop=x_set[:, 1].max() + 1000, step=0.25))
    # plt.contourf(x1, x2, classifier.predict(sc.transform(np.array([x1.ravel(), x2.ravel()]).T)).reshape(x1.shape),
    #              alpha=0.75, cmap=ListedColormap(('red', 'green')))
    # plt.xlim(x1.min(), x1.max())
    # plt.ylim(x2.min(), x2.max())
    # for i, j in enumerate(np.unique(y_set)):
    #     plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1], c=ListedColormap(('red', 'green'))(i), label=j)
    # plt.title('SVM (Training set)')
    # plt.xlabel('Age')
    # plt.ylabel('Estimated Salary')
    # plt.legend()
    # plt.show()
    #
    # # Visualising the Test set results
    #
    # x_set, y_set = sc.inverse_transform(x_test), y_test
    # x1, x2 = np.meshgrid(np.arange(start=x_set[:, 0].min() - 10, stop=x_set[:, 0].max() + 10, step=0.25),
    #                      np.arange(start=x_set[:, 1].min() - 1000, stop=x_set[:, 1].max() + 1000, step=0.25))
    # plt.contourf(x1, x2, classifier.predict(sc.transform(np.array([x1.ravel(), x2.ravel()]).T)).reshape(x1.shape),
    #              alpha=0.75, cmap=ListedColormap(('red', 'green')))
    # plt.xlim(x1.min(), x1.max())
    # plt.ylim(x2.min(), x2.max())
    # for i, j in enumerate(np.unique(y_set)):
    #     plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1], c=ListedColormap(('red', 'green'))(i), label=j)
    # plt.title('SVM (Test set)')
    # plt.xlabel('Age')
    # plt.ylabel('Estimated Salary')
    # plt.legend()
    # plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('AllVariable.csv')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
