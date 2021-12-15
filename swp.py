import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

#
# WELCOME & INTRODUCTION
#
st.title("Workforce Planninng Analysis")
st.header("Introduction")
st.write("Workforce planning isn't hard, but it isn't easy either. This app is designed to give you a taste of some of the tools and tricks of the trade to peak your interest and start putting your asumptions to the test. Enjoy, have fun, and more importantly, provide some feedback.")

#
# Sidebar
#
st.sidebar.text("Supply")
headcount = st.sidebar.number_input('Starting Headcount')
hires = st.sidebar.number_input('Hires')
transfers_in = st.sidebar.number_input('Transfers In')
attrition = st.sidebar.number_input('Attrition')
retirees = st.sidebar.number_input('Retirees')
transfers_out = st.sidebar.number_input("Transfers Out")
final_hc = (headcount + hires + transfers_in - attrition - transfers_out)
# st.sidebar.text("Final headcount: ", final_hc)

st.sidebar.text("Demand")
hc_demand = st.sidebar.number_input("Total Headcount Demand")


#
# SUPPLY ANALYSIS
#
st.header("Supply Analysis")
st.write("Use the sidebar to enter your inputs.")

# Create plot
fig = go.Figure(go.Waterfall(
    measure = ["relative", "relative", "relative", "relative", "relative", "relative", "total"],
    x = ["Starting Headcount", "Hires", "Transfers In", "Attrition", "Retirees", "Transfers Out", "Ending Headcount"],
    y = [headcount, hires, transfers_in, -(attrition), -(retirees), -(transfers_out), final_hc]
))
fig.update_layout(
    title = "Visualizing Talent Supply"
)
# Plot
st.plotly_chart(fig)

#
# DEMAND ANALYSIS
#
st.header("Baseline Demand Analysis")





#
# GAP ANALYSIS
#

st.header("Gap Analysis")