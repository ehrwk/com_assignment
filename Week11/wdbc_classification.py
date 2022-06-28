import numpy as np
import matplotlib.pyplot as plt
from sklearn import (datasets, linear_model, svm)

from sklearn import (datasets, tree, metrics)

from matplotlib.lines import Line2D 
import csv

def load_wdbc_data(filename):
    class WDBCData:
        data = []
        target = []
        target_names = ['malignant', 'benign']
        feature_names = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness', 'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension',
                         'radius error', 'texture error', 'perimeter error', 'area error', 'smoothness error', 'compactness error', 'concavity error', 'concave points error', 'symmetry error', 'fractal dimension error',
                         'worst radius', 'worst texture', 'worst perimeter', 'worst area', 'worst smoothness', 'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry', 'worst fractal dimension']
    wdbc = WDBCData()

    with open(filename, 'r') as f:
        data_reader = csv.reader(f)
        for line in data_reader:
            dx = [line[i] for i in range(2, len(line))]
            wdbc.data.append(dx)
            if(line[1] == 'M'):
                wdbc.target.append(0)
            else:
                wdbc.target.append(1)
    
    
    wdbc.data = np.array(wdbc.data, dtype=np.float_)
    return wdbc

if __name__ == '__main__':
    wdbc = load_wdbc_data('data/wdbc.data') 

    # Train a model
    model = linear_model.SGDClassifier(learning_rate='constant', eta0=0.1)
    model.fit(wdbc.data, wdbc.target)
    
    model1 = tree.DecisionTreeClassifier(max_depth=2)
    model1.fit(wdbc.data, wdbc.target)
    
    
    # Test the model
    predict = model.predict(wdbc.data)
    n_correct = sum(predict == wdbc.target)
    accuracy = n_correct / len(wdbc.data)
    bal_accurancy = metrics.balanced_accuracy_score(wdbc.target, predict)
        
    predict1 = model1.predict(wdbc.data)
    accuracy1 = metrics.balanced_accuracy_score(wdbc.target, predict1)
    
    

    # Visualize testing results
    cmap = np.array([(1, 0, 0), (0, 1, 0)])
    clabel = [Line2D([0], [0], marker='o', lw=0, label=wdbc.target_names[i], color=cmap[i]) for i in range(len(cmap))]
    for (x, y) in [(0, 1)]:
        plt.title(f'svm.SVC ({n_correct}/{len(wdbc.data)}={accuracy:.3f}) \n (balanced accurancy: ({bal_accurancy:.3f})')
        plt.scatter(wdbc.data[:,x], wdbc.data[:,y], c=cmap[wdbc.target], edgecolors=cmap[predict])
        plt.xlabel(wdbc.feature_names[x])
        plt.ylabel(wdbc.feature_names[y])
        plt.legend(handles=clabel, framealpha=0.5)
        plt.show()
        
    for (x, y) in [(0, 1)]:
        plt.title(f'Decision tree (balanced accurancy: ({accuracy1:.3f}))')
        plt.scatter(wdbc.data[:,x], wdbc.data[:,y], c=cmap[wdbc.target], edgecolors=cmap[predict1])
        plt.xlabel(wdbc.feature_names[x])
        plt.ylabel(wdbc.feature_names[y])
        plt.legend(handles=clabel, framealpha=0.5)
        plt.show()
   
    
    
