1) DESCRIPTION - 
    The package list you provided includes a broad range of libraries for data science, machine learning, web development, and geospatial analysis. Numpy, pandas, scikit-learn, tensorflow, and keras are key for data manipulation and machine learning, with pandas offering powerful data structures and tensorflow and keras enabling deep learning workflows. For visualization, matplotlib, seaborn, and altair provide tools for creating interactive and static plots, while geopandas, shapely, and pyproj help with geospatial data analysis and visualization.

    Web scraping and automation are handled by beautifulsoup4, requests, and selenium, while flask is a lightweight web framework for building web applications. Additionally, tools like pytest and tox support testing and automation, and joblib helps with saving and loading models efficiently. This collection of libraries is essential for tackling a wide array of tasks, from data analysis and visualization to web scraping and application development.

2) INSTALLATION - 
    1) Download data into the the main DETER_DATA_ANALYSIS-MAIN folder from 
        https://gtvault-my.sharepoint.com/:f:/g/personal/aram43_gatech_edu/Eu-me5nj565FoQ4dAhXyDM8B5NeJJe4fKNtmWLGHK2wIWQ?e=2ZEu16
    2) (Recommended) Create a virtual environment for python version 3.12.4 using the command :-
        'python3 -m venv .<name_of_environment>' and activate the environment.
    2) To install the packages run the following command on terminal/command prompt:-
        'pip install -r requirements.txt'
    (Please refer to the folder tree given below to ensure the folders are added to the right locations)

3) EXECUTION - 
    1) cd into the Notebooks folder Run scraper_deter.py
    (Disclaimer: If the bot does not run due to the website being down, download the data2 folder from https://gtvault-my.sharepoint.com/:f:/g/personal/aram43_gatech_edu/EgxHIxrRwcBOuhYw_2R3OPoBzO3Nk7MQoyfXSX4t-KA0lQ?e=sSmNLZ into the Notebooks folder)
    2) Run all cells of the notebook Map_Generation.ipynb from 
    3) Run all cells of the notebook Graph_Generation.ipynb
    4) Run the following command on terminal
            streamlit run app.py

4) DEMO VIDEO - 
5) FOLDER TREE 
    .
    ├── app.py
    ├── data
    ├── Images
    ├── Notebooks
    │   ├── data2
    │   ├── data2.zip
    │   ├── future_preds.csv
    │   ├── Graph_Generation.ipynb
    │   ├── Map_Generation.ipynb
    │   ├── merged_predictions.csv
    │   ├── merged_predictions_with_future.csv
    │   ├── prediction.ipynb
    │   ├── requirements.txt
    │   ├── scraper_deter.py
    │   └── scraper.ipynb
    ├── README.md
    ├── requirements.txt
    ├── texts
    ├── tree.txt
    └── Visualizations
        └── DETER
            ├── Graphs
            └── Maps