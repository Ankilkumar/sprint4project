# sprint4project

Project Description

The tasks are: creating and managing python virtual environments, developing a web application, and deploying it to a cloud service that will make it accessible to the public.

Data

Dataset was taken form following website:
https://catalog.data.gov/dataset/real-estate-sales-2001-2018

The data was then reduced with following conditions:

1. Commercial properties was removed
2. Only columns listed below were kept since they were most relevent to analysis being performed
3. All null values were removed since it cannot be determined which property type was null value

Real_Estate_Sales_2001_2020

list_year:          year property was listed
date_recorded:      date when the property was recorded as sold
assessed_value:     how much the property was valued in USD at time of listing
town:               town in which property is recorded
sale_amount:        how much the property was sold in USD
residential_type:   type of residential property


Following analysis were done on data:

1. How many properties were sold each year by type of property
2. Average value of property sold per month each year (you can select if you want to only view properties valued below 500,000 USD)

The results can be found on following site:

https://real-estate-sales-connecticut-2001-2020.onrender.com


Instruction on how to run the app locally:

1. Pull latest version of the repository.
2. Run "streamlit run app.py" from root directory of repository. If you dont have streamlit installed, run "pip install streamlist" before running the app.py using streamlit.
3. If displayed link doesn't open the web app, enter "http://0.0.0.0:10000/" in your browser to see the result of the app.