def get_advice(data):
    goal = data.get("goal", "retirement")
    if goal == "retirement":
        return "Invest 30% of your monthly income in mutual funds and PPF."
    elif goal == "house":
        return "Start a recurring deposit and avoid luxury spends."
    else:
        return "Keep your expense ratio under 50% and diversify income sources."
