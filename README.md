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
