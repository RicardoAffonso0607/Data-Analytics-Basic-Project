# Data Analytics Basic Project

## Overview
This is a simple data analytics project implemented in Python. The project focuses on analyzing and visualizing data using the Plotly and Pandas libraries.

To contextualize, in the "cancellations.csv" file, there is a database with 881.666 rows. I had to analyze this data and find why people were canceling a service so much (around 56,7%).

## Libraries used
- [Plotly](https://plotly.com/): Used for creating interactive and visually appealing plots and charts.
- [Pandas](https://pandas.pydata.org/): Used for data manipulation and analysis.

## How do I solved it?
FIrst I tried to find patterns in the people who were canceling. Using the Pandas library I discovered that all the people that had the "Monthly" plan cancelled their accounts.

<img src="https://github.com/RicardoAffonso0607/Data-Analytics-Basic-Project/assets/127418054/57fbd782-7911-4d1d-969c-9ac221e20758" />

To facilitate the data view, I utilized the Plotly library, and those were the more important graphics generated:

<img src="https://github.com/RicardoAffonso0607/Data-Analytics-Basic-Project/assets/127418054/b9fd4ba3-db29-4056-b921-c71fb36880b2" />

<img src="https://github.com/RicardoAffonso0607/Data-Analytics-Basic-Project/assets/127418054/04c246f3-fbcc-40bd-8629-088bbf853ef7" />

<img src="https://github.com/RicardoAffonso0607/Data-Analytics-Basic-Project/assets/127418054/d6fc2a1e-8080-4640-8e33-95ec803c44a1" />

Visualizing these graphics, I could conclude that most of the people who were canceling tried to call the assistance more than 5 times, or the service delayed more than 20 days to work. Another curious thing is that people over 50
years old were canceling their plans.

Taking these people of the database, I reached 12,1% of cancellations.

## How to Run

1. Clone the repository:
   ````bash
   git clone https://github.com/RicardoAffonso0607/Data-Analytics-Basic-Project
2. Make sure that you've already installed the Pandas and SciKit Learn libraries:
   ```bash
   pip install pandas
   pip install plotly
3. Unzip the files
4. Run the Project:
   ```bash
   python main.py # Windows
   python3 main.py # Linux

## Considerations

This little project was interesting to understand how to manage databases.

With the information I gatered, I could find the main reasons people were canceling this service, and show what had to be done.

## Acknowledgments

Thank Hashtag Programação for making the database available and to guide me in this project. Please follow them in YouTube: https://www.youtube.com/@HashtagProgramacao

