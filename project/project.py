import requests
from bs4 import BeautifulSoup

def url_retriever(ticker):
    url = f'https://www.google.com/finance/quote/{ticker}'
    return requests.get(url)

def price_returner(parsed):
    soup = BeautifulSoup(parsed.text, 'html.parser')
    price = soup.find('div', attrs={'class': 'kf1m0'}).text
    return price

def previous_close(parsed):
    soup = BeautifulSoup(parsed.text, 'html.parser')
    pre_price = soup.find('div', attrs={'class': 'P6K39c'}).text
    return pre_price

def percent_change(a, b):
    a_int = float(a[1:])
    b_int = float(b[1:])
    cal = ((a_int/b_int) - 1) * 100
    return f'{cal:.2}%'

def main():
    stock = input("Please type in the format of (Ticker symbol:Stock exchange): ")
    current = price_returner(url_retriever(stock))
    prev_close = previous_close(url_retriever(stock))
    print("Current: " + current)
    print("Previous Close: " + prev_close)
    print("Growth Performance: " + percent_change(current, prev_close))

if __name__ == "__main__":
    main()