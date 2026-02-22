# WordPress Product Scraper

A Python script to scrape all products from a WordPress/WooCommerce site and save them into a TXT file.
This tool works for a single category or the entire shop, automatically iterating through all pagination pages.

## Features

- Crawl all pages of a WordPress/WooCommerce store
- Extract product names
- Save output in a clean TXT file
- Easy to modify for any WordPress site

## Installation

1. Clone this repository:

git clone https://github.com/amirreza-saeedabadi/wordpress-product-scraper.git
cd wordpress-product-scraper

2. Install required Python packages:

pip install -r requirements.txt

## Usage

1. Open scraper.py and set the base URL of your store:

base_url = "https://example.com/product-category/towel"

2. Run the script:

python scraper.py

3. The script will create products.txt containing all product names.

## Project Structure

wordpress-product-scraper/
- scraper.py          # Main Python scraper script
- requirements.txt    # Dependencies
- README.md           # This file
- .gitignore          # Ignore unnecessary files
- products.txt        # Output file (auto-generated)

## Notes

- Respect the site's robots.txt and usage policies.
- Avoid sending too many requests too quickly; consider adding time.sleep() for large stores.
- Works best with standard WooCommerce structures. Custom themes may require CSS selector adjustment.

## Related Topics

- Python
- Web Scraping
- WooCommerce
- Automation

## Author

Amirreza Saeedabadi – Building automation tools for WordPress & WooCommerce ⚡
https://github.com/amirreza-saeedabadi
