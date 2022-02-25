import streamlit as stdef app():        # Welcome header/information.    col1, mid, col2 = st.columns([3,.1,3])    with col1:        st.image('./images/FRIEND_logo.jpg', width=250)    with col2:        st.write("# Welcome to FRIEND!")        st.write('''    "FRIEND" stands for the **Fitness Registry and Importance of Exercise     International Database**. FRIEND is an international database of     cardiorespiratory fitness tests collected in high-quality laboratories    from around the world.        **This web app was designed for researchers, clinicians, and the general \    public to highlight various aspects of the FRIEND project.** On the \    left you can navigate to different pages to view:         - Where the data in FRIEND comes from as well as distributions of \    some variables within FRIEND (_"Data Distributions"_ page).    - Trends in fitness (VO2max) data or other health metrics \    (_"Data Trends"_ page).     - Use a calculator to estimate your fitness (VO2max) and \        determine your fitness percentile (_"Assess Your Fitness"_ page).    - The list of publications that involved FRIEND \    (_"Publications"_ page).    - The people and support associated with recruiting contributors \    to FRIEND and maintaining the database (_"People and Support"_ \    page)        Have fun exploring the different pages and be sure to reach out if \    your lab or clinic is interested in contributing data!        _*Note, the data presented on these pages comes from real-time analysis \    of FRIEND and may differ slightly from previous publications._    ''')            