import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape

f = open("chemicals.txt", "r")
chem_props = open("chem_props.txt", "w+")
all_chemicals = f.read().split("\n")

for chemical in all_chemicals:
    # Make sure chemical leads to correct webpage, should be uppercase and multi-word should be separated by _
    print(chemical)
    url = 'https://en.wikipedia.org/wiki/' + chemical

    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Now you can extract data using BeautifulSoup methods
        # For example, print all the text content of <p> tags
        cleaned_text = ""
        for paragraph in soup.find_all('tr'):
            if "Molar mass" in paragraph.text or "Density" in paragraph.text or "Melting point" in paragraph.text or "Boiling point" in paragraph.text:
                cleaned_text = cleaned_text + paragraph.text
        chem_props.write(chemical)
        chem_props.write(cleaned_text)
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
