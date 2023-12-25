# Web Image Scraper

## Description:

WebImageScraper is a Python project designed to download images from a web page based on user-defined keywords. In this example, the project focuses on extracting images related to Steve Jobs, Bill Gates, Elon Musk from the web. The program recursively traverses links, identifies images with specified keywords in their alt attributes, and saves them to a local directory.

To use the project, clone the repository and modify the example usage section with your preferred URL, output directory, and keywords. Ensure compliance with the terms of service of the website you are scraping, and consider contributing improvements to benefit the communit

## Code Explanation:

### Dependencies:

```python
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
```

- `requests`: Used to send HTTP requests.
- `BeautifulSoup`: A library for parsing HTML content.
- `os`: Provides functionality for interacting with the operating system.
- `urljoin`: Used to join URLs.

### Function `download_images_with_keywords`:

- Downloads images from a specified URL based on given keywords.
- Creates an output directory for storing downloaded images.
- Initiates a recursive function to explore links and extract images.

### Recursive Function `download_images_internal`:

```python
# Follow links recursively
for link in soup.find_all('a', href=True):
    next_url = urljoin(current_url, link['href'])
    download_images_internal(next_url, depth + 1)
```

- Checks depth and visited URLs to control the recursion.
- Retrieves HTML content from the current URL.
- Searches for image tags (`<img>`) with alt attributes containing any of the specified keywords.
- Downloads and saves identified images to the output folder with unique filenames based on keywords and index.
- Recursively follows links found on the page.

### Example Usage:

```python
url_to_scrape = 'https://en.wikipedia.org/wiki/Elon_Musk'
output_directory = 'downloaded_elon_musk_images'
search_keywords = ['elon musk', 'elon', 'musk']

download_images_with_keywords(url_to_scrape, output_directory, search_keywords)
```
