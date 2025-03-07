Hotel Data Extraction from Hotels.ng

This project is a web scraping script that extracts hotel data from the Hotels.ng website for hotels located in Abia State, Nigeria. The extracted data includes hotel names, addresses, cities, states, prices, ratings, facilities, and likes.

Table of Contents
Overview

Features

Technologies Used

Setup and Installation

Usage

Output

Contributing

License

Overview
The script uses Python to scrape hotel data from the Hotels.ng website. It retrieves information such as:

Hotel Name

Address

City

State

Price

Rating

Facilities

Likes

The extracted data is stored in a list of dictionaries and can be further processed or exported to a CSV file for analysis.

Features
Web Scraping: Extracts hotel data from the Hotels.ng website.

Data Parsing: Parses HTML content to extract relevant hotel details.

Error Handling: Handles missing data gracefully (e.g., if a hotel has no rating or facilities).

Pandas Integration: Can convert the extracted data into a Pandas DataFrame for further analysis.

Technologies Used
Python: The programming language used for scripting.

Requests: For making HTTP requests to the Hotels.ng website.

BeautifulSoup: For parsing HTML content and extracting data.

Pandas: For data manipulation and analysis (optional).

Setup and Installation
Clone the Repository:

bash
git clone https://github.com/your-username/DE_task_data-extraction.git
cd DE_task_data-extraction
Set Up a Virtual Environment (optional but recommended):

bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies:

bash
pip install -r requirements.txt
The requirements.txt file should include:

requests
beautifulsoup4
pandas
Run the Script:

bash
python hotels.py
Usage
Run the Script:
Execute the script to scrape hotel data:

bash
python hotels.py
View the Output:
The script will print the extracted hotel data to the console. You can modify the script to save the data to a CSV file or a database.

Export to CSV (optional):
To export the data to a CSV file, add the following code at the end of the script:

python
import pandas as pd
df = pd.DataFrame(all_hotels)
df.to_csv('hotels_data.csv', index=False)

Output
The script outputs a list of dictionaries, where each dictionary contains details about a hotel. 
