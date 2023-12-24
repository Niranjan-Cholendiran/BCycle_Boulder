# Dock Watch

**About:**
Boulder BCycle is a popular and convenient transportation service in Boulder, Colorado. It offers electric bikes stationed throughout the city, providing a sustainable and efficient means of commuting. Notably, the service is tailored to the needs of the community, as it offers a unique benefit to students by providing them with free rides for up to one hour per trip. This student-friendly policy makes it an attractive choice for the University of Colorado Boulder's student population, who frequently utilize Boulder BCycle to commute between their residences and the university. The service plays a key role in the city's transport system, supporting sustainability goals and meeting student needs.

In Boulder's BCycle system, users often encounter reliability issues and struggle to predict bike station availability. This project, as part of the **CSCI 5502- Data Mining** course, **focuses on transforming the BCycle experience by dissecting usage patterns and calculating waiting times for each station**. By analyzing historical data and real-time inputs, we aim to provide users with valuable insights, enabling them to make informed decisions about when and where to pick up a bike. This initiative seeks to enhance the overall convenience and efficiency of the service, ultimately making BCycle an even more reliable and accessible mode of transportation for the Boulder community.

[Presentation Link](https://www.youtube.com/watch?v=QEBMTk4OsAE)

**Challenges**:
* **Data Availability**: Historical BCycle station status data is currently unavailable, as only real-time data is accessible. Consequently, we've been consistently collecting data in the background for our analysis.
* **Data Inconsistency**: The data is gathered continuously in the background using an AWS EC2 instance, but it occasionally experiences interruptions, causing breaks in the data. Additionally, external factors such as Colorado's Daylight Saving Time introduce additional complexity.
* **Data Sampling Limitations**: Numerous variables, such as public transport availability, weather conditions, and class schedules, influence BCycle usage. It's important to acknowledge that our data sample may not encompass all these influencing factors

**Approach Overview**
1. **Data Collection & Storage**: Collect live data from GBFS (General Bikeshare Feed Specification) and store it in an SQL server to maintain historical records.
2. **Data Preprocessing Pipeline**: Develop a data preprocessing pipeline to calculate additional variables and ensure data quality.
3. **Exploratory Data Analysis**: Conduct Exploratory Data Analysis (EDA) to identify and understand usage patterns within the dataset.
4. **Forecasting Model Development**: Build a predictive model to forecast waiting times for each station, utilizing the pre-processed data.
5. **Dashboard Creation**: Develop a Tableau dashboard to visualize real-time and historical bike station data along with live wait times.
6. **Cloud Deployment**: Deploy the Tableau dashboard, forecasting model, data preprocessing code, and data collection code to a cloud platform.
7. **Automation**: Automate the entire data collection, preprocessing, modeling, and dashboard updating processes to execute them based on a trigger point within the dashboard.
