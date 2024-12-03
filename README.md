# Web Crawler with Stylish Interface

This Python script is a simple web crawler with a stylish banner and aesthetic console output. It fetches web pages, extracts links, and traverses them up to a specified depth.

## Features
- **Recursive Crawling**: Starts from a given URL and crawls linked pages up to a configurable depth.
- **Beautiful Output**: Displays a visually appealing banner using the `pystyle` library.
- **Error Handling**: Handles HTTP errors gracefully with custom error messages.
- **Interactive Input**: Prompts the user for the starting URL.

## How It Works
1. Fetches the HTML content of a given page using `requests`.
2. Extracts all valid links on the page using `BeautifulSoup`.
3. Recursively visits each link, avoiding already visited URLs.
4. Displays the current URL being processed in a styled format.

## Usage
1. Run the script.
2. Enter a starting URL when prompted.
3. View the crawler in action as it navigates through the links.
