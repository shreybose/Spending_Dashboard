# **Synthetic Credit Card Expense Dataset – 2025**

This project generates a **realistic synthetic dataset of personal credit card transactions** for the year 2025. The dataset is designed for **data analysis, visualization, and machine learning practice**, while keeping privacy intact.  

---

## **Features**

- **Monthly spending totals** are adjustable per month.  
- **Categories include:** Bills & Utilities, Groceries, Food & Drink, Travel, Entertainment, Shopping, Gas, Health & Wellness, Education, and Other.  
- **Bills & Utilities** split into **Rent, Car, and Phone** with exact amounts.  
- **Travel** split into **Flights, Hotels, and Rideshare** with realistic transaction amounts.  
- **Randomized transaction dates** within each month for realism.  
- **Transaction counts** vary per category and are adjusted for travel vs non-travel months.  
- Output saved as a **CSV file** for easy use in Excel, Pandas, or Tableau.

---

## **Dataset Columns**

| **Column**      | **Description**                        |
|-----------------|----------------------------------------|
| Date            | Date of transaction (YYYY-MM-DD)       |
| Category        | Main transaction category               |
| Amount          | Transaction amount in USD               |
| Subcategory     | Subcategory if any (e.g., Rent, Flights)      |

---

## **Usage**

1. **Clone the repository:**  
```bash
git clone <repo_url>
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **cd into the folder with main.py**
```bash
cd script
```

3.  **Run the script:**
```
python main.py
```

4. The generated CSV file synthetic_expenses_2025_realistic.csv will be saved in the project directory.

## **Applications**

- **Data analysis and visualization practice** (e.g., Tableau, Power BI, Matplotlib).  
- **Testing machine learning models** on financial data.  
- **Creating dashboards** for portfolio or resume projects without using personal data.  

---

## **Notes**

- This dataset is **fully synthetic**, containing **no sensitive or personal information**.  
- **Spending patterns are adjustable** by modifying `monthly_total_adjusted` and `monthly_category_pct`.  
- **Bills & Utilities** and **Travel** categories are handled with **realistic subcategory breakdowns** to simulate real-world transactions.  


