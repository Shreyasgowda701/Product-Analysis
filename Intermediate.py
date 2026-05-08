import numpy as np
import pandas as pd

sub = pd.read_csv('subscriptions.csv')
churn = pd.read_csv('churn_events.csv')
account = pd.read_csv('accounts.csv')

# 1. Customer Churn Rate
customer_lost = sub.loc[sub['churn_flag'] == True, 'account_id' ].nunique()
total_customer = sub['account_id'].nunique()
ccr = (customer_lost / total_customer)*100
print("Customer Churn Rate is",ccr)
print("--------------------------------------------")

# 2. Revenue Churn
mrr = sub.loc[sub['churn_flag'] == True, 'mrr_amount' ].mean()
customer_lost = sub.loc[sub['churn_flag'] == True, 'account_id'].nunique()
total_loss = (mrr*customer_lost).__round__(2)
print("Amount of MRR lost due to cancellations", total_loss)
print("--------------------------------------------")

# 3. Trial-to-Paid Conversion Rate
trail = sub.loc[sub['is_trial'] == True, 'account_id'].unique()
paid = sub.loc[sub['is_trial'] == False, 'account_id'].unique()
converted = set(trail).intersection(set(paid))
total_trail = len(trail)
total_conversion = len(converted)
conversion_rate = (len(converted) / len(trail)) * 100
print('Trial-to-Paid Conversion Rate', conversion_rate)
print("--------------------------------------------")

# 4. Average Account Age (Tenure)
tenure = pd.merge(account, churn[['account_id', 'churn_date']], on='account_id', how='left')
current_date = pd.Timestamp.now()
tenure['Current_Date'] = tenure['churn_date'].fillna(current_date)
tenure['avg_tenure'] = (pd.to_datetime(tenure['Current_Date']) - pd.to_datetime(tenure['signup_date'])).dt.days
avg_tenure = tenure['avg_tenure'].mean()
print("Average Account Age (Tenure) is ", avg_tenure.__round__(2), 'days')
