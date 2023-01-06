# Job Scraper Using Python

### Table of Contents
<ul>
    <li><a href="#intro">Introduction</a></li>
    <li><a href="#showcase">Showcase</a></li>
    <li><a href="#pre">Prerequisites</a></li>
</ul>


<h3 id="intro">Introduction</h3>
This is a simple python project which will scrap job data from websites that are <a href="indeed.com">indeed</a> and <a href="weworkremotely.com">WE WORK REMOTELY</a>.
By using <b>Selenium</b>, python will automatically browse the websites and scrap job information which are title, company, location, and link. <br>
You can download a csv file which includes the data we have scraped.

<h3 id="showcase">Showcase</h3>
<img width="1220" alt="job_scraper_1" src="https://user-images.githubusercontent.com/97219959/210960653-1dd20291-b0f8-4e90-a461-7a014b164431.png">
<img width="1190" alt="job_scraper_2" src="https://user-images.githubusercontent.com/97219959/210960662-103bc1dc-49a7-4cfc-9481-92a28d1e5bcc.png">
<img width="1186" alt="job_scraper_3" src="https://user-images.githubusercontent.com/97219959/210960667-410ff77c-e3d3-48cd-b36e-f1e867995c1e.png">

<h3 id="pre">Prerequisites</h2>
<ol>
    <li><a href="https://requests.readthedocs.io/en/latest/#" target="_blank">requests</a></li>
        <b>requests</b> library will allow us to get access through websites. <br>
        <code>pip3 install requests</code> <br>
    <li><a href="https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup" target="_blank">Beautiful Soup</a></li>
        <b>Beautiful Soup</b> library gives us a HTML based code lines based on the websites that we have given. This will allow us to find specific tags and classes that we want in order to scrap the data we want. By using <b>requests</b>, we can get through websites then we can extract information. <br>
        <code>pip3 install beautifulsoup4</code> <br>
    <li><a href="https://www.selenium.dev" target="_blank">Selenium</a></li>
        <b>Selenium</b> is a library that automates browsers so that way the browsers we are about to extract data cannot identify the program we are about to use as a bot. <br>
        <code>pip3 install selenium</code> <br>
        <b>NOTE:</b> The following program is for educational purpose. I have no intention of using the program for commercial purposes.
    <li><a href="https://palletsprojects.com/p/flask/" target="_blank">Flask</a></li>
        <b>Flask</b> is a web application framework helps you to design a web easy and fast. <br>
        <code>pip3 install flask</code> <br>
    <li><a href="https://picocss.com" target="_blank">Pico.css</a></li>
        <b>Pico.css</b> will help your web looks fancier without any hard word<br>
        <pre><code>&lt;link rel="stylesheet" href="https://unpkg.com/@picocss/pico@latest/css/pico.min.css"&gt;</code></pre>
</ol>
