import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')


df.dropna(inplace=True) 


features = df.drop('species', axis=1)
labels = df['species']

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)


X_train, X_test, y_train, y_test = train_test_split(
    scaled_features, labels, test_size=0.2, random_state=42
)


pd.DataFrame(X_train).to_csv("X_train.csv", index=False)
pd.DataFrame(X_test).to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("ETL pipeline completed and files saved.")
