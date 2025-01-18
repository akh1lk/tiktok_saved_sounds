# TikTok Saved Sounds Downloader

In honor of TikTok getting banned, I decided to learn webscraping and make a Python script that automates the extraction of favorite sound links from TikTok's User Data. Using Selenium and BeautifulSoup, it is able to navigate TikTok's complicated JavaScript-based redirects to retrieve direct audio URLs.

If you're curious, I've posted some of my saved sounds up from Dec 2024 until now—if TikTok's CDN is still accessible.

## Overview

The script was created to address the challenge of scraping content from TikTok’s JavaScript-heavy pages. By automating browser interactions with Selenium and parsing the fully loaded HTML using BeautifulSoup, it extracts relevant metadata (i.e. audio `src` links) from dynamically rendered content.

## Challenges

- **JavaScript Redirects**: TikTok relies heavily on JavaScript to load and redirect pages, making traditional scraping methods ineffective.
- **Dynamic Content**: The script had to ensure the page was fully rendered before attempting to locate the required elements.

## Disclaimer

**This script is for educational purposes only.** Scraping websites may violate their Terms of Service, and any user should review TikTok’s TOS ([link here](https://www.tiktok.com/legal/terms-of-service)) before using this tool. I take no responsibility for misuse of this software or any consequences arising from its use. Always use responsibly.
