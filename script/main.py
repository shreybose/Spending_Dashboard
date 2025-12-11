import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# -----------------------------
# Monthly totals
# -----------------------------
monthly_total = {
    "Jan": 2500, "Feb": 1780, "Mar": 2200, "Apr": 1970, "May": 2800, "Jun": 3200,
    "Jul": 3300, "Aug": 1500, "Sep": 1100, "Oct": 1800, "Nov": 2500, "Dec": 1800
}

# -----------------------------
# Category percentages
# -----------------------------
monthly_category_pct = {
    "Jan": {"Bills": 0.4, "Grocery":0.2, "Food&Drink":0.2, "Entertainment":0.1, "Other":0.1},
    "Feb": None, "Mar": None, "Apr": None, "May": None, "Jun": None,
    "Jul": {"Professional services":0.74, "Food&Drink":0.11, "Travel":0.06, "Shopping":0.04, "Groceries":0.02, "Health & wellness":0.01, "Gas":0.01},
    "Aug": {"Travel":0.46,"Food&Drink":0.21,"Personal":0.08,"Shopping":0.02,"Groceries":0.03,"Health & wellness":0.17,"Gas":0.02,"Entertainment":0.02},
    "Sep": {"Travel":0.05,"Food&Drink":0.37,"Personal":0.01,"Shopping":0.21,"Groceries":0.06,"Health & wellness":0.15,"Gas":0.10,"Entertainment":0.05},
    "Oct": {"Travel":0.39,"Food&Drink":0.29,"Personal":0.08,"Shopping":0.11,"Groceries":0.04,"Health & wellness":0.08,"Gas":0.03,"Entertainment":0.04,"Education":0.02},
    "Nov": {"Travel":0.38,"Bills&Utilities":0.24,"Food&Drink":0.23,"Personal":0.08,"Shopping":0.03,"Groceries":0.03,"Health & wellness":0.05,"Gas":0.01,"Entertainment":0.02},
    "Dec": {"Travel":0.61,"Food&Drink":0.39}
}

# -----------------------------
# Categories for random months
# -----------------------------
month_categories_random = {
    "Feb":["Bills","Grocery","Food&Drink","Personal","Entertainment"],
    "Mar":["Wellness","Travel","Food&Drink","Bills","Grocery","Personal"],
    "Apr":["Wellness","Food&Drink","Bills","Grocery","Travel","Entertainment"],
    "May":["Food&Drink","Wellness","Travel","Grocery","Bills","Entertainment"],
    "Jun":["Wellness","Food&Drink","Grocery","Bills","Travel","Entertainment"]
}

# -----------------------------
# Travel subcategories
# -----------------------------
travel_subcategories = {"Flights":0.5, "Hotels":0.3, "Rideshare":0.2}

# -----------------------------
# Transaction count logic per category
# -----------------------------
category_transaction_counts = {
    "Bills": (2,5),
    "Groceries": (8,12),
    "Food&Drink": (10,20),
    "Entertainment": (5,10),
    "Other": (3,6),
    "Personal": (5,10),
    "Travel": (3,8),
    "Professional services":(2,5),
    "Shopping":(3,7),
    "Health & wellness":(2,5),
    "Gas":(3,6),
    "Education":(1,3),
    "Bills&Utilities":(2,5),
    "Wellness":(2,5)
}

# -----------------------------
# Function to generate random percentages
# -----------------------------
def random_percentages(categories):
    weights = np.random.rand(len(categories))
    weights = weights / weights.sum()
    #print(dict(zip(categories, weights)))
    return dict(zip(categories, weights))