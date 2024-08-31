import streamlit as st
import pandas as pd


st.markdown('## Approve report')
st.write("")
st.write("")

st.markdown('### :cherry_blossom: Step 1: Select a month')
month_selected = st.selectbox("", ["Jun 2024", "Jul 2024", "Aug 2024", "Sep 2024"])
#st.write('You selected month: ', month_selected)

d = {'Month': [month_selected, month_selected], 'Type': ["Top Line", "Bottom Line"], 'Status': ['Approved', 'Not Approved']}
df = pd.DataFrame(d)


st.write(df[['Month', 'Type', 'Status']])

st.write("")
st.markdown('### :sunflower: Step 2: Approve to make report visiable')


month_to_approve = df[df['Status']=='Not Approved']
#st.write("You can approve this month: ")

## :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:

st.markdown("You can approve this month: ")
st.write("   -  ", month_to_approve['Month'].values.tolist()[0] , " -  " , month_to_approve['Type'].values.tolist()[0])



st.button("Click me to approve")

