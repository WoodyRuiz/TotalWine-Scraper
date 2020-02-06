from bs4 import BeautifulSoup
import requests

product_site_list_1 = "https://www.totalwine.com/Product-en-USD-0.xml"

page_response = requests.get(product_site_list_1, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")



print(page_content)