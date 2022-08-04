import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit.legacy_caching.caching import cache

# st.title("COVID-19")
# nav = st.sidebar.radio("Navigation", ["Home", "All Data", "Specific Data", "Specific Graph"])
side_var = st.sidebar.selectbox(
    "Home", ["Welcome","Vaccination", "COVID-19", "Excel", "Latest Data"])

# Welcome
if side_var == "Welcome":
    st.title("Welcome to IT Project")
# Vaccination
if side_var == "Vaccination":
    st.title("Vaccination Data")
    data = pd.read_csv("https://covid19.who.int/who-data/vaccination-data.csv")
    # st.success("File Uploaded Successfully !")
    list_of_column = list(data.columns)
    list_of_country = list(data[list_of_column[0]])
    nav = st.sidebar.radio(
        "Navigation", ["Home", "All Data", "Specific Data", "Specific Graph"])
    if nav == "Home":
        st.title("Home")
    if nav == "All Data":
        st.title("All Data")
        st.write(data)
    if nav == "Specific Data":
        st.title("Specific Data")
        selected_country = st.multiselect("Select Country", list_of_country)

        for country in selected_country:
            st.header(country)
            dic = {}
            index_of_country = list_of_country.index(country)
            no_of_column = len(list_of_column)
            for i in range(no_of_column):
                lis = list(data[list_of_column[i]])
                temp = {list_of_column[i]: lis[index_of_country]}
                dic.update(temp)
            st.write(dic)
    if nav == "Specific Graph":
        st.title("Specific Graph")
        country_for_piechart = st.multiselect(
            "Select Country", list_of_country)
        input_for_comparison = st.selectbox(
            "Input for Comparison", list_of_column)

        y_axis_list = []
        for country in country_for_piechart:
            index_of_country = list_of_country.index(country)
            y_axis_list.append(
                int(data[input_for_comparison][index_of_country]))

        fig1, var1 = plt.subplots()
        var1.bar(country_for_piechart, y_axis_list)
        st.header("Comparison Between Countries")
        plt.suptitle('Bar Graph')
        st.pyplot(fig1)

        fig2, var2 = plt.subplots()
        var2.pie(y_axis_list, labels=country_for_piechart)
        plt.suptitle('Pie Chart')
        plt.legend()
        st.pyplot(fig2)

# COVID-19
if side_var == "COVID-19":
    st.title("COVID-19 Data")
    file = st.sidebar.file_uploader("Upload a csv file")

    # file = st.file_uploader("Upload a file")
    if file:

        data = pd.read_csv(file)
        st.success("File Uploaded Successfully !")
        list_of_column = list(data.columns)
        list_of_country = list(data[list_of_column[0]])
        nav = st.sidebar.radio(
            "Navigation", ["Home", "All Data", "Specific Data", "Graph"])
        if nav == "Home":
            st.title("Home")
        if nav == "All Data":
            data_var = st.sidebar.radio("Select One", ["Excel", "Latest"])
            if data_var == "Excel":
                st.title("All Data")
                st.write(data)
            if data_var == "Latest":
                _data = pd.read_csv(
                    "https://covid19.who.int/WHO-COVID-19-global-table-data.csv")
                st.write(data)
        if nav == "Specific Data":
            st.title("Specific Data")
            selected_country = st.multiselect(
                "Select Country", list_of_country)

            for country in selected_country:
                st.header(country)
                dic = {}
                index_of_country = list_of_country.index(country)
                no_of_column = len(list_of_column)
                for i in range(no_of_column):
                    lis = list(data[list_of_column[i]])
                    temp = {list_of_column[i]: lis[index_of_country]}
                    dic.update(temp)
                st.write(dic)
        if nav == "Graph":
            st.title("Graph")
            country_for_piechart = st.multiselect(
                "Select Country", list_of_country)
            input_for_comparison = st.selectbox(
                "Input for Comparison", list_of_column)

            y_axis_list = []
            for country in country_for_piechart:
                index_of_country = list_of_country.index(country)
                y_axis_list.append(
                    int(data[input_for_comparison][index_of_country]))

            graph_navigation = st.sidebar.radio(
                "Graphs", ["All Graph", "Bar Graph", "Pie Chart", "Scatter Plot"])
            if graph_navigation == "All Graph":
                # Bar Graph
                fig1, var1 = plt.subplots()
                var1.bar(country_for_piechart, y_axis_list)
                st.header("Comparison Between Countries")
                plt.suptitle('Bar Graph')
                st.pyplot(fig1)

                # Pie Chart
                fig2, var2 = plt.subplots()
                var2.pie(y_axis_list, labels=country_for_piechart)
                plt.suptitle('Pie Chart')
                plt.legend()
                st.pyplot(fig2)

                # Scatter Plot
                fig3, var3 = plt.subplots()
                var3.scatter(country_for_piechart, y_axis_list)
                plt.suptitle("Scatter Graph")
                plt.legend()
                st.pyplot(fig3)

            if graph_navigation == "Bar Graph":
                fig1, var1 = plt.subplots()
                var1.bar(country_for_piechart, y_axis_list)
                st.header("Comparison Between Countries")
                plt.suptitle('Bar Graph')
                st.pyplot(fig1)
            elif graph_navigation == "Pie Chart":
                fig2, var2 = plt.subplots()
                var2.pie(y_axis_list, labels=country_for_piechart)
                plt.suptitle('Pie Chart')
                plt.legend()
                st.pyplot(fig2)
            elif graph_navigation == "Scatter Plot":
                fig3, var3 = plt.subplots()
                var3.scatter(country_for_piechart, y_axis_list)
                plt.suptitle("Scatter Graph")
                plt.legend()
                st.pyplot(fig3)

