import requests
import bs4


def read_URL(URL, all_products_count):
    URL_ALL_data = requests.get(URL)
    URL_HTML_data = URL_ALL_data.text
    data = bs4.BeautifulSoup(URL_HTML_data)
    data_products_name = data.select('.woocommerce-LoopProduct-link')
    for product_name in data_products_name:
        file_deniz.write(f"{product_name.text}\n")
        all_products_count += 1
    
    print(f"{URL} SUCCESSFULLY DONE!")
    return URL_ALL_data.status_code , all_products_count


file_deniz = open("products.txt", "a")

all_products_count = 0
page = 1
while (True):
    page = str(page)
    #enter URL
    URL = "https://" + page
    URL_status , all_products_count = read_URL(URL, all_products_count)
    page = int(page)
    page += 1
    if (URL_status != 200):
        break

file_deniz.close()

print(f"{all_products_count} PPRODUCTS FOUNDED AND ALL PAGES DONE!")
