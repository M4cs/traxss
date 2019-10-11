from crayons import *
from traxss.core.scanner import Scanner
import sys
class Menu:
    def __init__(self):
        self.banner = """\
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄       ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌     ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▐░▌   ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ 
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌  ▐░▌ ▐░▌  ▐░▌          ▐░▌          
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌   ▐░▐░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ 
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌    ▐░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▐░▌     ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌   ▐░▌░▌    ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌     ▐░▌  ▐░▌       ▐░▌  ▐░▌ ▐░▌            ▐░▌          ▐░▌
     ▐░▌     ▐░▌      ▐░▌ ▐░▌       ▐░▌ ▐░▌   ▐░▌  ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
      ▀       ▀         ▀  ▀         ▀  ▀       ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
       Version: 1.1 | Created by @maxbridgland | github.com/M4cs/Traxss"""
        self.menu = """\
    [1] Scan URL (Full w/ HTML Scan)

    [2] Scan URL (Fast w/ HTML Scan)

    [3] Scan URL (Full w/o HTML Scan)

    [4] Scan URL (Fast w/o HTML Scan)
    
    [5] Exit Program\n"""
    
    def start(self):
        stop_on_first = False
        store_output = False
        report_out = None
        cookies = None
        url = None
        print(blue(self.banner))
        print('\nWelcome To Traxss - A URL XSS Scanner\n')
        print(self.menu)
        if 'win32' in sys.platform or 'win64' in sys.platform:
            ps1 = str('traxss> ')
        else:
            ps1 = str(blue('[') + white('traxss') + blue(']') + '> ')
        
        while True:
            option = input(ps1)
            if option == '1':
                print('\nPlease enter URL to scan w/ parameters included:')
                print(green('[ex.]'), 'https://xss-game.appspot.com/level1/frame?query=test\n')
                url = input(ps1)
                print('\nWould you like to add a cookie string?')
                while True:
                    ans = input('\n[Y\\n]> ').lower()
                    if ans == 'n':
                        cookies = None
                        break
                    elif ans == 'y':
                        print('Please enter your cookie string in this format:')
                        print(green('[ex.]'), '<cookiename>:<cookievalue>:<cookiepath>\n')
                        cookies = input(ps1)
                        break
                    else:
                        print('\nUnknown option. Please choose Y or N.\n')
                print('\nWould you like to stop after the first vulnerability found?')
                while True:
                    ans = input('\n[Y\\n]> ').lower()
                    if ans == 'n':
                        stop_on_first = False
                        break
                    elif ans == 'y':
                        stop_on_first = True
                        break
                    else:
                        print(red('\nUnknown option. Please choose Y or N.\n'))
                print('\nWould you like to store the results in a JSON file?\n')
                while True:
                    ans = input('[Y\\n]> ').lower()
                    if ans == 'n':
                        store_output = False
                        report_out = None
                        break
                    elif ans == 'y':
                        store_output = True
                        print('\nPlease enter the file name below:\n')
                        while True:
                            report_out = input(ps1)
                            break
                        break
                #print('\nPlease enter form names you would like to include in scope:')
                #print(blue('[')+white('ex.')+blue(']') + ' query-box, search-box')
                #while True:
                #    tags_ = input(ps1).lower()
                #    if len(tags_) >= 1:
                #        tag_list = tags_.split(',')
                #        tags_ = []
                #        for tag in tag_list:
                #            tags_.append(tag.replace(' ', ''))
                #        break
                #    else:
                #        tags_ = None
                #        break
                print(red('[*] This may take a while. Press ENTER to continue or Ctrl-C to quit.. [*]'))
                input()
                print()
                scanner = Scanner(url, cookies, stop_on_first, store_output, report_out, html_scan=True)
                scanner.run_on_url()
                scanner.store_results()
            elif option == '2':
                print('\nPlease enter URL to scan w/ parameters included')
                print(green('[ex.]'), 'https://xss-game.appspot.com/level1/frame?query=test\n')
                url = input(ps1)
                print('\nWould you like to add a cookie string?')
                while True:
                    ans = input('\n[Y\\n]> ').lower()
                    if ans == 'n':
                        cookies = None
                        break
                    elif ans == 'y':
                        print('Please enter your cookie string in this format:')
                        print(green('[ex.]'), '<cookiename>:<cookievalue>:<cookiepath>\n')
                        cookies = input(ps1)
                        break
                    else:
                        print('\nUnknown option. please choose Y or N.\n')
                print('\nWould you like to stop after the first vulnerability found?')
                while True:
                    ans = input('\n[Y\\n]> ').lower()
                    if ans == 'n':
                        stop_on_first = False
                        break
                    elif ans == 'y':
                        stop_on_first = True
                        break
                    else:
                        print(red('\nUnknown option. Please choose Y or N.\n'))
                print('\nWould you like to store the results in a JSON file?\n')
                while True:
                    ans = input('[Y\\n]> ').lower()
                    if ans == 'n':
                        store_output = False
                        report_out = None
                        break
                    elif ans == 'y':
                        store_output = True
                        print('\nPlease Enter The File Name Below\n')
                        while True:
                            report_out = input(ps1)
                            break
                    else:
                        print(red('\nUnknown option. Please choose Y or N.\n'))
                #print('\nPlease enter form names you would like to include in scope:')
                #print(blue('[')+white('ex.')+blue(']') + ' query-box, search-box')
                #while True:
                #    tags_ = input(ps1).lower()
                #    if len(tags_) >= 1:
                #        tag_list = tags_.split(',')
                #        tags_ = []
                #        for tag in tag_list:
                #            tags_.append(tag.replace(' ', ''))
                #        break
                #    else:
                #        tags_ = None
                #        break
                print(red('\n[*] This may take a while. Press ENTER to continue or Ctrl-C to quit. [*]'))
                input()
                scanner = Scanner(url, cookies, stop_on_first, store_output, report_out, fast_payload=True, html_scan=True)
                scanner.run_on_url()
                scanner.store_results()
            elif option == '3':
                print('\nPlease Enter URL To Scan w/ Parameters Included')
                print(green('[ex.]'), 'https://xss-game.appspot.com/level1/frame?query=test\n')
                url = input(ps1)
                print('\nWould You Like To Add A Cookie String?')
                while True:
                    ans = input('\n[Y\\n]> ').lower()
                    if ans == 'n':
                        cookies = None
                        break
                    elif ans == 'y':
                        print('Please Enter Your Cookie String In This Format')
                        print(green('[ex.]'), '<cookiename>:<cookievalue>:<cookiepath>\n')
                        cookies = input(ps1)
                        break
                    else:
                        print('\nUnknown Option. Please Choose Y or N\n')
                print('\nWould you like to stop after the first vulnerability found?')
                while True:
                    ans = input('\n[Y\\n]> ').lower()
                    if ans == 'n':
                        stop_on_first = False
                        break
                    elif ans == 'y':
                        stop_on_first = True
                        break
                    else:
                        print(red('\nUnknown Option. Please Choose Y or N\n'))
                print('\nWould you like to store results to a JSON file?\n')
                while True:
                    ans = input('[Y\\n]> ').lower()
                    if ans == 'n':
                        store_output = False
                        report_out = None
                        break
                    else:
                        store_output = True
                        print('\nPlease Enter The File Name Below\n')
                        while True:
                            report_out = input(ps1)
                            break
                        break
                print(red('[*] This may take a while. Press ENTER to continue or Ctrl-C to quit. [*]'))
                input()
                print()
                scanner = Scanner(url, cookies, stop_on_first, store_output, report_out, html_scan=True)
                scanner.run_on_url()
                scanner.store_results()
            elif option == '4':
                print('\nPlease Enter URL To Scan w/ Parameters Included')
                print(green('[ex.]'), 'https://xss-game.appspot.com/level1/frame?query=test\n')
                url = input(ps1)
                print('\nWould You Like To Add A Cookie String?')
                while True:
                    ans = input('\n[Y\\n]> ').lower()
                    if ans == 'n':
                        cookies = None
                        break
                    elif ans == 'y':
                        print('Please Enter Your Cookie String In This Format')
                        print(green('[ex.]'), '<cookiename>:<cookievalue>:<cookiepath>\n')
                        cookies = input(ps1)
                        break
                    else:
                        print('\nUnknown Option. Please Choose Y or N\n')
                print('\nWould you like to stop after the first vulnerability found?')
                while True:
                    ans = input('\n[Y\\n]> ').lower()
                    if ans == 'n':
                        stop_on_first = False
                        break
                    elif ans == 'y':
                        stop_on_first = True
                        break
                    else:
                        print(red('\nUnknown Option. Please Choose Y or N\n'))
                print('\nWould you like to store results in a JSON file?\n')
                while True:
                    ans = input('[Y\\n]> ').lower()
                    if ans == 'n':
                        store_output = False
                        report_out = None
                        break
                    else:
                        store_output = True
                        print('\nPlease Enter The File Name Below\n')
                        while True:
                            report_out = input(ps1)
                            break
                        break
                print(red('\n[*] This may take a while. Press ENTER to continue or Ctrl-C to quit. [*]'))
                input()
                scanner = Scanner(url, cookies, stop_on_first, store_output, report_out, fast_payload=True, html_scan=False)
                scanner.run_on_url()
                scanner.store_results()
            elif option == '5':
                exit()
            else:
                print(red('\nUnknown Option. Please Choose 1 or 2\n'))
