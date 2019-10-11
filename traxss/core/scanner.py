import sys
import requests
import json
import urllib
import os
from crayons import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def get_payloads_from_vectors(fast=False):
    payloads = []
    if not fast:
        with open('traxss/core/constants/vectors.txt', 'r', encoding = "utf-8") as vector_file:
            for vector in vector_file.readlines():
                payloads.append(vector)
    else:
        with open('traxss/core/constants/vectors.txt', 'r', encoding = "utf-8") as vector_file:
            for vector in vector_file.readlines():
                payloads.append(vector)
    return payloads

def get_base_url(url):
    base_url = url.split('?')[0]
    return base_url

def encode_url(url, params):
    params_encoded = urllib.parse.urlencode(params)
    full_url = url + "?" + params_encoded
    return full_url

class Scanner:
    def __init__(self, url, cookies=None, stop_on_first=False, store_report=False, report_output=None, fast_payload=False, html_scan=False):
        self.payloads = get_payloads_from_vectors()
        if fast_payload:
            self.payloads = get_payloads_from_vectors(fast=True)
        self.url = url
        self.stop = stop_on_first
        self.base_url = get_base_url(self.url)
        self.params = self.get_params()
        self.html_scan = html_scan
        self.cookies = cookies
        if cookies:
            self.cookies = self.get_cookies()
        self.result_count = 0
        self.results = { 'results': [] }
        self.store_report = store_report
        self.report_output = report_output
        if store_report:
            if not report_output:
                raise Exception('Missing Report Output')

    def get_cookies(self):
        cookies_list = cookies.split(':')
        cookies_obj = {
            'name': cookies[0],
            'values': cookies[1],
            'path': cookies[2]
        }
        return cookies_obj
    
    def get_params(self):
        pure_url = urllib.parse.urlparse(self.url)
        query_string = pure_url.query
        params = dict(urllib.parse.parse_qsl(query_string))
        return params

    def run_on_url(self):
        print(blue('[*] Running URL Query Scan [*]'))
        for payload in self.payloads:
            if self.result_count == 1 and self.stop:
                break
            for param in self.params.keys():
                previous_value = self.params[param]
                self.params[param] = payload
                target_url = encode_url(self.base_url, self.params)
                raw_params = urllib.parse.urlencode(self.params)
                options = webdriver.ChromeOptions()
                options.add_argument('--headless')
                driver = webdriver.Chrome(chrome_options=options)
                if self.cookies:
                    driver.get(url)
                    driver.add_cookie(self.cookies)
                driver.get(target_url)
                driver.implicitly_wait(1)
                try:
                    if driver.switch_to.alert.text:
                        if self.stop is True:
                            self.result_count += 1
                            print(green('RESULTS: {}'.format(self.result_count).center(50, '='), bold=True))
                            print()
                            print(blue('[') + green('*', bold=True) + blue(']') + green(' Found XSS Vulnerability'))
                            print(blue('[') + green('*', bold=True) + blue(']') + green(' Payload:'), blue(raw_params))
                            print(blue('[') + green('*', bold=True) + blue(']') + green(' URL:'), blue(target_url))
                            print()
                            print(green(''.center(50, '='), bold=True))
                            driver.quit()
                            break
                        else:
                            self.result_count += 1
                            print(green('RESULTS: {}'.format(self.result_count).center(50, '='), bold=True))
                            print()
                            print(blue('[') + green('*', bold=True) + blue(']') + green(' Found XSS Vulnerability'))
                            print(blue('[') + green('*', bold=True) + blue(']') + green(' Payload:'), blue(raw_params))
                            print(blue('[') + green('*', bold=True) + blue(']') + green(' URL:'), blue(target_url))
                            print()
                            print(green(''.center(50, '='), bold=True))
                            self.results['results'].append({
                                'count': self.result_count,
                                'payload': raw_params,
                                'url': target_url
                            })
                            driver.quit()
                except NoAlertPresentException:
                    pass
        print(blue('[*] Completed URL Query Scan [*]'))
        if self.html_scan:
            print(blue('[*] Starting HTML XSS Scan [*]'))
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Chrome(chrome_options=options)
            if self.cookies:
                driver.get(url)
                driver.add_cookie(self.cookies)
            for payload in self.payloads:
                if self.result_count == 2 and self.stop:
                    break
                driver.get(self.base_url)
                webelement_list = WebDriverWait(driver, 10).until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//input | //textarea | //button")))
                for id in webelement_list:
                    if self.result_count == 1 and self.stop:
                        break
                    try:
                        if id.tag_name == 'textarea' or id.tag_name == 'input':
                            id.send_keys(payload)
                            id.send_keys(Keys.ENTER)
                            try:
                                new = driver.find_element_by_css_selector('button').click()
                            except ElementNotInteractableException:
                                pass
                        if id.tag_name == 'button' or id.tag_name == 'input':
                            id.click()
                        if driver.switch_to.alert.text:
                            if self.stop is True:
                                self.result_count += 1
                                print(green('RESULTS: {}'.format(self.result_count).center(50, '='), bold=True))
                                print()
                                print(blue('[') + green('*', bold=True) + blue(']') + green(' Found XSS Vulnerability'))
                                print(blue('[') + green('*', bold=True) + blue(']') + green(' Payload:'), blue(raw_params))
                                print(blue('[') + green('*', bold=True) + blue(']') + green(' URL:'), blue(target_url))
                                print()
                                print(green(''.center(50, '='), bold=True))
                                driver.quit()
                                break
                            else:
                                self.result_count += 1
                                print(green('RESULTS: {}'.format(self.result_count).center(50, '='), bold=True))
                                print()
                                print(blue('[') + green('*', bold=True) + blue(']') + green(' Found XSS Vulnerability'))
                                print(blue('[') + green('*', bold=True) + blue(']') + green(' Payload:'), blue(raw_params))
                                print(blue('[') + green('*', bold=True) + blue(']') + green(' URL:'), blue(target_url))
                                print()
                                print(green(''.center(50, '='), bold=True))
                                self.results['results'].append({
                                    'count': self.result_count,
                                    'payload': raw_params,
                                    'url': target_url
                                })
                                driver.quit()
                    except NoAlertPresentException:
                        pass
                    except StaleElementReferenceException:
                        pass
                    except ElementNotInteractableException:
                        pass
        print(blue('[*] Completed Scan on URL'))
        if self.result_count == 0:
            print(red('[!] No Results Found. Warning This Does NOT Mean You Are Not Still Vulnerable [!]'))

    def store_results(self):
        if self.store_report:
            if not self.report_output.endswith('.json'):
                report_out = self.report_output + '.json'
                real_path = os.path.realpath(report_out)
            else:
                real_path = os.path.realpath(self.report_output)
            if os.path.exists(real_path):
                os.remove(real_path)
            with open(real_path, 'w') as file:
                file.write('{}')
            with open(real_path, 'r+') as json_file:
                obj = json.load(json_file)
                obj = self.results
                json_file.truncate()
                json_file.seek(0)
                json.dump(obj, json_file, indent=4)
            print(blue('[*] Stored Results To {}'.format(real_path)))
