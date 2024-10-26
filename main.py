# importing required libraries

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# set page config
st.set_page_config(page_title="Data Visualizer",
                   layout="centered",
                   page_icon="📈")

# title
st.title("📈 Data Visualizer - Web App")

st.write("- Mekhma/MekhzZ")

working_dir = os.path.dirname(os.path.abspath(__file__))

datasets_path = f"{working_dir}/datasets"

files_list = [f for f in os.listdir(datasets_path) if f.endswith(".csv")]

selected_file = st.selectbox("select a file", files_list, index= None)

if selected_file:
    file_path = os.path.join(datasets_path,selected_file)
    df = pd.read_csv(file_path)

    columns = df.columns.to_list()

    col1, col2 = st.columns(2)

    with col1:
        st.write("")
        st.write(df.head())

    with col2:
        st.write("")
        x_axis = st.selectbox("select X-axis",options=columns, index=None)
        y_axis = st.selectbox("select Y-axis",options=columns, index=None)

        plot_list = ['Scatter plot','Bar plot']

        selected_plot = st.selectbox("select a plot to generate", plot_list, index=None)

    if st.button("Generate a plot"):

        fig,ax = plt.subplots(figsize=(12,8))

        if selected_plot == "Scatter plot" :
            st.write("")
            st.write(selected_plot)
            st.write("- Displays individual data points on a two-dimensional plane, where each point represents the values of two variables.")
            st.write("- Ideal for showing relationships or correlations between two variables.")
            plt.scatter(x=df[x_axis],y=df[y_axis])

        elif selected_plot == "Bar plot" :
            st.write("")
            st.write(selected_plot)
            st.write("- Uses rectangular bars to represent data values, with the length or height of each bar proportional to the value it represents.")
            st.write("- Best for comparing different categories or groups.")
            plt.bar(df[x_axis],df[y_axis])






        #adujsting label sizes
        ax.tick_params(axis='x', labelsize=10)  # Adjust x-axis label size
        ax.tick_params(axis='y', labelsize=10)  # Adjust y-axis label size

        # Adjust title and axis labels with a smaller font size
        plt.title(f'{selected_plot} of {y_axis} vs {x_axis}', fontsize=12)
        plt.xlabel(x_axis, fontsize=10)
        plt.ylabel(y_axis, fontsize=10)

        st.pyplot(fig)

