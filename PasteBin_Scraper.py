"""
This program is designed to be a threat intelligence gathering tool that will search various known locations for
keywords provided by the user. The tool will offer multiple report generation options or console output.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

global driver

path = "/Applications/chromedriver"
paste_URL = "http://google.com"
driver = webdriver.Chrome(path).close()


def paste_scrape(keyword):
    """
    Provides functionality to scrape pastebin.
    """
    driver = webdriver.Chrome(path)
    driver.minimize_window()
    driver.get(paste_URL)
    search = driver.find_element_by_name('q')
    search.send_keys("site:pastebin.com" + " " + keyword)
    search.send_keys(Keys.RETURN)

    paste_titles = ''
    paste_summaries = ''
    paste_links = ''

    i = 0
    try:
        for i in range(10):
            Next_Page = driver.find_element_by_class_name('d6cvqb')
            Next_Page.click()
            for finding in driver.find_elements_by_xpath('//div[@class="g"]'):
                paste_titles += finding.find_element_by_tag_name('h3').text + '\r\n'
                paste_summaries += finding.find_element_by_class_name('aCOpRe').text + '\r\n'
                paste_links += finding.find_element_by_css_selector('.yuRUbf [href]').get_attribute('href') + '\r\n'
            i = (i + 1)
    except:
        print("It appears there were less than ten pages of results, moving to try single page scrape")
        for finding in driver.find_elements_by_xpath('//div[@class="g"]'):
            paste_titles += finding.find_element_by_tag_name('h3').text + '\r\n'
            paste_summaries += finding.find_element_by_class_name('aCOpRe').text + '\r\n'
            paste_links += finding.find_element_by_css_selector('.yuRUbf [href]').get_attribute('href') + '\r\n'

    join_files(paste_titles, paste_summaries, paste_links)


def join_files(list1, list2, list3):
    """
    Joins results from scrapes and places them in a single variable.
    """
    global titles
    global summaries
    global links

    titles = ''
    summaries = ''
    links = ''

    if len(list1) > 10:
        for strs in list1:
            titles += strs
        for strs in list2:
            summaries += strs
        for strs in list3:
            links += strs


# def twitter_scrape():

# def facebook_scrape():

def file_generation(list1, list2, list3, Date, keyword, driver):
    """
    Creates a file if the user chooses to do so and places it in the current working directory. To be updated to include
    custom file location placement.
    """
    file_name = 'WebScrape_{}_{}.txt'.format(str(keyword), str(Date))
    results = open(file_name, "w+")

    results.write('Scrape results:' + ' ' + keyword)
    results.write('\r\n')
    results.write('\r\n')

    results.write('Findings Summary:')
    results.write('\r\n')

    pass_title = titles.find('password')
    pass_sum = summaries.find('password')
    email_title = titles.find('@')
    email_sum = summaries.find('@')
    user_title = titles.find('username')
    user_sum = summaries.find('username')
    hack_title = titles.find('hacked')
    hack_sum = summaries.find('hacked')
    vuln_title = titles.find('vulnerable')
    vuln_sum = summaries.find('vulnerable')

    if pass_title > 1 or pass_sum > 1:
        print('Password mentions found!')
        results.write('Password mentions found!' + '\r\n')
    else:
        print('No password mentions found')
        results.write('No password mentions found' + '\r\n')
    if email_title > 1 or email_sum > 1:
        print('Email found!')
        results.write('Email found!' + '\r\n')
    else:
        print('No email mentions found')
        results.write('No email mentions found' + '\r\n')
    if user_title > 1 or user_sum > 1:
        print('Username mentions found!')
        results.write('Username mentions found!' + '\r\n')
    else:
        print('No username found')
        results.write('No username found' + '\r\n')
    if hack_title > 1 or hack_sum > 1:
        print('Hack mention found!')
        results.write('Hack mention found!' + '\r\n')
    else:
        print('No mentions of hacks')
        results.write('No mentions of hacks' + '\r\n')
    if vuln_title > 1 or vuln_sum > 1:
        print('Vulnerability mentions found!')
        results.write('Vulnerability mentions found!' + '\r\n')
    else:
        print('No vulnerabilities mentioned')
        results.write('No vulnerabilities mentioned' + '\r\n')

    results.write('\r\n')
    results.write('\r\n')
    results.write('titles:')
    results.write('\r\n')

    for strs in titles:
        results.write(strs)

    results.write('\r\n')
    results.write('\r\n')
    results.write('summaries:')
    results.write('\r\n')

    for strs in summaries:
        results.write(strs)

    results.write('\r\n')
    results.write('\r\n')
    results.write('links:')
    results.write('\r\n')

    for strs in links:
        results.write(strs)
    results.close()
    driver
    results.close()
    quit()


def keyword_search_format(list1, list2):
    """
    Changes the strings in the list to lowercase so that when they are serched for keywords no false negatives occur
    based on a difference of capitalization.
    """
    try:
        for x in list1:
            titles = list1.lower()
        for x in list2:
            summaries = list2.lower()
        print('Successful')
    except:
        print(type(titles))
        print(type(summaries))
        print('Lowercase conversion failed')


# def keyword_search_f():

def keyword_search_nf(titles, summaries, links, driver):
    """
    Searches the text output of the function that returns the results for keywords if the user chooses not to generate a
    file.
    Need to change this to a list that is ran against titles and summaries.
    """
    pass_title = titles.find('password')
    pass_sum = summaries.find('password')
    email_title = titles.find('@')
    email_sum = summaries.find('@')
    user_title = titles.find('username')
    user_sum = summaries.find('username')
    hack_title = titles.find('hacked')
    hack_sum = summaries.find('hacked')
    vuln_title = titles.find('vulnerable')
    vuln_sum = summaries.find('vulnerable')

    if pass_title > 1 or pass_sum > 1:
        print('Password mentions found!')
    else:
        print('No password mentions found')
    if email_title > 1 or email_sum > 1:
        print('Email found!')
    else:
        print('No email mentions found')
    if user_title > 1 or user_sum > 1:
        print('Username mentions found!')
    else:
        print('No username found')
    if hack_title > 1 or hack_sum > 1:
        print('Hack mention found!')
    else:
        print('No mentions of hacks')
    if vuln_title > 1 or vuln_sum > 1:
        print('Vulnerability mentions found!')
    else:
        print('No vulnerabilities mentioned')

    print(titles, summaries, links)

    time.sleep(120)
    driver.close()
    quit()


def return_check(list1, list2, link3, driver):
    """
    Checks the search results to ensure data was returned.
    """
    if len(titles) > 10:
        print('Results found!')
        What_2_Do = input('Would you like the results placed in a text file for you? (Yes/No)')

        if What_2_Do == 'Yes':
            file_generation(titles, summaries, links, Date, keyword, driver)
        else:
            pass_title = titles.find('password')
            pass_sum = summaries.find('password')
            email_title = titles.find('@')
            email_sum = summaries.find('@')
            user_title = titles.find('username')
            user_sum = summaries.find('username')
            hack_title = titles.find('hacked')
            hack_sum = summaries.find('hacked')
            vuln_title = titles.find('vulnerable')
            vuln_sum = summaries.find('vulnerable')

            if pass_title > 1 or pass_sum > 1:
                print('Password mentions found!')
            else:
                print('No password mentions found')
            if email_title > 1 or email_sum > 1:
                print('Email found!')
            else:
                print('No email mentions found')
            if user_title > 1 or user_sum > 1:
                print('Username mentions found!')
            else:
                print('No username found')
            if hack_title > 1 or hack_sum > 1:
                print('Hack mention found!')
            else:
                print('No mentions of hacks')
            if vuln_title > 1 or vuln_sum > 1:
                print('Vulnerability mentions found!')
            else:
                print('No vulnerabilities mentioned')

            print(titles, summaries, links)

            time.sleep(90)
            driver.close()
            quit()
    else:
        try_again()


# def report_generation():

def try_again():
    """
    Offers the user the ability to search again without rerunning the program.
    """
    print('Scrape produced little to no results, try searching again using additional keywords')
    try_again = input('Would you like to try again (Yes/No)?:')

    if try_again.lower() == 'yes':
        main()
    else:
        quit()


def main():
    """
    Provides the main functionality of the program.
    """
    global Date
    global keyword
    Date = datetime.date(datetime.now())
    keyword = '"' + input(
        "Please provide a keyword or multiple keywords such as an agency name, usernames, emails, etc.:") + '"'

    if keyword == "NA" or keyword == '':
        print("No keywords provided, program will now close....")
        quit()
    else:
        paste_scrape(keyword)
        keyword_search_format(titles, summaries)
        return_check(titles, summaries, links, driver)


main()

