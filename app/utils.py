def project_future(data):
    income = data["income"]
    savings = data["savings"]
    spend = data["monthly_expense"]
    years = data.get("years", 10)
    projection = []
    for year in range(1, years + 1):
        savings += (income - spend) * 12
        projection.append({"year": year, "savings": round(savings, 2)})
    return projection

def analyze_behavior(data):
    spend = data["monthly_expense"]
    income = data["income"]
    ratio = round((spend / income) * 100, 2)
    return {"spend_ratio": ratio, "status": "Healthy" if ratio < 70 else "Warning"}

def backward_impact(data):
    choices = data.get("past_choices", [])
    impact = []
    for choice in choices:
        if choice == "new_car":
            impact.append({"choice": "New Car", "impact": "-₹5,00,000"})
        elif choice == "early_investment":
            impact.append({"choice": "Invested Early", "impact": "+₹8,00,000"})
    return impact
