import os
import requests
import zipfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scraper():
    url = 'https://terrabrasilis.dpi.inpe.br/downloads/'
    download_folder = './data2'
    os.makedirs(download_folder, exist_ok=True)

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headlessly if desired

    # Initialize WebDriver with ChromeDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Open the page
    driver.get(url)

    try:
        # Wait and find the link by id 'file-download-2'
        link = driver.find_element(By.ID, 'file-download-2')

        # Get the JavaScript function parameter from the href
        js_download = link.get_attribute('href')
        if "javascript: download" in js_download:
            # Extract the URL within the JavaScript function
            file_path = js_download.split("'")[1]
            file_url = f'https://terrabrasilis.dpi.inpe.br{file_path}'

            # Specify the filename with .zip extension
            filename = f"{file_path.split('/')[-1]}.zip"
            full_file_path = os.path.join(download_folder, filename)

            # Download the ZIP file
            print(f"Downloading {filename}...")
            file_response = requests.get(file_url)

            # Save the ZIP file locally
            with open(full_file_path, 'wb') as f:
                f.write(file_response.content)

            print(f"Saved {filename} to {full_file_path}")

            # Extract the ZIP file
            with zipfile.ZipFile(full_file_path, 'r') as zip_ref:
                zip_ref.extractall(download_folder)
            print(f"Extracted {filename} to {download_folder}")

            # Delete the ZIP file after extraction
            os.remove(full_file_path)
            print(f"Deleted {filename} after extraction.")

        else:
            print("Unable to parse JavaScript download URL.")
    except Exception as e:
        print("Link with id 'file-download-2' not found.")
        print("Error:", e)
    finally:
        driver.quit()

scraper()