from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import base64
import os
import time

def html_to_single_page_pdf1(input_html_path, output_pdf_path):
    chrome_options = Options()
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=chrome_options)

    file_url = 'file:///' + os.path.abspath(input_html_path).replace("\\", "/")
    driver.get(file_url)
    time.sleep(1)  # Let the page load fully

    # Get the height of the rendered HTML in pixels
    scroll_height = driver.execute_script("return document.body.scrollHeight")

    # Chrome uses inches for paperHeight and paperWidth (1 inch = 96 px)
    page_width_in_inches = 8.5  # Standard A4 width or you can adjust
    page_height_in_inches = scroll_height / 96.0  # Convert pixels to inches

    pdf = driver.execute_cdp_cmd("Page.printToPDF", {
        "printBackground": True,
        "marginTop": 0,
        "marginBottom": 0,
        "marginLeft": 0,
        "marginRight": 0,
        "paperWidth": page_width_in_inches,
        "paperHeight": page_height_in_inches,
        "preferCSSPageSize": False,
        "scale": 1
    })

    with open(output_pdf_path, "wb") as f:
        f.write(base64.b64decode(pdf['data']))

    driver.quit()
    print(f" PDF saved to {output_pdf_path} — fitted on one continuous page.")

def html_to_single_page_pdf(input_html_path, output_pdf_path):
    chrome_options = Options()
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=chrome_options)

    file_url = 'file:///' + os.path.abspath(input_html_path).replace("\\", "/")
    driver.get(file_url)
    time.sleep(1)

    pdf = driver.execute_cdp_cmd("Page.printToPDF", {
        "printBackground": True,
        "marginTop": 0,
        "marginBottom": 0,
        "marginLeft": 0,
        "marginRight": 0,
        "paperWidth": 9,
        "paperHeight": 8,  
        "scale": 0.7,      
        "preferCSSPageSize": False
    })

    with open(output_pdf_path, "wb") as f:
        f.write(base64.b64decode(pdf['data']))

    driver.quit()
    print(f" PDF saved to {output_pdf_path} — scaled to fit on one page.")

