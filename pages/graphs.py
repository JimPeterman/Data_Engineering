# import pandas as pd# import numpy as npimport pickle# import plotly.graph_objects as go# import seaborn as snsimport matplotlib.pyplot as pltimport streamlit as stdef app():    st.write('''    ## Explore Trends in the Data from FRIEND        On this page, you can explore trends in VO2max or other health metrics.        At this time, we're only displaying trends from the US, but check back \    later for global trends!    ''')            ###### Create summary line graphs for VO2max metrics.    st.write('''    ### VO2max trends:    ''')        col1, col2 = st.columns(2)        with col1:        comp_pick = st.radio("What comparison are you interested in?",                              ("Male vs. Female", "Treadmill vs. Cycling",                               "Healthy vs. CVD", "US Regions"), index=0)                if "Regions" in comp_pick:            # Only display options for regions with >500 tests.            # Import list of regions with <500 tests.            with open('./data/line_graph_region_counts.pickle', 'rb') as to_read:                region_low_cts = pickle.load(to_read)            region_full = ["Midwest", "Northeast", "South", "West", "Pacific"]            region_options = [x for x in region_full if x not in region_low_cts]            # Use the options in the select box.            regions = st.multiselect("What regions are you intersted in? (Select\                                     all regions of interest).",                                     region_options)            # Print what regions are not included so users can know.            lst = ["**Region(s) not included due to <500 tests:"]            for region in region_low_cts:                lst.append(region)            st.write(" ".join(lst))                        int_in_cvd_cat = "No"        # cvd_categories = []        if "Healthy" in comp_pick:            int_in_cvd_cat = st.radio("Do you want to view individual CVD\                                  categories?", ("Yes", "No"), index=1)                        if int_in_cvd_cat == "Yes":                cvd_categories = st.multiselect("What CVD categories are you\                                        intersted in? (Select all categories of\                                        interest).", ["MI", "PCI", "CABG",                                           "HF"])                    # Import the appropriate summary data.             if int_in_cvd_cat == "Yes":            with open('./data/line_graph_modes_cvd_specific.pickle', 'rb') as to_read:                df = pickle.load(to_read)        elif "Healthy" in comp_pick:            with open('./data/line_graph_modes_cvd.pickle', 'rb') as to_read:                df = pickle.load(to_read)        elif "Regions" in comp_pick:            with open('./data/line_graph_modes_region.pickle', 'rb') as to_read:                df = pickle.load(to_read)         else:            with open('./data/line_graph_modes_separate.pickle', 'rb') as to_read:                df = pickle.load(to_read)                        with col2:        # Get the grouping variables.        if "Male" in comp_pick:            grp_pick = st.radio("Are you interested in treadmill tests or cycling\                                tests?", ("Treadmill", "Cycling"), index=0)            if "Treadmill" in grp_pick:                df_avg = df.query("ExMode == 'Treadmill'")            else:                df_avg = df.query("ExMode == 'Cycling'")                            elif "Treadmill" in comp_pick:            grp_pick = st.radio("Are you interested in data from males or\                                females?", ("Males", "Females"), index=0)            if "Males" in grp_pick:                df_avg = df.query("Sex == 'Male'")            elif "Females" in grp_pick:                df_avg = df.query("Sex == 'Female'")                             else:            grp_pick = st.radio("Are you interested in treadmill tests or cycling\                                tests?", ("Treadmill", "Cycling"), index=0)            if "Treadmill" in grp_pick:                df_avg = df.query("ExMode == 'Treadmill'")            else:                df_avg = df.query("ExMode == 'Cycling'")                         grp_pick2 = st.radio("Are you interested in data from males or\                                females?", ("Males", "Females"), index=0)            if "Males" in grp_pick2:                df_avg = df_avg.query("Sex == 'Male'")            elif "Females" in grp_pick2:                df_avg = df_avg.query("Sex == 'Female'")        # Set up the filtering and list for graphing.    if "Male" in comp_pick:        comp_lst = ["Male", "Female"]        query_col = "Sex"    elif "Treadmill" in comp_pick:        comp_lst = ["Treadmill", "Cycling"]        query_col = "ExMode"    elif "Healthy" in comp_pick:        if int_in_cvd_cat == "Yes":            comp_lst = ["Healthy"] + cvd_categories            query_col = "CVDcategory"        else:            comp_lst = ["Healthy", "CVD"]            query_col = "CVDstatus"    elif "Regions" in comp_pick:        comp_lst = regions        query_col = "CensusRegion"        # Plot!    fig, ax = plt.subplots(figsize=(9,5))        colors = ["blue", "darkorange", "forestgreen", "red", "y"]    # Counter for where to print VO2 values on graph.    count_multi = 0    count_two = [5, -5]    for idx, var in enumerate(comp_lst):        query = f"{query_col} == '{var}'"        label = var        x = df_avg.query(query).AgeGroup        y = df_avg.query(query).VO2_rel        error = df_avg.query(query).VO2_rel_std        upper = y + error        lower = y - error            ax.plot(x, y, label=label, color=colors[idx])        ax.plot(x, lower, alpha=0.1)        ax.plot(x, upper, alpha=0.1)        ax.fill_between(x, lower, upper, alpha=0.2)        if "Regions" in comp_pick or int_in_cvd_cat == "Yes":            for i,v in enumerate(y):                ax.text(i, 12+count_multi, f"{var[0]}: {v:.1f}", ha = "center",                         color = colors[idx], fontweight='bold')            count_multi += 2        elif int_in_cvd_cat == "Yes":            for i,v in enumerate(y):                ax.text(i, 12+count_multi, f"{var}: {v:.1f}", ha = "center",                         color = colors[idx], fontweight='bold')            count_multi += 1        else:            for i,v in enumerate(y):                ax.text(i, v+count_two[0], f"{v:.1f}", ha = "center",                        color = colors[idx], fontweight='bold')            count_two = count_two[1:]                    ax.legend(loc="upper right")    ax.set_xlabel('Age Group')    ax.set_ylabel("VO2max (ml/kg/min)")    ax.spines['top'].set_visible(False)    ax.spines['right'].set_visible(False)        st.pyplot(fig)    st.write("""    _The line on the graph indicates the average while the shaded area     represents the standard deviation._    """)        if int_in_cvd_cat == "Yes":        st.info("""        **_The CABG category includes those who also reported MI but does not \        include those who reported PCI or HF.         The PCI category excludes individuals who also reported CABG, MI, or HF.         The MI category does not include individuals who also reported CABG \        or HF.         The HF category does not exclude those who reported occurrence of \        any other CVD category._        """)                    ###### Create summary line graphs for non-VO2max metrics.    st.write('''    ### Trends for other health metrics:    _(Note: metrics from individuals who completed a treadmill exercise test)_    ''')        # Determine the variable of interest to graph.    var_int = st.radio("What metric are you interested in?",                        ("Maximum Heart Rate",                        "Resting Systolic Blood Pressure",                        "Height", "Weight",                        "BMI"), index=0)        with open('./data/line_graph_other_metrics.pickle', 'rb') as to_read:            df = pickle.load(to_read)        if "Pressure" in var_int:        y_label = var_int + " (mmHg)"        var_int = "RestingSBP"    elif "Heart" in var_int:        y_label = var_int + " (beats/min)"        var_int = "MaxHR"    elif "Height" in var_int:        y_label = var_int + " (inches)"    elif "Height" in var_int:        y_label = var_int + " (lbs)"    else:        y_label = var_int + " (kg/m2)"        var_int_SD = var_int + "_std"    fig, ax = plt.subplots(figsize=(9,5))        colors = ["blue", "darkorange"]    count_two = [2, -2] if var_int == "BMI" or var_int == "Height" else [6, -6]    for idx, var in enumerate(["Male", "Female"]):        query = f"Sex == '{var}'"        label = var        x = df.query(query).AgeGroup        y = df.query(query)[var_int]        error = df.query(query)[var_int_SD]        upper = y + error        lower = y - error            ax.plot(x, y, label=label, color=colors[idx])        ax.plot(x, lower, alpha=0.1)        ax.plot(x, upper, alpha=0.1)        ax.fill_between(x, lower, upper, alpha=0.2)        for i,v in enumerate(y):            ax.text(i, v+count_two[0], f"{v:.1f}", ha = "center",                        color = colors[idx], fontweight='bold')        count_two = count_two[1:]                ax.legend(loc="upper right")        ax.set_xlabel('Age Group')        ax.set_ylabel(y_label)        ax.spines['top'].set_visible(False)        ax.spines['right'].set_visible(False)        st.pyplot(fig)    st.write("""    _The line on the graph indicates the average while the shaded area     represents the standard deviation._    """)    