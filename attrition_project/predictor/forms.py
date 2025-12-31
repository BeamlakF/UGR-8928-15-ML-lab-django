from django import forms

class EmployeeForm(forms.Form):
    Age = forms.IntegerField(label="Age")
    MonthlyIncome = forms.IntegerField(
    label="Monthly Income (1000-20000)",
    min_value=1000,
    max_value=20000)
    JobLevel = forms.IntegerField(label="Job Level (1–5)")
    JobSatisfaction = forms.IntegerField(label="Job Satisfaction (1–4)")
    WorkLifeBalance = forms.IntegerField(label="Work-Life Balance (1–4)")
    YearsAtCompany = forms.IntegerField(label="Years at Company")

    OverTime = forms.ChoiceField(
        label="Works Overtime?",
        choices=[(0, "No"), (1, "Yes")]
    )

    DistanceFromHome = forms.IntegerField(label="Distance From Home (km)")

    model = forms.ChoiceField(
        label="Prediction Model",
        choices=[
            ("lr", "Logistic Regression"),
            ("dt", "Decision Tree")
        ]
    )
