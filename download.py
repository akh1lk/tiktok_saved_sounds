from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
from bs4 import BeautifulSoup
import requests
import os

MAX_DOWNLOADS = 10 #CHANGE THIS TO WHAT YOU WANT

json_file_path = "./favorite_sounds.json"
output_directory = "./downloads"
os.makedirs(output_directory, exist_ok=True)

with open(json_file_path, "r") as file:
    data = json.load(file)

# Set up Selenium with optimized options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--disable-dev-shm-usage")


service = Service('/Users/akhilkagithapu/Downloads/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)


sound_links =  [item['Link'] for item in data.get('FavoriteSounds', [])]

redirected_urls = []

sound_links_cut = sound_links[4:MAX_DOWNLOADS]
try:
    for link in sound_links_cut:
        #Load Page w/ Initial JSON Link
        print(f"Processing: {link}")
        driver.get(link)
        final_url = driver.current_url
        #Redirect Number 1
        print(f"Final TikTok URL: {final_url}")
        #Load page to access tiktokcdn link
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        mse_div = soup.find('div', id='mse')
        if mse_div:
            video_tag = mse_div.find('video')
            if video_tag and video_tag.has_attr('src'):
                src = video_tag['src']
                print(f"Extracted: {src}")
                
                #Nice name for the download
                basename = final_url.split('/')[-1].split('?')[0]
                
                #save to mp3 file here
                response = requests.get(src, stream=True)
                if response.status_code == 200:
                    filename = os.path.join(output_directory, f"{basename}.mp3")
                    with open(filename, "wb") as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    print(f"Downloaded and saved: {filename}")
                else:
                    print(f"Failed to download the file from {src}. Status code: {response.status_code}")

except Exception as e:
    print(e)

driver.quit()