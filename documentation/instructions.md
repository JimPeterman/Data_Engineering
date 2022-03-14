# FRIEND Data Pipeline and Web App Instructions

### Folders.
_analysis Folder_: The files in this folder create the regressions and summaries used for the web app. The data produced ends up in the data folder.
- line graph summaries: creates the summary data used for making the fitness and other health metrics trends graphs.
- publication scraper: scrapes the FRIEND publications and outputs the format in a way that can be easily used for the web app.
- regression creation: creates the regression equations as well as the metrics for those regressions.
- summary test count: creates the figures summarizing where all of the data comes from.

_data Folder_: This folder contains all the data used by the web app. It includes summary tables, regression models, figures, and lists of certain variables to be used as user-interface options.

_images Folder_: Images embedded on the website (i.e., FRIEND logo)

_pages Folder_: These files are used for the web app pages. 
- graphs: This creates the graphs for the fitness and other health metrics trends across ages. 
- home: This is for the home page of the web app.
- personnel: For the personnel page that lists those associated with FRIEND and my contact information.
- publications: The publications page.
- regressions: The fitness predictions and fitness percentiles page.
- summaries: The summary of where the data comes from page.

_documentation Folder_: includes presentation and written summary used for Metis. Web app has since been updated so these are a little outdated. 


### Files:
_app_: The primary file used by Streamlit to deploy the web app.

_main summary_: Run this to update the data folder for the web app (does not update publications).

_multipage_: This is used by app.py to make multiple pages within Streamlit.

_ref calcs_: This is the function used to determine fitness percentiles.

_sql db creation_: File to convert the .xlsx database into a SQL database. The result is saved on my local computer and not in the data folder since FRIEND is not currently available to all of the public.

_requirements_: A list of the libraries used by Streamlit to run the app. From the terminal, can type “pip show pandas” to find version. 
