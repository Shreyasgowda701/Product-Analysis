import pandas as pd 


accounts = pd.read_csv("accounts.csv")
sub = pd.read_csv("subscriptions.csv")

# 1. Total Customers
uq = accounts['account_id'].nunique()
print("Total Customers is", uq)
print("------------------------------------")

# 2. Total Active Subscriptions
sp = sub[sub['churn_flag'] == False]
active = len(sp)
print("Total Active Subscriptiom is", active)
print("------------------------------------")

# 2. Monthly Recurring Revenue (MRR) 
mrr = sub.loc[sub["churn_flag"] == False, 'mrr_amount'].sum()
print("Monthly Recurring Revenue (MRR) is",mrr)
print("------------------------------------")

# 3.Average Monthly Revenue Per User (AMRPU)
acctive_sub = sub.loc[sub["churn_flag"] == False]
amr = acctive_sub['mrr_amount'].sum() / acctive_sub['account_id'].nunique()
#you can use any of this line
amr2 = (sub.loc[sub['churn_flag'] == False, 'mrr_amount'].sum()) / (sub.loc[sub['churn_flag'] == False, 'account_id'].nunique())
print("Average Monthly Revenue Per User is",amr)
print("------------------------------------")

# 4.Plan Distribution
plan = sub['plan_tier'].value_counts()
print(plan)

# Method 2
counts = sub['plan_tier'].value_counts()
pcts = sub["plan_tier"].value_counts(normalize=100) * 100
plan_dist = pd.DataFrame({'Total_User': counts,
                          'Percentage': pcts})
plan_dist = plan_dist.reset_index()
print(plan_dist)

# Method 3
pivot = sub.groupby('plan_tier').agg(user_count = ('subscription_id', 'count'))
total = pivot['user_count'].sum()
pivot['Percentage'] = (pivot['user_count'] / total) * 100
print(pivot.reset_index())





