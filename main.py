# import requests
# from bs4 import BeautifulSoup
# # import os
# # os.system('clear')

# # получение ХТМЛ(уникальна)
# def get_html(url, header):
#     responce = requests.get(url, headers=header)
#     if responce.status_code!=200:
#         return f"возникла ошибка: {responce.status_code}"
#     else:
#         return responce.text

# # Оброботка ХТМЛ
# def processing(html):
#     soup = BeautifulSoup(html, "lxml")
#     return soup


# # Запуск кода(уникальна)
# def main():
#     url='https://www.lcwaikiki.kz/ru-RU/KZ/tag/tshirt-7-5'
#     header= {'User_agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0'}
#     html = get_html(url, header)
#     soup= processing(html)
#     with open("nurai.html",'w', encoding="utf-8") as file:
#         file.write(str(soup))
#     print(soup)

# main()

# import os
# import requests
# from bs4 import BeautifulSoup
# import json
# os.system("clear")


# # Получения HTML (Уникальна)
# def get_html(url, header):
#     response = requests.get(url, headers=header)

#     if response.status_code != 200:
#         return f"Error: {response.status_code}"
#     else:
#         return response.text


# # Обработка HTML
# def proccessing(html):
#     soup = BeautifulSoup(html, "lxml").find('div',{'class':"product-grid"})
#     products = soup.find_all('div',{'class':"product-card"})
#     data = []
#     for product in products:
#         a=product.find('a')
#         url = "https://www.lcwaikiki.kz" + a.get('href')
#         id = a.get('data-optionid')
#         product_title = a.get('title')
#         data.append({
#             'id товара': id,
#             'ссылка': url,
#             'название товара': product_title
#         })
#     with open('iii.json', 'w') as file:
#         json.dump(data, file, indent=4, ensure_ascii=False)


#     return data


# # Запуск кода (Уникальна)
# def main():
#     url = 'https://www.lcwaikiki.kz/ru-RU/KZ/tag/tshirt-7-5'
#     header = {
#         'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0"
#     }

#     html = get_html(url, header)
#     soup = proccessing(html)
#     with open("nurai.html",'w', encoding="utf-8") as file:
#         file.write(str(soup))

#     print(soup)


# main()





import os
import requests
from bs4 import BeautifulSoup
import json
os.system("clear")


# Получения HTML (Уникальна)
def get_html(url, header):
    response = requests.get(url, headers=header)

    if response.status_code != 200:
        return f"Error: {response.status_code}"
    else:
        return response.text


# Обработка HTML
def proccessing(html):
    soup = BeautifulSoup(html, "lxml").find('div',{'class':"product-grid"})
    products = soup.find_all('div',{'class':"product-card"})
    data = []
    for product in products:
        a=product.find('a')
        url = "https://www.lcwaikiki.kz" + a.get('href')
        id = a.get('data-optionid')
        price = a.find('div',{"class" : "product-price"}).find(
            'span', {'class': 'product-price__price'}).text
        product_title = a.get('title')
        data.append({
            'id товара': id,
            'ссылка': url,
            'название товара': product_title,
            'цена': price.replace(' '," ")
        })
    with open('toys.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


    return data


# Запуск кода (Уникальна)
def main():
    # page= input('выберите страницу')
    data = []

    header = {
            'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0"
        }
    for page in range(1,10):
        url = f'https://www.lcwaikiki.kz/ru-RU/KZ/tag/tshirt-7-5?PageIndex={page}'
        if page<2:
            url = 'https://www.lcwaikiki.kz/ru-RU/KZ/tag/tshirt-7-5'

        html = get_html(url, header)
        soup = proccessing(html)
        data.extend(soup)
        print(f'page: {page} | {url}')
        with open("nurai.html",'w', encoding="utf-8") as file:
            file.write(str(soup))

        # print(soup)


main()