# Traxss

<p align="center">
  <b>Automated Vulnerability Scanner for XSS | Written in Python3 | Utilizes Selenium Headless</b>
  <b>Traxss is a Hacktoberfest Project! If you are looking for a place to make Pull Requests, feel free here!</b></br>
  <a href="https://github.com/M4cs/traxss/network"><img src="https://img.shields.io/github/forks/M4cs/traxss# .svg" alt="Forks"></a>
  <a href="https://github.com/M4cs/traxss/stargazers"><img src="https://img.shields.io/github/stars/M4cs/traxss.svg" atl="Stars"></a>
  <a href="https://github.com/M4cs/traxss/issues"><img src="https://img.shields.io/github/issues/M4cs/traxss.svg" alt="Issues"></a>
  <a href="http://www.python.org/download/"><img alt="Python 3.6+" src="https://img.shields.io/badge/Python-3.6+-yellow.svg"></a></br>
  <a href="https://asciinema.org/a/273492" target="_blank"><img src="https://asciinema.org/a/273492.svg" /></a>
</p>

# What is Traxss

Traxss is an automated framework to scan URLs and webpages for XSS Vulnerabilities. It includes over 575 Payloads to test with and multiple options for robustness of tests. View the gif above to see a preview of the fastest type of scan. **Traxss is still in development and if you'd like to help PLEASE contribute with fixes or feature additions.**

# Getting Started

## Installing Requirements

To install the requirements run:

```
pip3 install -r requirements.txt
```

You will also need Chromedriver installed. To install on MacOS run `brew install cask chromedriver`. To install on Windows find the Chromedriver installer. For Linux find the correct install method for your distro.

## Running Traxss

To run Traxss run `python3 traxss.py`.

This will display a menu that will help walk you through the features.

# Features

## Full Scan w/ HTML

This scan uses a query scan with 575+ payload. It will attempt to find XSS vulnerabilities by passing params through the URL. It will also render the HTML and attempt to find manual XSS Vulnerablities (this functionality may be broken I have only gotten it to work under some circumstances).

## Full Scan w/o HTML

This scan is only the query scan

## Fast Scan w/ HTML

This scan is the same as the full w/ HTML but it will only use 7 attack vectors rather than the 575+ vectors.

## Fast Scan w/o HTML

This scan is the same as the full w/o HTML but it will only use 7 attack vectors rather than the 575+ vectors.

# Contributions

Please make PRs. I haven't worked with Selenium enough to know the tricks with it so if you could help perfect the HTML scans that would be the priority!
