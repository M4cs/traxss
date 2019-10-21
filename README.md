# Traxss

<b>Automated Vulnerability Scanner for XSS</b> | <b>Written in Python3</b> | <b>Utilizes Selenium Headless</b>
<p align="center">
<a href="https://github.com/M4cs/traxss/network"><img src="https://img.shields.io/github/forks/M4cs/traxss# .svg" alt="Forks"></a>
<a href="https://github.com/M4cs/traxss/stargazers"><img src="https://img.shields.io/github/stars/M4cs/traxss.svg" atl="Stars"></a>
<a href="https://github.com/M4cs/traxss/issues"><img src="https://img.shields.io/github/issues/M4cs/traxss.svg" alt="Issues"></a>
<a href="http://www.python.org/download/"><img alt="Python 3.6+" src="https://img.shields.io/badge/Python-3.6+-yellow.svg"></a></br>
<a href="https://asciinema.org/a/273492" target="_blank"><img src="https://asciinema.org/a/273492.svg" /></a>
</p>
<p align = "center"><b>DEMO</b></p>

# Background

### Traxss is a Hacktoberfest Project! If you are looking for a place to make contribute, please feel free.
Traxss is an automated framework to scan URLs and webpages for XSS Vulnerabilities. It includes over 575 Payloads to test with and multiple options for robustness of tests. View the gif above to see a preview of the fastest type of scan.

# Getting Started

## Prerequisites

Traxss depends on Chromedriver. On MacOS this can be installed with the homebrew command:

```
brew install cask chromedriver
```

Alternatively, find a version for other operating systems here: https://sites.google.com/a/chromium.org/chromedriver/downloads

## Installation

Run the command:

```
pip3 install -r requirements.txt
```

## Docker Build
```
docker build -t <IMAGE NAME> .
docker build -t xshuden/traxss .
```

## Docker Run
```
docker run --rm -it xshuden/traxss
```

## Running Traxss

Traxx can be started with the command:

```
python3 traxss.py
```

This will launch an interactive CLI to guide you through the process.

## Types of Scans

#### Full Scan w/ HTML

Uses a query scan with 575+ payloads and attempts to find XSS vulnerabilities by passing parameters through the URL. It will also render the HTML and attempt to find manual XSS Vulnerabilities (this feature is still in beta).

#### Full Scan w/o HTML

This scan will run the query scan only.

#### Fast Scan w/ HTML

This scan is the same as the full w/ HTML but it will only use 7 attack vectors rather than the 575+ vectors.

#### Fast Scan w/o HTML

This scan is the same as the fast w/o HTML but it will only use 7 attack vectors rather than the 575+ vectors.

## Contributing

Thank you for your interest! All types of contributions are welcome.
- Fork and clone this repository
- Create your branch from the master branch
- Please open your PR with the master branch as the base
