# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 11:44:44 2022

@author: Shinemet
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st

import warnings
warnings.filterwarnings("ignore")

################# Import data #################

data = pd.read_csv(r"C:\Users\Shinemet\Ironhack\Projects\Project5\Work files\heart.csv")

##################### Layout #########################

st.set_page_config(layout="wide")

st.markdown("## Heart Disease Dataset Analysis")   ## Main Title


############ Common references ############

# continuous features
measurements = ['trestbps', 'chol', 'thalach']

# categorical features
categories = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal', 'target']

################# Dynamic scatter plot #################

st.sidebar.markdown("### Blood Measurements (Scatter Plot)")

x_axis = st.sidebar.selectbox("X-Axis", measurements)
y_axis = st.sidebar.selectbox("Y-Axis", measurements, index=1)

if x_axis and y_axis:
    scatter_fig = plt.figure(figsize=(12,8))

    scatter_ax = scatter_fig.add_subplot(111)

    low_attack = data[data["target"] == 0]
    high_attack = data[data["target"] == 1]

    low_attack.plot.scatter(x=x_axis, y=y_axis, s=120, c="tomato", alpha=0.6, ax=scatter_ax, label="High risk of heart attack")
    high_attack.plot.scatter(x=x_axis, y=y_axis, s=120, c="dodgerblue", alpha=0.6, ax=scatter_ax,
                           title="{} vs {}".format(x_axis.capitalize(), y_axis.capitalize()), label="Low risk of heart attack");


########################### Dynamic Pie Chart ###########################


st.sidebar.markdown("### Patients Split by Categorical Features (Pie Chart)")

data_cat = data[['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal', 'target']]
pie_axis = st.sidebar.selectbox(label='Patients Split by Feature', options=categories)

colors = sns.color_palette('coolwarm')

if pie_axis:
    pie_fig = plt.figure(figsize=(2,2))

    pie_ax = pie_fig.add_subplot(111)

    sub_data_cat = data_cat[pie_axis]

    pie_ax.pie(data_cat[pie_axis].value_counts(), startangle=90, #cmap='plasma', ax=pie_ax, 
                       autopct='%.1f', colors=colors, textprops={'fontsize': 4}
                       )
    
    pie_ax.set_title("Blood Measurements by Age", fontsize=4);



################ Dynamic Bar Chart ##################


st.sidebar.markdown("### Blood Measurements (Bar Chart)")

gp_target = data.groupby("target").mean()
bar_axis = st.sidebar.multiselect(label="Average Measures for High and Low Risk of HA",
                                  options=measurements,
                                  default=measurements)

if bar_axis:
    bar_fig = plt.figure(figsize=(12,8))

    bar_ax = bar_fig.add_subplot(111)

    sub_gp_target = gp_target[bar_axis]

    sub_gp_target.plot.bar(alpha=0.8, cmap='plasma',
                           ax=bar_ax, title="Blood Measurements by Risk of Heart Attack", rot=0)
    
    labels = [item.get_text() for item in bar_ax.get_xticklabels()]
    labels[0] = 'Low'
    labels[1] = 'High'
    bar_ax.set_xticklabels(labels)
    bar_ax.set_xlabel('Risk of Heart Attack')
    bar_ax.legend(loc='upper right');


else:
    bar_fig = plt.figure(figsize=(12,8))

    bar_ax = bar_fig.add_subplot(111)

    sub_gp_target = gp_target[measurements]

    sub_gp_target.plot.bar(alpha=0.8, cmap='plasma',
                           ax=bar_ax, title="Blood Measurements by Risk of Heart Attack", rot=0)
    #sns.barplot(#x='clarity', y='mean', 
                #data=sub_gp_target, ax=bar_ax,
                #title="Blood Measurements by Risk of Heart Attack", rot=0
                #alpha=0.8)
    
    labels = [item.get_text() for item in bar_ax.get_xticklabels()]
    labels[0] = 'Low'
    labels[1] = 'High'
    bar_ax.set_xticklabels(labels)
    bar_ax.set_xlabel('Risk of Heart Attack')
    bar_ax.legend(loc='upper right');


################# Histogram Logic ########################


st.sidebar.markdown("### Blood Measurements Distribution by Bins (Histogram)")

hist_axis = st.sidebar.multiselect(label="Histogram Ingredient", options=measurements, default=measurements)
bins = st.sidebar.radio(label="Bins :", options=[10,50,100], index=2)

