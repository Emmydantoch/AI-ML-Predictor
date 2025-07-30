from django.shortcuts import render
from django.http import HttpResponse
from sklearn.linear_model import LinearRegression
import numpy as np

# Train model (use database in real project)
X = np.array([[1.5], [2], [3], [4.5], [5], [6], [7.5], [8], [9]])
y = np.array([20, 25, 35, 55, 60, 65, 75, 85, 90])
model = LinearRegression()
model.fit(X, y)


def index(request):
    result = None
    if request.method == "POST":
        try:
            hours = float(request.POST.get("hours"))
            predicted = model.predict([[hours]])
            result = round(predicted[0], 2)
        except:
            result = "Invalid input!"
    return render(request, "predictor/index.html", {"result": result})


def welcome(request):
    return HttpResponse("Welcome to Score Predictor!")
