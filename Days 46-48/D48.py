import requests
import bs4
from functools import wraps
from pathlib import Path
import os

# Trying to get a stock price from Yahoo! finance (FR)

URL = "https://fr.finance.yahoo.com/quote/"
STOCK = 'BIM.PA'
STORAGE = "BIM.PA.data"


def check_data_exists(fun):
    wraps(fun)

    def _wrapper(*args, **kwargs):
        file = Path(os.path.dirname(os.path.abspath(__file__))) / STORAGE
        if file.exists():
            with open(file, 'r') as f:
                result = f.read()
                return result
        else:
            result = fun(*args, **kwargs)
            with open(file, "w") as f:
                length = f.write(result)
                print(f'Wrote {length} characters to file {file}')
                return result

    return _wrapper


@check_data_exists
def pull_site(url: str) -> str:
    print(f'Getting data from {url}')
    r = requests.get(url)
    r.raise_for_status()

    return r.text


def parse_to_get_price(site_data: str) -> float:
    soup = bs4.BeautifulSoup(site_data, 'html.parser')
    res = soup.find("div", {"id": "quote-header-info"})

    return soup.find('span', {'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'}).getText()


if __name__ == '__main__':
    url = f'{URL}{STOCK}'
    data = pull_site(url)
    result = parse_to_get_price(data)
    print(result)
