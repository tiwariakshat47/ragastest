# IMPORT LIBRARIES
#pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

# REQUEST WEBPAGE AND STORE IT AS A VARIABLE
page_to_scrape = requests.get("https://codeforces.com/problemset")

# USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

# FIND ALL THE ROWS WITH CLASS 'dark'
rows = soup.findAll("tr")

for row in rows:
    # Replace newline characters and remove leading/trailing whitespaces
    row_text = row.text.replace('\n', '').strip()
    print(row_text)

# Set a maximum number of prints


# for type, name in zip(types, names):
#     if print_count < max_prints:
#         print(name.text + " contains " + type.text)
#         print_count += 1
#     else:
#         break


#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'AUTHOR'
#AND STORE THE LIST AS A VARIABLE
# brawlers = soup.findAll(attrs={"class":"rarity4 text-center small mb-1"})
# # print(brawlers)
# names = [h3.text.strip() for h3 in soup.find_all('h3')]
# # print(names)
# #LOOP THROUGH BOTH LISTS USING THE 'ZIP' FUNCTION
# #AND PRINT AND FORMAT THE RESULTS
# print(winrates)
# i = 1
# for name in names:
#     if(i > 76):
#         break
#     print(name)
#     i = i+1
    
# for winrate, name in zip(winrates, names):
#     print(winrate.text + "-" + name)