from urllib.request import urlopen


def scraper(url):
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    with open('test.txt', 'w') as f:
        f.write(html)

