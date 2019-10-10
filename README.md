# __Traxss__

<p align="center">
  <b>Automated Vulnerability Scanner for XSS || Written in Python3 || Utilizes Selenium Headless</b></br>
  <b>Traxss is a Hacktoberfest Project! If you are looking for a place to make Pull Requests, feel free here!</b></br>
  <a href="https://github.com/M4cs/traxss/network"><img src="https://img.shields.io/github/forks/M4cs/traxss# .svg" alt="Forks"></a>
  <a href="https://github.com/M4cs/traxss/stargazers"><img src="https://img.shields.io/github/stars/M4cs/traxss.svg" atl="Stars"></a>
  <a href="https://github.com/M4cs/traxss/issues"><img src="https://img.shields.io/github/issues/M4cs/traxss.svg" alt="Issues"></a>
  <a href="http://www.python.org/download/"><img alt="Python 3.6+" src="https://img.shields.io/badge/Python-3.6+-yellow.svg"></a></br>
  <a href="https://asciinema.org/a/273492" target="_blank"><img src="https://asciinema.org/a/273492.svg" /></a>
</p>

# What is Traxss

Traxss* is an automated framework to scan URLs and webpages for XSS vulnerabilities. It includes over 575 payloads to test with and multiple options for robustness of tests. View the gif above to see a preview of the fastest type of scan.</br>
    * **Traxss is still in development and if you'd like to help PLEASE contribute with fixes or feature additions.**

# __Getting Started__

## _Installing Requirements_

* To install the requirements run: ```pip3 install -r requirements.txt```

* You will also need Chromedriver installed.
  * To install on <b>MacOS</b> run:  ```  brew install cask chromedriver  ```
  * To install on <b>Windows</b> find the Chromedriver installer at <a href="https://chromedriver.chromium.org/downloads"></a>
  * To install on <b>Linux</b>:
    * Debian based Linux distros: run:    ```sudo apt-get install chromium-chromedriver```
    * Other distros : find the correct install method for your distro.

## _Running Traxss_

To run Traxss run: ```python3 traxss.py```
This will display a menu that will help walk you through the features.

# __Features__

## * Full Scan w/ HTML

This scan uses a query scan with 575+ payloads. It will attempt to find XSS vulnerabilities by passing params through the URL. It will also render the HTML and attempt to find manual XSS Vulnerablities (this functionality may be broken I have only gotten it to work under some circumstances).

## * Full Scan w/o HTML

This scan is only the query scan.

## * Fast Scan w/ HTML

This scan is the same as the full w/ HTML but it will only use 7 attack vectors rather than the 575+ vectors.

## * Fast Scan w/o HTML

This scan is the same as the fast w/o HTML but it will only use 7 attack vectors rather than the 575+ vectors.

# __Contributions__

Please make PRs. I haven't worked with Selenium enough to know the tricks with it so if you could help perfect the HTML scans that would be the priority!
