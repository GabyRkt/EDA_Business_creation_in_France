# EDA - Business creation in France (2012 - 2024)
This project is an exploratory data analysis (EDA) on business creation in France between 2012 and 2024. It uses INSEE public data to examine how the number of new businesses have evolved over time and which demographic or structural components contribute most to this evolution.

Data source : https://www.data.gouv.fr/datasets/creations-dentreprises-individuelles-unites-legales/


## Objectives
The goal of this project is to explore how business creation has evolved in France over the period 2012–2024. The analysis focuses on:
- Describing the overall evolution of new businesses over time.
- Comparing business creation across gender and age groups.
- Examining differences between different legal forms.
- Identifying which sectors account for the largest share of new businesses.
- Summarizing the results in an interactive Power BI dashboard.
  
## Key findings
From the analysis, several consistent patterns emerge:
- The number of new businesses has nearly doubled between 2012 and 2024.
- Most of this increase comes from the rise of micro-entrepreneurs, who represent more than 80% of new businesses in 2024.
- Entrepreneurs under 30 years old show the fastest growth and now make up close to 40% of new businesses in 2024.
- The gender gap remains quite stable over the period : around 40% women and 60% men.
- A small number of service-oriented sectors account for most of the increase, particularly administrative support services, commerce, construction, and transport.

## Data components
This section summarizes the main steps used to prepare, clean, and structure the data for analysis and reporting.
- Raw Data Ingestion: Loading and processing data from INSEE's public datasets in a Jupyter Notebook using Python.
- Data cleaning: Basic quality checking to identify missing values, incorrect data types, and other initial inconsistencies.
- Metadata management : Joining metadata to the dataset to add descriptive labels to the original coded variables.
- Exploratory visualization & Insight: Generating graphs in the notebook to understand key trends.
- Clean data generation : Exporting the clean dataset as the definitive source for analysis in Power BI.
- Power BI dashboard : Importing the clean dataset into Power BI to build interactive visuals and KPI summaries.

## Repository structure 
├── images/ --------------- Screenshots

├── EDA_dashboard.pbix ---- Power BI dashboard

├── EDA_project.ipynb ----- Full Python EDA

├── README.md ------------- Documentation

└── data.zip -------------- Raw INSEE datasets

## Conlusion
The analysis shows that the rise in business creation in France over the last decade is driven by a few clear forces: the expansion of the micro-entrepreneur regime, the growing participation of younger founders, and the weight of a few group of service-oriented sectors. Despite this rapid growth, the overall structure of entrepreneurs remains fairly stable, especially in terms of gender and legal form.
