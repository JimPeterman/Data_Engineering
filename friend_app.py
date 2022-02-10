# import pandas as pd# import numpy as npimport pickle# import plotly.graph_objects as go# import seaborn as sns# import matplotlib.pyplot as pltimport streamlit as st# Welcome header/information.col1, mid, col2 = st.columns([2,1,20])with col1:    st.image('./images/FRIEND_logo.jpg', width=100)with col2:    st.write('# Welcome to FRIEND!')st.write('''"FRIEND" stands for the **Fitness Registry and Importance of Exercise International Database**.It is an international database of cardiorespiratory fitness tests from high-quality laboratories.Below you will find a variety of summaries about the database and highlights of reaserch from the database.''')# Data import.# with open('./cleaned_dataframe.pickle','rb') as read_file:#     df = pickle.load(read_file)       ###### Start with showing states with test data.st.write('''## Where the test data comes from''')show_map = st.radio("Location of interest:", ("United States", "Global"), index=0)if show_map == "United States":    with open('data/summary_fig_usa.pickle','rb') as read_file:        fig = pickle.load(read_file)else:    with open('data/summary_fig_global.pickle','rb') as read_file:        fig = pickle.load(read_file)st.plotly_chart(fig)          ###### Create a CRF percentile calculator.from ref_calcs import friend_percentilest.write('''## Determine your fitness percentile(Reference values for fitness percentiles are based on US-only data and come from  [this 2022 FRIEND publication](https://www.mayoclinicproceedings.org/article/S0025-6196(21)00645-5/fulltext))''')crf_type = st.radio("Do you already know your VO2max?", ("Yes", "No"), index=1)if crf_type == "Yes":    col1, col2 = st.columns(2)        with col1:        sex = st.selectbox("Your sex:", ("Male", "Female"), index=1)        mode = st.selectbox("Testing mode you used:",                             ("Treadmill", "Cycle Ergometer"), index=0)        with col2:        age = st.selectbox("Your age range:", ("20-29", "30-39", "40-49",                                               "50-59", "60-69", "70-79",                                                "80-89"), index=1)        age = int(age[:2])        vo_2 = st.number_input('Enter your VO2max value:', min_value=(0.0),                            max_value=(99.9), step=0.1, value=38.6)        crf_perc = friend_percentile(vo_2, age, sex, mode)        st.metric("Your fitness percentile is:", crf_perc)else:    st.write("""             This estimated CRF comes from real-time regression              analysis on FRIEND.""")    col1, col2 = st.columns(2)        with col1:        sex = st.selectbox("Your sex:", ("Male", "Female"), index=1)        sex_num = 1 if sex == "Male" else 0        ht = st.selectbox("Select your height:",                           ("5 ft, 0 in", "5ft, 1 in",                           "5 ft, 2 in", "5ft, 3 in",                           "5 ft, 4 in", "5ft, 5 in",                           "5 ft, 6 in", "5ft, 7 in",                           "5 ft, 8 in", "5ft, 9 in",                           "5 ft, 10 in", "5ft, 11 in",                           "6 ft, 0 in", "6ft, 1 in",                           "6 ft, 2 in", "6ft, 3 in",                           "6 ft, 4 in", "6ft, 5 in",                           "6 ft, 6 in", "6ft, 7 in",                           "6 ft, 8 in", "6ft, 9 in",                           "6 ft, 10 in", "6ft, 11 in"), index=7)        ht = (int(ht.split(", ")[0][0]) * 12) + (int(ht.split(", ")[1][:2]))        mode = st.selectbox("What exercise mode are you interested in",                        ("Treadmill", "Cycling"), index=0)        mode_num = 1 if mode == "Treadmill" else 0        with col2:        age = st.number_input("Enter your age:", min_value=(18), max_value=(90),                              step=1, value=(29))        wt = st.slider("Select your weight (in lbs):", min_value=(40),                       max_value=(350), value=(170), step=(1))        cvd = st.selectbox("Do you have CVD?", ("Yes", "No"), index=1)        cvd = 1 if cvd == "Yes" else 0    reg_type = st.radio("Which data do you want to use in estimating your VO2max?",                    ("US only", "Global"), index=0)            if reg_type == "US only":        with open('./data/reg_model_usa.pickle','rb') as read_file:            lm_OLS = pickle.load(read_file)    else:        pass        vo_2 = round(lm_OLS.predict([[age, sex_num, ht, wt, cvd, mode_num]])[0],1)    crf_perc = friend_percentile(vo_2, age, sex, mode)    st.metric("Your estimated VO2max is:", vo_2)    st.metric("Your fitness percentile is:", crf_perc)    