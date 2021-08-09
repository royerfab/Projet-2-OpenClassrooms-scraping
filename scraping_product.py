from bs4 import BeautifulSoup
import requests

url = 'http://books.toscrape.com/catalogue/a-flight-of-arrows-the-pathfinders-2_876/index.html'
response = requests.get(url)

image_url_base = 'http://books.toscrape.com/'
def image_url(image_url_relative):
    return image_url_base + image_url_relative.replace('../', '')

if response.ok:
    soup = BeautifulSoup(response.content, 'html.parser')
    conteneur_td = soup.find("table", class_="table table-striped")
    td = conteneur_td.find_all("td")
    product_page_url = requests.get(url)
    universal_product_code = td[0].text
    title = soup.find("h1").text
    prices_including_taxes = td[3].text
    prices_excluding_taxes = td[2].text
    number_available = td[5].text
    conteneur_p = soup.find("article", class_='product_page')
    p_description = conteneur_p.find_all("p")
    product_description = p_description[3].text
    conteneur_a_category = soup.find("ul", class_='breadcrumb')
    a_category = conteneur_a_category.find_all("a")
    category = a_category[2].text
    review_rating = soup.find("p", class_="star-rating")
    image_url_relative = soup.find("div", class_="item active").find("img").get('src')
    url_image = image_url(image_url_relative)
    product_informations = {'product_page_url': product_page_url, 'universal_product_code': universal_product_code,
                            'title': title, 'prices_including_taxes': prices_including_taxes,
                            'prices_excluding_taxes': prices_excluding_taxes, 'number_available': number_available,
                            'product_description': product_description, 'category': category,
                            'review_rating': review_rating.text, 'image_url': url_image}
    print(product_informations)
else:
    print('La requête n a pas aboutie.')
