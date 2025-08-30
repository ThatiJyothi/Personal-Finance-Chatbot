from math import ceil

DEFAULT_PROFILES = {
    "student": {
        "income": 10000,
        "expenses": {"rent": 4000, "food": 2000, "transport": 1000, "shopping": 1000},
        "loan_payment": 3000,
        "current_savings": 2000
    },
    "professional": {
        "income": 50000,
        "expenses": {"rent": 15000, "food": 8000, "transport": 4000, "shopping": 3000},
        "loan_payment": 12000,
        "current_savings": 8000
    }
}

def budget_summary(income, expenses):
    total_expenses = sum(expenses.values())
    savings = income - total_expenses
    return (f"💰 **Budget Summary:**\n"
            f"Income: ₹{income}\n"
            f"Total Expenses: ₹{total_expenses}\n"
            f"Expected Savings: ₹{savings}\n"
            f"Tip: Track your expenses weekly to improve savings!")

def goal_planner(cost, months, current_savings=0):
    per_month = ceil(cost / max(1, months))
    status = "✅ You're on track!" if current_savings >= per_month else "⚠️ You may need to save more or extend your timeline."
    return f"🎯 **Goal Planner:** Save ₹{per_month}/month for {months} months. {status}"

def get_response(message: str, mode: str = "student") -> str:
    txt = message.lower()
    profile = DEFAULT_PROFILES.get(mode, DEFAULT_PROFILES["student"])

    # Greetings
    if any(g in txt for g in ("hi", "hello", "hey")):
        return ("👋 Hello! I can help you with budgeting, savings, loans, and financial goals. "
                )

    # Budget request
    if "budget" in txt or "summary" in txt:
        return budget_summary(profile["income"], profile["expenses"])

    # Loans / repayment advice
    if "loan" in txt or "repay" in txt or "student loan" in txt:
        if mode == "student":
            return ("📘 **Student Loan Tips:** Pay minimum installments and try to save 5–10% of your income. "
                    "Keep an emergency buffer of at least one month's expenses.")
        else:
            return ("💼 **Professional Loan Tips:** Allocate ~20% of your income to savings and prioritize high-interest loans. "
                    "Extra payments reduce interest over time.")

    # Goal planner
    if "goal" in txt or "laptop" in txt or "save for" in txt:
        # Simple static example, can be extended to parse user input
        return goal_planner(60000, 6, profile.get("current_savings", 0))

    # Spending categories
    if "spending" in txt or ("where" in txt and "money" in txt) or "categories" in txt:
        items = sorted(profile["expenses"].items(), key=lambda kv: kv[1], reverse=True)
        top = ", ".join([f"{k} (₹{v})" for k, v in items[:3]])
        return f"📊 **Top Spending Categories:** {top}\nTip: Focus on reducing your largest expenses first!"

    # Suggestions / recommendations
    if "suggest" in txt or "recommend" in txt or "advice" in txt:
        return ("💡 **Financial Tips:**\n"
                "- Automate monthly savings\n"
                "- Cancel one unnecessary subscription\n"
                "- Prioritize repaying high-interest debt\n"
                "- Track expenses daily to see where you can save more")

    # Emotional / supportive
    if "stress" in txt or "worried" in txt or "anxious" in txt:
        return ("🤝 It's normal to feel stressed about finances. Start small: track expenses this week, "
                "and celebrate small wins in saving or paying down debt.")

    # Fallback / goodbye
    if "bye" in txt or "goodbye" in txt:
        return "👋 Goodbye! Remember, I'm here anytime you want to check your finances or set new goals."

    # Generic fallback
    return ("🤔 I'm not sure I understand. You can ask me about budgeting, savings goals, loans, or spending tips!")

