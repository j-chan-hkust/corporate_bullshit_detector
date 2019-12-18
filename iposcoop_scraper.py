from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

from random import randint
from time import sleep

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

if __name__ == "__main__":
    raw_html = simple_get('https://www.iposcoop.com/last-12-months/')
    html = BeautifulSoup(raw_html, 'html.parser')
    count = 0
    for tr in html.findAll('table')[0].findAll('tr'):
        print(tr.findAll('a'))
        mission_statement_html = ''
        yahoo_financial_html = ''

        try:
            mission_statement_html = tr.findAll('a')[0].get('href')
            ticker = tr.findAll('a')[1].text
        except IndexError:
            print("index err")
            continue

        ms_soup = simple_get(mission_statement_html)
        ms_soup = BeautifulSoup(ms_soup, 'html.parser')
        print(ms_soup.findAll('p'))
        text = ms_soup.findAll('p')[1].text

        print(text)
        print(ticker)
        file = open('mission_statements/'+ticker+'.txt', 'w')
        file.write(text)

        sleep(randint(10, 100)*.01) #sleep for random amount of time