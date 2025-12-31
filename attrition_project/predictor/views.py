import os
import joblib
import pandas as pd

from django.shortcuts import render
from .forms import EmployeeForm

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logistic_model = joblib.load(
    os.path.join(BASE_DIR, "predictor/models/logistic_model.pkl")
)
decision_tree_model = joblib.load(
    os.path.join(BASE_DIR, "predictor/models/decision_tree_model.pkl")
)
scaler = joblib.load(
    os.path.join(BASE_DIR, "predictor/models/scaler.pkl")
)

def predict_employee(request):
    prediction = None

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            model_type = data.pop("model")
            df = pd.DataFrame([data])

            if model_type == "lr":
                df_scaled = scaler.transform(df)
                result = logistic_model.predict(df_scaled)[0]
            else:
                result = decision_tree_model.predict(df)[0]

            prediction = "Will Leave" if result == 1 else "Will Stay"
    else:
        form = EmployeeForm()

    return render(request, "index.html", {
        "form": form,
        "prediction": prediction
    })
