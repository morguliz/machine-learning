from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

# train
X_train = [
    [2, 60],
    [4, 75],
    [6, 80],
    [8, 90],
    [3, 65],
    [7, 85]
]

y_train = [55, 65, 78, 92, 60, 85]

gradientBoost = GradientBoostingRegressor(
    random_state=42,
    learning_rate=0.1
)

gradientBoost.fit(X_train, y_train)

# prediction
X_test = [
    [5, 78],
    [7, 88],
    [3, 70],
    [6, 82]
]

y_test = [75, 87, 62, 80]

predictions = gradientBoost.predict(X_test)
print(predictions)


# regression evaluation
mae = mean_absolute_error(y_test, predictions)
print(mae)

r2 = gradientBoost.score(X_test, y_test)
print(r2)