# Metis_Engineering

The fifth and final project from my Metis Data Science Bootcamp involved building a data pipeline. 

I chose to build a data storage and processing pipeline that uses data from the Fitness Registry and Importance of Exercise International Database (FRIEND) to create summaries and regressions that are then deployed through a web app. The goal was to create a web app that highlights various aspects of the database in real time to increase interest in the project and therefore increase the contributions of test data to FRIEND.

The data pipeline involves storing the FRIEND data as a SQL database on Google Cloud. Processing involved analyzing the database on my local computer. Data cleaning and robustness testing was done with NumPy and Pandas. Summary figures were created with Plotly, Matplotlib, and Seaborn. The OLS linear regression was created with sklearn. A list of publications from FRIEND was collected via webscraping using BeautifulSoup. The web app was created with Streamlit. 

Included are:
- documents folder with a brief project summary and a slide deck for a short (5min) presentation.
- analysis folder with the Python files used for creating summary figures, regression models, and webscraping publications.
- pages folder with the Python files for the different pages of the web app.
- Python files for creating the SQL database and running the Streamlit web app.

The finalized web app can be found [here](https://share.streamlit.io/jimpeterman/metis_engineering/main/app.py)
