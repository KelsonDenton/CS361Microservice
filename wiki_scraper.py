# Source: Geeks for Geeks - Web scraping from Wikipedia using Python – A Complete Guide
# Accessed 4/19/22
# URL: https://www.geeksforgeeks.org/web-scraping-from-wikipedia-using-python-a-complete-guide/

# import required modules
import time

from bs4 import BeautifulSoup
import requests
import json


def get_text_under(url, title_name):
    """
    Parameters of url and title_name are used to find information at wikipedia url and under title.
    """
    # get URL
    page = requests.get(url)
    # scrape webpage
    soup = BeautifulSoup(page.content, 'html.parser')
    headlines = soup.find_all('span', {"class": "mw-headline"})
    for headline in headlines:
        for title in headline:
            if title == title_name:  # correct title was found
                # get the paragraph by navigating back to the header then to sibling paragraph
                header = headline.find_parent('h2')
                paragraphs = []
                paragraph = header.find_next_sibling()
                # print paragraph until encounters next section marked by h2
                while paragraph.name != 'h2':
                    paragraphs.append(paragraph)
                    paragraph = paragraph.find_next_sibling()
                # create easily readable form
                return_str = ""
                for paragraph in paragraphs:
                    return_str += paragraph.get_text()
                    return_str += "\n"
                return return_str
    # title was not found on page (error message)
    return f'Title {title_name} does not exist'  


while True:  # continuously runs while file is run to read and update wiki.json
    try:
        try:
            with open('wiki.json', 'r') as read_json:  # open json file for reading
                json_file = json.load(read_json)
                description = get_text_under(json_file["url"], json_file["title"])  # use get_text_under with JSON data
                desc_dict = {"text": description}
                json_object = json.dumps(desc_dict)
        finally:
            read_json.close()
        try:
            with open('wiki.json', 'w') as write_json:  # write resulting data to JSON file
                write_json.write(json_object)
        finally:
            write_json.close()
    except:
        pass
