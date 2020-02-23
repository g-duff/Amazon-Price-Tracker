import requests
from bs4 import BeautifulSoup
import smtplib, ssl

def extract_url(url):
    if url.find("www.amazon.co.uk") != -1:
        index = url.find("/dp/")
        if index != -1:
            index2 = index + 14
            url = "https://www.amazon.co.uk"+url[index:index2]
        else:
            index = url.find("/gp/")
            if index != -1:
                index2 = index + 22
                url = "https//www.amazon.co.uk"+url[index:index2]
            else:
                url = None
    else:
        url = None
    return url

def get_converted_price(price):
    stripped_price = (float(price.strip("£")))
    return stripped_price

def email(message, password):
    context = ssl.create_default_context()
    port = 465
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("drbencpython@gmail.com", password)
        server.sendmail("drbencpython@gmail.com", "coulsonba@gmail.com", str(message))
        print("Cheap price detected, email sent")

def timestamp_to_list(timestamp):
    ''' Converts a timestamp to [year, month, day, hour, minute, second]'''
    date, time = str(timestamp).split(' ')
    date, time = date.split('-'), time.split(':')
    date, time = [int(d) for d in date], [float(t) for t in time]
    timestamp = date + time
    return timestamp

def get_soup(url):
    '''Gets a soup from a URL'''
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/79.0.3945.130 Safari/537.36"}
    _url = extract_url(url)
    #print(_url)
    if _url is None:
        soup = None
    else:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html5lib")
    return soup

def get_price(soup):
    '''Gets price from soup'''
    price = soup.find(id="priceblock_dealprice")
    if price is None:
        price = soup.find(id="priceblock_ourprice")
    price = get_converted_price(price.get_text())
    return price

def get_title(soup):
    '''Gets title from soup'''
    title = soup.find(id = "productTitle")
    return title.get_text().strip()


def get_deal(soup):
    '''Determines if there's a deal on '''
    pass

def price_check(names, prices, good_prices):
    check_good = [p1<p2 for p1, p2 in zip(prices, good_prices)]
    cheap_items = [n for n, b in zip(names, check_good) if b]
    return cheap_items

    # #set email price thresholds here
    # if int(prices[0]) < 10:
    #     email("cheap 71708")
    # elif float(prices[1]) < 18:
    #     email("cheap gamers market")
    # elif float(prices[2]) < 18:
    #     email("cheap car")
    # elif float(prices[3]) < 15:
    #     email("cheap racers")
    # elif float(prices[4]) < 27:
    #     email("cheap dragon")
    # elif float(prices[5]) < 30:
    #     email("cheap mandalorian walker")
    # elif float(prices[6]) < 12:
    #     email("cheap welcome to hidden side")
    # elif float(prices[7]) < 7:
    #     email("cheap kai pod")
    # elif float(prices[8]) < 7:
    #     email("cheap lloyd pod")
    # elif float(prices[9]) < 7:
    #     email("cheap jay pod")