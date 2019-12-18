from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

from random import randint
from time import sleep
import os.path


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


# Previously used:
# https://web.archive.org/web/20190220221837/https://www.iposcoop.com/last-12-months/
# https://web.archive.org/web/20171218111456/https://www.iposcoop.com/last-12-months/
# https://web.archive.org/web/20170519103155/https://www.iposcoop.com/last-12-months/
if __name__ == "__main__":
    raw_html = simple_get('https://web.archive.org/web/20170519103155/https://www.iposcoop.com/last-12-months/')
    html = BeautifulSoup(raw_html, 'html.parser')
    count = 0
    for tr in html.findAll('table')[0].findAll('tr'):
        print(tr.findAll('a'))
        mission_statement_html = ''
        yahoo_financial_html = ''

        try:
            mission_statement_html = tr.findAll('a')[0].get('href')
            mission_statement_html = mission_statement_html[mission_statement_html.find("https://www.iposcoop.com/"):]
            print(mission_statement_html)
            ticker = tr.findAll('a')[1].text
        except IndexError:
            print("index err")
            continue

        if os.path.isfile(ticker + ".txt"):  # this is so we can skip redundant searches/updates
            continue

        try:
            ms_soup = simple_get(mission_statement_html)
            ms_soup = BeautifulSoup(ms_soup, 'html.parser')
        except TypeError:
            print("type err")
            continue

        print(ms_soup.findAll('p'))
        text = ''
        for t in ms_soup.findAll('p'):
            if len(t.text) < 5:
                continue
            if t.text.find("Disclaimer") != -1:
                continue
            if t.text.find("Disclosure") != -1:
                continue

            text = t.text

        print(text)
        print(ticker)
        file = open('mission_statements/' + ticker + '.txt', 'w')
        try:
            file.write(text)
        except UnicodeEncodeError:
            print('unicode error')
            continue

        sleep(randint(10, 100) * .01)  # sleep for random amount of time
