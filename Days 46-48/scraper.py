import requests
import bs4

URL = 'https://pybit.es/pages/projects.html'

# It would be good to create a decorator to wrap the pull_site() function to save the
# data and requests the data only if this has not been pulled already.
# More sophisticated would be to check how old is the saved data


def pull_site() -> requests.models.Response:
    raw_site_page = requests.get(URL)
    raw_site_page.raise_for_status()

    return raw_site_page


def scrape_site(sitedata: requests.models.Response) -> None:
    soup = bs4.BeautifulSoup(sitedata.text, "html.parser")
    html_header_list = soup.select('.projectHeader')

    header_list = [header.getText() for header in html_header_list]

    for header in header_list:
        print(header)


if __name__ == '__main__':
    site = pull_site()
    scrape_site(site)
