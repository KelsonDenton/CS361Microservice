# CS361Microservice
A wikipedia text scraper that uses the BeautifulSoup python package to scrape descriptions from wikipedia pages

Install package in your project and run the wiki_scraper.py file. When running it will look for an entry into a wiki.json file of:\n
{"url": <url of wikipedia page>, "title": <title of section of text you want>}\n
The same wiki.json file will then be updated with: \n
  {"text": <text from wikipedia article title>}

