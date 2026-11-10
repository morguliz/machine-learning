# adaBoost classifier
from sklearn.ensemble import AdaBoostClassifier

# train
X_train = [
    [2, 60],
    [4, 75],
    [6, 80],
    [8, 90],
    [3, 65],
    [7, 85]
]

y_train = [0, 0 , 1 , 1, 0, 1]

adaBoost = AdaBoostClassifier(
    random_state=42
)

adaBoost.fit(X_train, y_train)

# prediction
X_test = [
    [5, 78]
]

prediction = adaBoost.predict(X_test)
print(prediction)
y_test = [1]

# evaluate
accuracy = adaBoost.score(X_test, y_test)
print(accuracy)