import requests
from bs4 import BeautifulSoup
import csv

# URL and form data
url = "https://www.biseb.edu.pk/result-search.php?id=49&rd_id=0"
data = {
    'roll_number': '400001',
    'action': 'by_id'
}

# Send a POST request with the form data
response = requests.post(url, data=data)

# Parse the HTML content of the response
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table you want to extract data from
table = soup.find('table', class_='table')

# Extract column names from the table header
columns = [th.text.strip() for th in table.find('tr').find_all('th')]

# Extract and save data from the table rows to a CSV file
with open('ssc_12th_annual_1_2023.csv', 'a', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the column names as the header
    # csv_writer.writerow(columns)
    i = 414746
    fails = 0
    while True:
      data = {
        'roll_number': f'{i}',
        'action': 'by_id'
      }

      # Send a POST request with the form data
      response = requests.post(url, data=data)
      if "Sorry! Result Not Found, Please Try Again" in response.text:
          fails = fails+1
          if fails==5:
            break
      # Parse the HTML content of the response
      soup = BeautifulSoup(response.content, 'html.parser')

      # Find the table you want to extract data from
      table = soup.find('table', class_='table')

      # Extract and write data from the table rows

      if(table != None):
        print(table)
        for row in table.find_all('tr')[1:]:
            values = [td.text.strip() for td in row.find_all('td')]
            csv_writer.writerow(values)
      i = i+1

print("Data saved to 'ssc_12th_annual_1_2023.csv'")
