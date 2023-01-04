from selenium import webdriver
from selenium.webdriver.safari.options import Options as SafariOptions
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

options = SafariOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Safari(options=options)

browser.get("https://www.indeed.com/jobs?q=python&limit=50")
