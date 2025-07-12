import requests
from bs4 import BeautifulSoup
import json
from dateutil import parser
import re

URLS = [
    'https://www.udemycoupons.me/',
    'https://freecouponcode.co/udemy/',
    'https://coursescoupon.net/',
    'https://udemycoupon.site/',
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_udemycoupons_me(soup):
    courses = []
    # This is a placeholder selector. I will update it after inspecting the site.
    for item in soup.select('.item'):
        title_element = item.select_one('a.title')
        if not title_element:
            continue

        title = title_element.text.strip()
        url = title_element['href']

        description_element = item.select_one('.description')
        description = description_element.text.strip() if description_element else ''

        courses.append({
            'title': title,
            'url': url,
            'description': description,
            'source': 'udemycoupons.me'
        })
    return courses

def scrape_freecouponcode_co(soup):
    courses = []
    # This is a placeholder selector. I will update it after inspecting the site.
    for item in soup.select('.item'):
        title_element = item.select_one('a.title')
        if not title_element:
            continue

        title = title_element.text.strip()
        url = title_element['href']

        description_element = item.select_one('.description')
        description = description_element.text.strip() if description_element else ''

        courses.append({
            'title': title,
            'url': url,
            'description': description,
            'source': 'freecouponcode.co'
        })
    return courses

def scrape_coursescoupon_net(soup):
    courses = []
    # This is a placeholder selector. I will update it after inspecting the site.
    for item in soup.select('.item'):
        title_element = item.select_one('a.title')
        if not title_element:
            continue

        title = title_element.text.strip()
        url = title_element['href']

        description_element = item.select_one('.description')
        description = description_element.text.strip() if description_element else ''

        courses.append({
            'title': title,
            'url': url,
            'description': description,
            'source': 'coursescoupon.net'
        })
    return courses

def scrape_udemycoupon_site(soup):
    courses = []
    # This is a placeholder selector. I will update it after inspecting the site.
    for item in soup.select('.item'):
        title_element = item.select_one('a.title')
        if not title_element:
            continue

        title = title_element.text.strip()
        url = title_element['href']

        description_element = item.select_one('.description')
        description = description_element.text.strip() if description_element else ''

        courses..append({
            'title': title,
            'url': url,
            'description': description,
            'source': 'udemycoupon.site'
        })
    return courses


SCRAPER_MAP = {
    'www.udemycoupons.me': scrape_udemycoupons_me,
    'freecouponcode.co': scrape_freecouponcode_co,
    'coursescoupon.net': scrape_coursescoupon_net,
    'udemycoupon.site': scrape_udemycoupon_site,
}


def scrape_site(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    for domain, scraper_func in SCRAPER_MAP.items():
        if domain in url:
            return scraper_func(soup)

    return []


if __name__ == "__main__":
    all_courses = []
    for url in URLS:
        print(f"Scraping {url}...")
        courses = scrape_site(url)
        all_courses.extend(courses)
        print(f"Found {len(courses)} courses.")

    with open("courses.json", "w") as f:
        json.dump(all_courses, f, indent=2)

    print(f"\nScraping complete. Total courses found: {len(all_courses)}. Data saved to courses.json")
