# FRIEND Data Pipeline and Web App

In brief, the goal of this project was to create a web app that highlights various aspects of the Fitness Registry and Importance of Exercise International Database (FRIEND) that can be updated in real-time. **The web app can be found [HERE](https://share.streamlit.io/jimpeterman/metis_engineering/main/app.py)**.

### The Rationale:
The American Heart Association recommends that fitness (i.e., maximum oxygen consumption [VO2max]) be considered a clinical vital sign that is regularly assessed in the same manner as other risk factors (e.g., blood pressure, cholesterol levels, and body weight). Like other risk factors, the accurate interpretation of fitness requires reference standards to stratify patient risk by first determining what constitutes a “normal” value for that individual. The **Fitness Registry and Importance of Exercise International Database (FRIEND)** was established with the goal of creating accurate fitness reference standards. Accurate reference standards, though, require representative data from around the US and world. 

Of note, measuring fitness by having an individual perform an exercise test is not always feasible or desirable. In these situations, the American Heart Association recommends fitness be estimated. I have previously published papers highlighting errors associated with current prediction models ([acute assessments of non-exercise models](https://pubmed.ncbi.nlm.nih.gov/33838037/), [longitudinal assessment of non-exercise models](https://pubmed.ncbi.nlm.nih.gov/32458761/#:~:text=The%20median%20percentage%20of%20participants,to%20detect%20changes%20in%20CRF.), and [acute assessments of exercise models](https://pubmed.ncbi.nlm.nih.gov/32694370/)). Larger amounts of fitness test data (along with non-exercise data) could improve upon current prediction models and assist clinicians with meeting the American Heart Association recommendations.

FRIEND currently contains data from over 120k fitness tests, yet more data is needed. In my position at Ball State University, I have been working to increase the contributions of data to FRIEND. To better increase interest and data contributions to the registry, **_the goal of this project was to create a web app that highlights various aspects of FRIEND that can be updated in real-time as data is added to FRIEND_**. As it so happens, I was able to combine this goal with my fifth and final project for my Metis Data Science Bootcamp, in which the guidelines were to build a data pipeline and/or web app.

### The Final Product:
The data pipeline for this project allows for real-time updates to the web app as data is added to FRIEND. **The web app can be found [HERE](https://share.streamlit.io/jimpeterman/metis_engineering/main/app.py)**. The web app itself is interactive to foster interest in FRIEND and includes:
- Maps indicating where data within FRIEND has been collected.
- Distributions of some variables within FRIEND.
- Trends in fitness across ages and across different categories (e.g., different US Census regions, treadmill vs. cycling).
- Trends in other health metrics across ages (e.g., blood pressure, BMI).
- Determinations of fitness percentile based on user-entered values. If fitness level is unknown, real-time prediction models can be used to estimate fitness and fitness percentile. For those interested, performance metrics for these models can also be viewed.
- A list of publications that have come from FRIEND.


### The Process:
_Database creation and storage_: The FRIEND dataset is converted to a SQL database and saved on Google Cloud. Considering FRIEND is not currently updated frequently, the data pipeline involves copying the SQL database from Google Cloud back to my local computer when updates to the web app are needed.  

_Summary figures_: Summaries of the different variables within FRIEND are created when there are updates to FRIEND. These included locations of where the data was collected, distributions of variables (e.g., age), and trends in variables (e.g., changes to fitness with increasing age). The resulting figures for the web app are created with Plotly, Matplotlib, or Seaborn.

_Publications summary_: A list of publications from FRIEND is collected via webscraping using BeautifulSoup. This list is not saved with the SQL database since it is more regularly updated.

_Fitness percentile calculator_: An individual’s fitness percentile can be calculated based on age, sex, fitness level, and exercise test mode. The fitness percentile is calculated from [current fitness reference standards](https://www.mayoclinicproceedings.org/article/S0025-6196(21)00645-5/fulltext), of which I led the analysis. 

_Regression models_: An OLS linear regression model is created using sklearn to predict an individual’s fitness from their age, sex, height, weight, test exercise mode, and country (I have [previously published findings of global differences in fitness](https://pubmed.ncbi.nlm.nih.gov/31883698/)). An additional global regression model is also created. Along with the prediction of fitness, the individual’s fitness percentile is calculated. Performance metrics (i.e., R^2, RMSE, MAE) along with figures of model fit are determined for each regression model using sklearn and matplotlib.

_Web app_: The web app is deployed using Streamlit.

_Testing and robustness_: Data cleaning during processing is used to eliminate extraneous values prior to the creation of the data summaries and regressions. This is done with NumPy and Pandas. Various lists are also created from the dataset and then used as options in the user interface of the web app to improve robustness of the data pipeline.

Additional details about the process can be found in the documentation folder of this repository. 

Summary of tools/libraries used for this project:
- SQLite
- Google Cloud
- Pandas
- NumPy
- sklearn
- BeautifulSoup
- Streamlit
- Plotly
- Matplotlib
- Seaborn


