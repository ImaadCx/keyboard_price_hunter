from bs4 import BeautifulSoup
from camoufox.sync_api import Camoufox

with Camoufox(headless=False) as browser:
    page = browser.new_page()
    page.goto("https://www.amazon.in/s?k=Mechanical+Keyboard")
    page.wait_for_timeout(20000)
    html_content = page.content()
    print(html_content)
