from sklearn.ensemble import RandomForestClassifier

# train
X_train = [
    # [hours_studied, attendance, sleep, previous_exam_score]
    [8, 90, 7, 85],
    [2, 50, 5, 45],
    [6, 80, 8, 75],
    [1, 40, 4, 35],
    [7, 85, 7, 80],
    [3, 60, 6, 50]
]

y_train = [1, 0, 1, 0, 1, 0]

classifer = RandomForestClassifier(
    n_estimators=10,
    random_state=42,
    max_features=2
)

classifer.fit(X_train, y_train)

# generate predictions
X_test = [
    [5, 75, 7, 70]
    ]

predictions = classifer.predict(X_test)
y_test = [1]
print(predictions)
# evaluate accuracy
accuracy = classifer.score(X_test, y_test)
print(accuracy)