# Excel
if side_var == "Excel":
    st.title("COVID-19")
    # function to read data from a excel file return a dictionary having key:value pair as "region:population"
    # where "population" is the count of people vaccinated.

    file = st.sidebar.file_uploader("Upload a Excel Sheet")
    if file:
        def VaccinationStatus():
            df = pd.read_excel(file)
            dictionary = dict()

            for ind in df.index:
                if df['REGION'][ind] not in dictionary:
                    dictionary[df['REGION'][ind]] = 0

            for ind in df.index:
                if df['REGION'][ind] in dictionary:
                    if(df['STATUS'][ind] == 'Y'):
                        dictionary[df['REGION'][ind]] += 1

            return dictionary

        # function to read data from a excel file return a dictionary having key:value pair as "region:population"
        # where "population" is the count of people not vaccinated.

        def notVaccinated():
            df = pd.read_excel(file)
            dictionary = dict()

            for ind in df.index:
                if df['REGION'][ind] not in dictionary:
                    dictionary[df['REGION'][ind]] = 0

            for ind in df.index:
                if df['REGION'][ind] in dictionary:
                    if(df['STATUS'][ind] == 'N'):
                        dictionary[df['REGION'][ind]] += 1

            return dictionary

        # function to display the bar graph having arguments dict(region : population), str(title of graph) & col(color of graph)

        def barGraph(dict, str, col):
            names = list(dict.keys())
            status = list(dict.values())

            fig1, var1 = plt.subplots()
            var1.bar(names, status, color=col)
            plt.title(str)
            plt.xlabel("Region")
            plt.ylabel("Status")
            plt.grid(True)
            # plt.show()
            st.pyplot(fig1)

            # fig1, var1 = plt.subplots()
            # var1.bar(country_for_piechart, y_axis_list)
            # st.header("Comparison Between Countries")
            # plt.suptitle('Bar Graph')
            # st.pyplot(fig1)

        # function to display the scatter plot having arguments dict(region : population), str(title of graph) & col(color of graph)

        def scatterPlot(dict, str, col):
            names = list(dict.keys())
            status = list(dict.values())

            fig2, var2 = plt.subplots()
            var2.scatter(names, status, c=col, s=100)
            plt.title("Vaccinated")
            # plt.show()
            st.pyplot(fig2)

        # function to display the pie chart having arguments dict(region : population) & str(title of graph)

        def pieChart(dict, str):
            names = list(dict.keys())
            status = list(dict.values())

            fig3, var3 = plt.subplots()
            var3.pie(status, labels=names)
            # plt.show()
            st.pyplot(fig3)

        st.title("VACCINATION STATUS")
        radio_variable = st.sidebar.selectbox(
            "Please, Select One", ["Population Vaccinated", "Population Not Vaccinated"])
        if radio_variable == "Population Vaccinated":
            inside_radio = st.sidebar.radio(
                "Please Select", ["Bar", "Pie", "Scatter"])
            vaccination_status = VaccinationStatus()
            if inside_radio == "Bar":
                barGraph(vaccination_status, "Vaccination Status", "g")
            elif inside_radio == "Pie":
                pieChart(vaccination_status, "Vaccination Status", "g")
            else:
                scatterPlot(vaccination_status, "Vaccination Status", "g")
        elif radio_variable == "Population Not Vaccinated":
            inside_radio = st.sidebar.radio(
                "Graphs", ["Bar", "Pie", "Scatter"])
            vaccination_status = notVaccinated()
            if inside_radio == "Bar":
                barGraph(vaccination_status, "Vaccination Status", "r")
            elif inside_radio == "Pie":
                pieChart(vaccination_status, "Vaccination Status")
            else:
                scatterPlot(vaccination_status, "Vaccination Status", "r")


# Latest Data
if side_var == "Latest Data":
    st.title("Latest COVID-19 Data")

    latest_var = st.sidebar.radio("Latest Data", [
                                  "Daily Cases By Date", "Latest Counts of Cases", "Vaccination Data", "Vaccination metadata"])
    if latest_var == "Daily Cases By Date":
        st.header("Daily cases and deaths by date reported to WHO")
        daily = pd.read_csv(
            "https://covid19.who.int/WHO-COVID-19-global-data.csv")
        st.write(daily)

    if latest_var == "Latest Counts of Cases":
        st.header("Latest reported counts of cases and deaths")
        counts = pd.read_csv(
            "https://covid19.who.int/WHO-COVID-19-global-table-data.csv")
        st.write(counts)

    if latest_var == "Vaccination Data":
        st.header("Vaccination data")
        vac_data = pd.read_csv(
            "https://covid19.who.int/who-data/vaccination-data.csv")
        st.write(vac_data)

    if latest_var == "Vaccination metadata":
        st.header("Vaccination metadata")
        meta = pd.read_csv(
            "https://covid19.who.int/who-data/vaccination-metadata.csv")
        st.write(meta)
