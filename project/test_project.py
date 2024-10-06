from project import url_retriever, price_returner, previous_close, percent_change

def test_url_retriever():
    assert(url_retriever("AAPL:NASDAQ")).status_code == 200

def price_returner():
    assert(price_returner("AAPL:NASDAQ")) == "$171.21"

def previous_close():
    assert(previous_close("AAPL:NASDAQ")) == "$170.69"

def percent_change():
    assert(previous_close("AAPL:NASDAQ")) == "0.3%"