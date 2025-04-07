import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [5, 6, 7, 8, 9]
}

df = pd.DataFrame(data)

X = df['feature1'].values.reshape(-1, 1)
y = df['feature2'].values

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
