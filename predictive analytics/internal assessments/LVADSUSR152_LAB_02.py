# -*- coding: utf-8 -*-
"""cust_m_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18UtI6v2-LfmHG0_kC4QuB4eXmZs4qbsh
"""

import pandas as pd

df_mall = pd.read_csv('Mall_Customers.csv')
df_mall.info()

df_mall.head(2)

df_mall.isnull().sum()

df_mall = df_mall.bfill(axis='columns')
df_mall.isnull().sum()

import matplotlib.pyplot as plt

plt.boxplot(df_mall['Age'])



plt.boxplot(df_mall['Annual Income (k$)'])

df_mall = df_mall[df_mall['Annual Income (k$)']<130]

# Commented out IPython magic to ensure Python compatibility.
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder



lbl = LabelEncoder()

km = KMeans(n_clusters=3)
df_mall['Gender'] = lbl.fit_transform(df_mall['Gender'])
y_predicted = km.fit_predict(df_mall[['Gender','Age','Annual Income (k$)','Spending Score (1-100)']])

df_mall['cluster']=y_predicted
print(df_mall.head())

km.cluster_centers_

print(km.cluster_centers_)

df1 = df_mall[df_mall.cluster==0]
df2 = df_mall[df_mall.cluster==1]
df3 = df_mall[df_mall.cluster==2]
plt.scatter(df1.Age,df1['Spending Score (1-100)'],color='green')
plt.scatter(df2.Age,df2['Spending Score (1-100)'],color='red')
plt.scatter(df3.Age,df3['Spending Score (1-100)'],color='black')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('Age')
plt.ylabel('Spending Score (1-100)')
plt.legend()

scaler = MinMaxScaler()
scaler.fit(df_mall[['Spending Score (1-100)']])
df_mall['Spending Score (1-100)'] = scaler.transform(df_mall[['Spending Score (1-100)']])
scaler.fit(df_mall[['Age']])
df_mall['Age'] = scaler.transform(df_mall[['Age']])
print(df_mall.head())
plt.scatter(df_mall.Age,df_mall['Spending Score (1-100)'])


km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df_mall[['Age','Spending Score (1-100)']])
df_mall['cluster']=y_predicted
df_mall.head(25)
print(km.cluster_centers_)

sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df_mall[['Age','Spending Score (1-100)']])
    sse.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng,sse)