import streamlit as st
import pandas as pd
import plotly.express as px
from Basic import uq, active, mrr, amr, plan_dist, sp
from Intermediate import ccr, total_loss, conversion_rate, avg_tenure, tenure

st.set_page_config(page_title="RavenStack SaaS Analysis", layout='wide')
st.title("RavenStack SaaS Analysis")



col1, col2, col3, col4= st.columns(4)
col1.metric("Total Customers", uq)
col2.metric("Total Active Subscriptions", active)
col3.metric("Monthly Recurring Revenue", mrr)
col4.metric("Average Monthly Revenue Per User", amr)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Churn Rate", f"{ccr:.1f}%")
m2.metric("Revenue Lost", f"${total_loss:,.2f}", delta_color="inverse")
m3.metric("Trial Conversion", f"{conversion_rate:.1f}%")
m4.metric("Avg Tenure", f"{avg_tenure:.0f} Days")
st.divider()

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Plan Tier Distribution (Count)")
    fig_bar = px.bar(plan_dist, x='plan_tier', y='Total_User', text_auto=True, color='plan_tier')
    st.plotly_chart(fig_bar, use_container_width=True)
    
    st.subheader("Account Age Distribution")
    fig_hist = px.histogram(tenure, x='avg_tenure', nbins=20, labels={'avg_tenure': 'Days Active'})
    st.plotly_chart(fig_hist, use_container_width=True)
    
with col_right:
    st.subheader("Revenue Share by Tier")
    mrr_dist = sp.groupby('plan_tier')['mrr_amount'].sum().reset_index()
    fig_pie = px.pie(mrr_dist, values='mrr_amount', names='plan_tier', hole=0.5)
    st.plotly_chart(fig_pie, use_container_width=True)

with st.expander("View Raw Plan Distribution Data"):
    st.table(plan_dist)