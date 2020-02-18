# -*- coding: utf-8 -*-
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, accuracy_score
from sklearn.model_selection import GridSearchCV, ParameterGrid, KFold
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

test_data=pd.read_csv("churn-bigml-20.csv")
training_data = pd.read_csv("churn-bigml-80.csv")
print(test_data.columns)
del training_data['State']
del training_data['Area code']
#del training_data['International plan']

#del training_data['Total day calls','Total day charge','Total eve minutes',
#  'Total eve calls', 'Total eve charge', 'Total night minutes',
#       'Total night calls', 'Total night charge', 'Total intl minutes']
 
del test_data['State']
del test_data['Area code']
#del test_data['International plan']
X_train = training_data.ix[:, 0:16]
y_train = training_data.ix[:, 16]
X_test = test_data.ix[:, 0:16]
y_test = test_data.ix[:, 16]
corr_matrix = X_train.corr()
#sns.heatmap(corr_matrix,cmap="YlGnBu",annot=True)
sns.heatmap(corr_matrix,cmap="YlGnBu")
plt.ylabel('Y ekseninindeki degerler')
plt.xlabel('X ekseninindeki degerler')
d = {'Yes':1,
     'No':0}
 
X_train['International plan'] = X_train['International plan'].map(d)
X_train['Voice mail plan'] = X_train['Voice mail plan'].map(d)
X_test['International plan'] = X_test['International plan'].map(d)
X_test['Voice mail plan'] = X_test['Voice mail plan'].map(d)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
classifiers = {'linear_svm': SVC(kernel='linear'),
       'poly_svm': SVC(kernel='poly'),
       'rbf_svm': SVC(kernel='rbf'),
       'knn_clf': KNeighborsClassifier(),
       'dcs_clf': DecisionTreeClassifier(),
       'rnd_clf': RandomForestClassifier(),
       'ext_clf': ExtraTreesClassifier(),
       'sgd_clf': SGDClassifier()
      }
 
for clf in classifiers:
    classifiers[clf].fit(X_train, y_train)
    print(clf, accuracy_score(y_test, classifiers[clf].predict(X_test)))
pipeline = Pipeline([('scaler', StandardScaler()),
                    ('rnd_clf', RandomForestClassifier())]
                   )
 
pipeline.fit(X_train, y_train)
joblib.dump(pipeline, 'churn.pkl')
plt.show()
