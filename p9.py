import numpy as np
import  pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
import matplotlib.pyplot as plt
iris = load_iris()
x = iris.data
y = iris.target
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
decision_tree = DecisionTreeClassifier()
decision_tree.fit(x_train,y_train)
plt.figure(figsize=(12,8))
plot_tree(decision_tree,feature_names=iris.feature_names,class_names=iris.target_names,filled=True)
plt.show()
