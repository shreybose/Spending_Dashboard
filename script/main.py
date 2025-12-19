import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# -----------------------------
# Assigned monthly totals
# -----------------------------
monthly_total_adjusted = {
    "Jan": 2900,   
    "Feb": 2780,  
    "Mar": 3800,  
    "Apr": 2970, 
    "May": 3700,
    "Jun": 2900,
    "Jul": 4000,
    "Aug": 3000,
    "Sep": 3200,
    "Oct": 3900,
    "Nov": 4200,
    "Dec": 3100
}

# -----------------------------
# Assigned category percentages
# -----------------------------
monthly_category_pct = {
    "Jan": {"Bills&Utilities": 0.57, "Health&Wellness": 0.16, "Groceries": 0.11, "Food&Drink": 0.09, "Gas": 0.04, "Other": 0.03},
    "Feb": {"Bills&Utilities": 0.59, "Groceries": 0.12,"Health&Wellness":0.09, "Food&Drink": 0.07, "Gas": 0.06, "Shopping": 0.06, "Entertainment": 0.07, "Other": 0.04},
    "Mar": {"Bills&Utilities": 0.43, "Travel": 0.22, "Food&Drink": 0.12, "Gas": 0.04, "Health&Wellness": 0.06, "Entertainment": 0.05, "Other": 0.04},
    "Apr": {"Bills&Utilities": 0.56, "Groceries": 0.12, "Food&Drink": 0.10, "Gas": 0.04, "Health&Wellness": 0.09, "Shopping": 0.08, "Other": 0.01},
    "May": {"Bills&Utilities": 0.46, "Travel": 0.23, "Food&Drink": 0.12, "Gas": 0.04, "Entertainment": 0.08, "Health&Wellness": 0.05, "Other": 0.02},
    "Jun": {"Bills&Utilities": 0.57, "Groceries": 0.13, "Food&Drink": 0.10, "Gas": 0.06, "Entertainment": 0.10, "Other": 0.05},
    "Jul": {"Bills&Utilities": 0.41, "Travel": 0.22, "Food&Drink": 0.12, "Gas": 0.03, "Shopping": 0.10, "Entertainment": 0.06, "Other": 0.06},
    "Aug": {"Bills&Utilities": 0.55, "Travel": 0.16, "Food&Drink": 0.09, "Gas": 0.03, "Health&Wellness": 0.09, "Entertainment": 0.06, "Other": 0.02},
    "Sep": {"Bills&Utilities": 0.52, "Travel": 0.15, "Food&Drink": 0.10, "Gas": 0.03, "Health&Wellness": 0.08, "Shopping": 0.08, "Entertainment": 0.03, "Other": 0.01},
    "Oct": {"Bills&Utilities": 0.43, "Travel": 0.18, "Food&Drink": 0.12, "Gas": 0.04, "Health&Wellness": 0.07, "Shopping": 0.08, "Entertainment": 0.03, "Other": 0.05},
    "Nov": {"Bills&Utilities": 0.39, "Travel": 0.13, "Food&Drink": 0.09, "Gas": 0.02, "Shopping": 0.08, "Entertainment": 0.04, "Other": 0.25},
    "Dec": {"Bills&Utilities": 0.53, "Food&Drink": 0.16, "Entertainment": 0.11, "Shopping": 0.09, "Gas": 0.05, "Other": 0.06}
}

# -----------------------------
# Assigned transaction count (non travel)
# -----------------------------
category_transaction_counts_non_travel = {
    "Groceries": (6, 8),
    "Food&Drink": (5, 10),
    "Entertainment": (2, 5),
    "Other": (3, 7),
    "Shopping": (3, 6),
    "Health & Wellness": (4, 8),
    "Gas": (4, 8),
    "Bills&Utilities": 1650
}

# -----------------------------
# Assigned transaction count (travel)
# -----------------------------
category_transaction_counts_travel = {
    "Groceries": (3, 5),
    "Food&Drink": (13, 20),
    "Entertainment": (8, 15),
    "Other": (5, 9),
    "Travel": (6, 12),
    "Shopping": (5, 8),
    "Health & Wellness": (2, 3),
    "Gas": (2, 4),
    "Bills&Utilities": 1650
}
travel_subcategories = {"Flights": 0.4, "Hotels": 0.4, "Rideshare": 0.2}

# -----------------------------
# Generating data
# -----------------------------
data = []

# Define Bills&Utilities subcategories and amounts
bills_subcategories = {
    "Rent": 1000,
    "Car": 550,
    "Phone": 100
}

for month_num in range(1, 13):
    month_name = datetime(2025, month_num, 1).strftime("%b")
    total = monthly_total_adjusted[month_name]
    
    # Determines category percentages
    category_pct = monthly_category_pct[month_name]
    
    # Calculates total per category
    category_totals = {cat: total * category_pct[cat] for cat in category_pct}
    
    # Select correct transaction counts based on travel/non travel months
    travel_months = {"Mar", "May", "Jul", "Aug", "Sep", "Oct", "Nov"}

    if month_name in travel_months:
        txn_counts_dict = category_transaction_counts_travel
    else:
        txn_counts_dict = category_transaction_counts_non_travel
    
    for cat, cat_total in category_totals.items():
        # Handle Bills&Utilities separately
        if cat == "Bills&Utilities":
            for subcat, amt in bills_subcategories.items():
                # Random date in month
                start_date = datetime(2025, month_num, 1)
                end_day = (datetime(2025, month_num + 1, 1) - timedelta(days=1)).day if month_num < 12 else 31
                date = start_date + timedelta(days=random.randint(0, end_day-1))
                
                record = {
                    "Date": date,
                    "Category": "Bills&Utilities",
                    "Amount": amt,
                    "Subcategory": subcat
                }
                data.append(record)
            continue  # skip the rest of the loop for Bills&Utilities

        # For other categories
        txn_val = txn_counts_dict.get(cat, (5,10))
        if isinstance(txn_val, tuple):
            t_min, t_max = txn_val
            num_transactions = random.randint(t_min, t_max)
        else:
            num_transactions = txn_val  # if fixed number
        
        for _ in range(num_transactions):
            # Random date within month
            start_date = datetime(2025, month_num, 1)
            end_day = (datetime(2025, month_num + 1, 1) - timedelta(days=1)).day if month_num < 12 else 31
            date = start_date + timedelta(days=random.randint(0, end_day-1))
            
            # Random amount for the transaction 
            if cat == "Groceries":
                amount = round(random.uniform(60,100),2)
            elif cat == "Travel":
                subcat = random.choices(list(travel_subcategories.keys()), weights=list(travel_subcategories.values()), k=1)[0]
                if subcat=="Flights":
                    amount = round(random.uniform(300,1000),2)
                elif subcat=="Hotels":
                    amount = round(random.uniform(150,500),2)
                else:
                    amount = round(random.uniform(10,50),2)
            else:
                amount = round(cat_total/num_transactions * random.uniform(0.5,1.5),2)
            
            record = {"Date": date, "Category": cat, "Amount": amount}
            record["Subcategory"] = subcat if cat=="Travel" else ""
            data.append(record)

# ----------------------------- 
# Create DataFrame and save 
# -----------------------------
df = pd.DataFrame(data) 
df.sort_values("Date", inplace=True) 
df.reset_index(drop=True, inplace=True) 
df.to_csv("synthetic_expenses_2025_realistic.csv", index=False) 
print(df.head(15))