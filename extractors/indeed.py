from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def load_url(keyword, page):
    base_url = "https://kr.indeed.com/jobs"
    end_url = "&limit=50"
    
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("detach", True)
    
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    final_url = f"{base_url}?q={keyword}&start={page * 10}{end_url}"
    print("Loading", final_url)
    browser.get(final_url)

    return browser

def get_page_count(keyword):
    browser= load_url(keyword, 0)

    soup = BeautifulSoup(browser.page_source, "html.parser")

    pagination = soup.find("nav", class_ = "css-jbuxu0 ecydgvn0")

    if pagination == None:
        return 1
    else:
        pages = pagination.find_all("div", recursive=False)
        count = len(pages)

        if count >= 5:
            return 5
        else:
            return count

def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found ", pages, "pages")

    results = []

    for page in range(pages):
        browser= load_url(keyword, page)

        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_ = "jobsearch-ResultsList")
        jobs = job_list.find_all("li", recursive = False)
        
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

    return results
