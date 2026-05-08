# Product-Analysis

# SaaS Subscription & Churn Analysis Project

To learn Python effectively, this project progresses from **Descriptive Analytics** (what happened?) to **Diagnostic/Advanced Analytics** (why did it happen?).

Below is the roadmap of metrics for this dataset, categorized by complexity and the Python skills required.

---

## 1. Basic Metrics (The "Health Check")
**Focus:** Mastering `pandas` basics like `.sum()`, `.count()`, and `.groupby()`.

* **Total Customers:** Count of unique `account_id` in the accounts table.
* **Active Subscriptions:** Count of records where the status is "Active."
* **Monthly Recurring Revenue (MRR):** Sum of the `monthly_price` from all active subscriptions.
* **Average Revenue Per User (ARPU):** Total Revenue divided by the total number of users.
* **Plan Distribution:** A breakdown of how many users are on "Basic" vs. "Premium" vs. "Enterprise."

---

## 2. Intermediate Metrics (Growth & Churn)
**Focus:** Learning date manipulation (`pd.to_datetime`), filtering, and calculating ratios.

* **Customer Churn Rate:**
    $$\text{Churn Rate} = \frac{\text{Customers Lost in Period}}{\text{Total Customers at Start of Period}} \times 100$$
* **Revenue Churn:** The amount of MRR lost due to cancellations.
* **Trial-to-Paid Conversion Rate:** Percentage of users moving from a "Trial" status to a paid tier.
* **Average Account Age (Tenure):** Difference between the `signup_date` and today (or `churn_date`).

---

## 3. Advanced Metrics (Deep Insights) - DO IT YOURSELF
**Focus:** Complex joins, window functions, and behavioral analysis.

* **Cohort Analysis:** Grouping users by "Signup Month" to track retention over time.
* **Customer Lifetime Value (LTV):**
    $$\text{LTV} = \frac{\text{ARPU}}{\text{User Churn Rate}}$$
* **Feature Adoption Rate:** Identifying which features are used most by non-churning users using the `feature_usage` table.
* **Support Impact on Churn:** Correlating `support_tickets` or satisfaction scores with churn likelihood.
* **Churn Heatmap:** Visualizing churn rates across different plans and geographical regions.

---

## 4. Suggested Dashboard Layout
The final dashboard (built with **Streamlit** or **Plotly Dash**) is organized into three primary views:

| Tab | Content |
| :--- | :--- |
| **Executive Summary** | Key KPIs: Total MRR, Total Customers, and Overall Churn Rate. |
| **Revenue & Plans** | Bar charts of revenue by plan type and growth trends over time. |
| **Customer Behavior** | Ticket volume vs. Churn and a Feature Usage leaderboard. |

---

<img width="1639" height="738" alt="Screenshot 2026-05-08 at 7 42 09 PM" src="https://github.com/user-attachments/assets/9f65f66d-26b1-48d7-894b-d048f48cdca2" />


## Why this project helps learn Python:
1.  **Data Cleaning:** Handling "Edge Cases" like mid-cycle plan changes or null satisfaction scores.
2.  **Relational Logic:** Learning how to `merge` (join) the `accounts`, `subscriptions`, and `churn_events` tables.
3.  **Visual Literacy:** Understanding when to use a `line plot` (trends) versus a `box plot` (distributions).