if hist_axis:
    hist_fig = plt.figure(figsize=(12,8))

    hist_ax = hist_fig.add_subplot(111)

    sub_data = data[hist_axis]

    sub_data.plot.hist(bins=bins, alpha=0.7, ax=hist_ax, 
                       title="Distribution of Blood Measurements",
                       cmap='plasma')
    hist_ax.legend(loc='upper right');
    
else:
    hist_fig = plt.figure(figsize=(12,8))

    hist_ax = hist_fig.add_subplot(111)

    sub_data = data[measurements]

    sub_data.plot.hist(bins=bins, alpha=0.7, ax=hist_ax, 
                       title="Distribution of Blood Measurements",
                       cmap='plasma')
    hist_ax.legend(loc='upper right');


#################### Dynamic Bar Chart ##################################

st.sidebar.markdown("### Blood Measurements by Chest Pain Type (Bar Chart)")

gp_cp = data.groupby('cp')['trestbps', 'chol', 'thalach'].mean()
bar2_axis = st.sidebar.multiselect(label='Blood Measurements by Chest Pain Type',
                                 options=measurements, default=measurements)

if bar2_axis:
    bar2_fig = plt.figure(figsize=(12,8))

    bar2_ax = bar2_fig.add_subplot(111)

    sub_gp_target = gp_cp[bar2_axis]

    sub_gp_target.plot.bar(alpha=0.8, cmap='plasma',
                       ax=bar2_ax, title="Blood Measurements by Chest Pain Type", rot=0)
    
    bar2_ax.set_xlabel('Chest Pain Type')
    bar2_ax.legend(loc='upper right');


else:
    bar2_fig = plt.figure(figsize=(12,8))

    bar2_ax = bar2_fig.add_subplot(111)

    sub_gp_target = gp_cp[measurements]

    sub_gp_target.plot.bar(alpha=0.8, cmap='plasma',
                       ax=bar2_ax, title="Blood Measurements by Chest Pain Type", rot=0)
    
    bar2_ax.set_xlabel('Chest Pain Type')
    bar2_ax.legend(loc='upper right');


#################### Dynamic Line Chart ##################################

st.sidebar.markdown("### Blood Measurements by Age (Line Chart)")

gp_age = data.groupby('age')['trestbps', 'chol', 'thalach'].mean()
line_axis = st.sidebar.multiselect(label='Blood Measurements by Age',
                                 options=measurements, default=measurements)

if line_axis:
    line_fig = plt.figure(figsize=(12,8))

    line_ax = line_fig.add_subplot(111)

    sub_gp_target = gp_age[line_axis]

    sub_gp_target.plot(alpha=0.8, cmap='plasma',
                       ax=line_ax, title="Blood Measurements by Age", rot=0)
    
    line_ax.set_xlabel('Age')
    line_ax.legend(loc='upper right');


else:
    line_fig = plt.figure(figsize=(12,8))

    line_ax = line_fig.add_subplot(111)

    sub_gp_target = gp_age[measurements]

    sub_gp_target.plot(alpha=0.8, cmap='plasma',
                       ax=line_ax, title="Blood Measurements by Age", rot=0)
    
    line_ax.set_xlabel('Age')
    line_ax.legend(loc='upper right');



#####################################################


########## Thalac and CA bar plot ##################


gp_ca = data.groupby(['restecg'])['thalach'].mean()

bar_fig = plt.figure(figsize=(12,8))

bar_ax = bar_fig.add_subplot(111)

gp_ca.plot.bar(alpha=0.8, ax=bar_ax, color='r', 
               title='Average Max Heart Rate by Resting ECG', 
               rot=0);
bar_ax.set_xlabel('resting ECG results from low to high')


##################### Layout Application ##################

container1 = st.container()
col1, col2, col3 = st.columns(3)

with container1:
    with col1:
        scatter_fig
#    with col2:
#        pie_fig
#    with col3:
#        pie_fig    

container2 = st.container()
col4, col5, col6 = st.columns(3)

with container2:
    with col4:
        hist_fig
    with col5:
        bar2_fig
#    with col6:
#        bar2_fig        
        
container3 = st.container()
col7, col8, col9 = st.columns(3)

with container3:
    with col7:
        line_fig
    with col8:
        bar_fig
#    with col9:
#        bar2_fig  
        
container4 = st.container()
col10, col11, col12 = st.columns(3)

with container4:
#    with col10:
#        line_fig
#    with col11:
#        bar_fig
    with col12:
        pie_fig