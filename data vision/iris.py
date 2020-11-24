from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris_dataset = load_iris()
# 查看数据集的描述
# print(iris_dataset.DESCR)
import pandas as pd

iris_df = pd.DataFrame(iris_dataset['data'],columns=iris_dataset.feature_names)
iris_df.head()

pd.plotting.scatter_matrix(iris_df, c=iris_dataset['target'],figsize=(15,15),marker='o',alpha=0.5)
#plt.savefig('matrix.png') # 保存
plt.show()