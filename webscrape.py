# IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests

# REQUEST WEBPAGE AND STORE IT AS A VARIABLE
page_to_scrape = requests.get("https://codeforces.com/problemset")

# USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

# FIND ALL THE ROWS WITH CLASS 'dark'
rows = soup.findAll("tr")

# Create a list to store the rows with their modified text
formatted_rows = []

for row in rows:
    # Replace newline characters and remove leading/trailing whitespaces
    row_text = row.text.replace('\n', '').strip()
    formatted_rows.append(row_text)

# Sort the rows alphabetically based on the name
formatted_rows.sort(key=lambda x: x.split()[0])

# Print the sorted rows with the specified styles
for row_text in formatted_rows:
    print(row_text)
