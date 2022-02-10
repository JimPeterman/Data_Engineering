from sqlalchemy import create_engineimport pandas as pdimport pickleimport plotly.graph_objects as goengine = create_engine("sqlite:///data_NO_github/friend.db")df = pd.read_sql("SELECT * FROM data", engine)## Create the USA figure.df_usa = pd.DataFrame(df.query("Country == 'USA' & MaxRER >= 1.00"))df_usa = df_usa.State.value_counts()df_usa = df_usa.reset_index()df_usa = df_usa.set_axis(["State", "Count"], axis=1)fig = go.Figure(data=go.Choropleth(    locations=df_usa['State'],     z = df_usa['Count'].astype(float), # Data to be color-coded    locationmode = 'USA-states', # set of locations match entries in `locations`    colorscale = 'Greens',    colorbar_title = "Number of Tests",))fig.update_layout(    title_text = 'Current Distribution of Tests from the US in FRIEND<br>(Hover for number meeting RER ≥ 1.00)',    geo_scope='usa', # limite map scope to USA)with open('./data/summary_fig_usa.pickle', 'wb') as to_write:    pickle.dump(fig, to_write)## Create the global figure.df_world = pd.DataFrame(df.query("MaxRER >= 1.00"))df_world = df_world.Country.value_counts()df_world = df_world.reset_index()df_world = df_world.set_axis(["Country", "Count"], axis=1)fig = go.Figure(data=go.Choropleth(    locations=df_world['Country'],     z = df_world['Count'].astype(float), # Data to be color-coded    colorscale = 'Reds',    colorbar_title = "Number of Tests",))fig.update_layout(    title_text = 'Current Distribution of Tests from Around the World in FRIEND<br>(Hover for number meeting RER ≥ 1.00)',)with open('./data/summary_fig_global.pickle', 'wb') as to_write:    pickle.dump(fig, to_write)