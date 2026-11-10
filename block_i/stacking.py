from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

import pandas as pd

top_250 = pd.read_csv("/Users/macbookair/School/Loyola/fall26/_csv_data/top_250_players_fc26.csv")
# print(top_250.head())
# print(top_250.columns)

# base learners
lr = LogisticRegression(
    random_state=42,
)

knn = KNeighborsClassifier(
    n_neighbors=3
)

dt = DecisionTreeClassifier(
    random_state=42
)  

estimators = [
    ("lr", lr),
    ("knn", knn),
    ("dt", dt)
    ]

# meta learner
stacking = StackingClassifier(
    estimators = estimators,
    final_estimator = LogisticRegression(random_state=42)
)

# training
median_value = top_250["value_eur"].median() # classification theshold
print(f"median value: €{median_value}")

X = top_250[
    ["pace",
    "shooting",
    "passing",
    "dribbling",
    "defending",
    "physical"]
]
y = (top_250["value_eur"]>= median_value).astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# train the entire ensemble
stacking.fit(X_train, y_train)

# predictions
predictions = stacking.predict(X_test)
print(predictions)

# evaluating the stacking classifier
accuracy = stacking.score(X_test, y_test)
print(accuracy)