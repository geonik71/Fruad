import streamlit as st
import pandas as pd
import numpy as np
import joblib









# Define the columns for feature selection

# App header
import streamlit as st

# Custom HTML for title with red background
title_html = """
    <div style="background-color: red; padding: 10px; border-radius: 5px;">
        <h1 style="color: white; text-align: center;">Ethereum Fraud Detection App</h1>
    </div>
"""

# Render the custom HTML
st.markdown(title_html, unsafe_allow_html=True)

# Introduction
st.header("Introduction")

st.write(
    """
    Welcome to the Ethereum Fraud Detection App! Ethereum is a decentralized blockchain platform that allows users to execute smart contracts and make peer-to-peer transactions using its native cryptocurrency, Ether (ETH). Each transaction is recorded on the blockchain and is publicly accessible, making Ethereum a popular platform for various decentralized applications.

    With the increasing volume of Ethereum transactions, there is a growing concern about fraudulent activities. Fraud detection in Ethereum transactions is crucial to ensure the integrity and security of the network.

    This app aims to detect potentially fraudulent transactions in the Ethereum network. We use machine learning techniques, specifically the XGBoost (XGB) algorithm, to predict and identify suspicious transactions. By analyzing key transaction data, we can provide insights into whether a transaction may be fraudulent or legitimate.
    """
)

st.sidebar.write("""
### Feature Selection
Select the features you want to use for prediction:
""")

# Feature selection checkboxes
Avg_min_between_sent_tnx_select = st.sidebar.slider('Avg min between sent tnx', 0, 430287)
Avg_min_between_received_tnx_select = st.sidebar.slider('Avg min between received tnx', 0, 482175)
Time_Diff_between_first_and_last_select = st.sidebar.slider('Time Diff between first and last (Mins)', 0, 1954861)
Sent_tnx_select = st.sidebar.slider('Sent tnx', 0, 10000)
Received_tnx_select = st.sidebar.slider('Recived tnx', 0, 10000)
Number_of_Created_Contracts_select = st.sidebar.slider('Number of Created Contracts', 0, 9995)
max_value_received_select = st.sidebar.slider('max value received', 0, 611102)
avg_val_received_select = st.sidebar.slider('avg val received', 0, 12963)
avg_val_sent_select = st.sidebar.slider('avg val sent', 0, 10162)
total_Ether_sent_select = st.sidebar.slider('total Ether sent', 0, 28580960)
total_Ether_balance_select = st.sidebar.slider('total Ether balance', 0, 14288640)
ERC20_total_Ether_received_select = st.sidebar.slider('ERC20 total Ether received', 0, 21000000000)
ERC20_total_Ether_sent_select = st.sidebar.slider('ERC20 total Ether sent', 0, 112000000000)
ERC20_total_Ether_sent_contract_select = st.sidebar.slider('ERC20 total Ether sent', 0, 416000)
ERC20_uniq_sent_addr_select = st.sidebar.slider('ERC20 uniq sent addr', 0, 4078)
ERC20_uniq_rec_token_name_select = st.sidebar.slider('ERC20 uniq rec token name', 0, 737)





row_list = [Avg_min_between_sent_tnx_select, Avg_min_between_received_tnx_select, Time_Diff_between_first_and_last_select, Sent_tnx_select,
            Received_tnx_select, Number_of_Created_Contracts_select, max_value_received_select, avg_val_received_select,
            avg_val_sent_select, total_Ether_sent_select, total_Ether_balance_select, ERC20_total_Ether_received_select,
            ERC20_total_Ether_sent_select, ERC20_total_Ether_sent_contract_select, ERC20_uniq_sent_addr_select, ERC20_uniq_rec_token_name_select ]

row_array = np.array(row_list).reshape(1, -1)



model = joblib.load('XGB.joblib')
prediction = model.predict(row_array)

if st.button('Predict'):
    if prediction[0] == 0:
        st.success("No fraud detected in this transaction.")
    else:
        st.warning("Warning: This transaction is potentially fraudulent!")




