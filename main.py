from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.get("https://kr.indeed.com/jobs?q=python&limit=50")

soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_ = "jobsearch-ResultsList")
jobs = job_list.find_all("li", recursive = False)

results = []

for job in jobs:
    zone = job.find("div", class_ = "mosaic-zone")
    if zone == None:
        anchor = job.select_one("h2 a") # find("h2") && find("a")
        title = anchor["aria-label"]
        link = anchor["href"]
        company = job.find("span", class_ = "companyName")
        company_loc = job.find("div", class_ = "companyLocation")

        job_data = {
            "link": f"https://kr.indeed.com/jobs?q=python&limit=50{link}",
            "company": company.string,
            "location": company_loc.string,
            "position": title
        }
        results.append(job_data)

for result in results:
    print(result, "\n\n----------------------\n")
