from bs4 import BeautifulSoup
import requests
#maybe an input technique for amazon link
AMZN_LINK = "https://www.amazon.in/s?k=Mechanical+Keyboard" 
def scrape_amazon (AMZN_LINK):
    '''
    This function scrapes amazon list pages and will store them in a pandas dataframe
    Args:
        amazon_link - Current Amazon link

    Returns: 
        None - It directly uploads to the existing Pandas data frame 

    '''
    amazon_html = requests.get(AMZN_LINK)
    amazon_soup = BeautifulSoup(amazon_html,'lxml')

