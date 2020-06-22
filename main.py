import csv
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def parse_level_4(item):
    driver.get(item)
    time.sleep(0.15)

    links = driver.find_elements_by_xpath("//div[@class='shopAll']/a")

    if links:
        for link in links:
            name_to_list = []
            name = link.get_attribute('text')
            name = name.replace('Shop ', '')
            link = link.get_attribute('href')
            if link not in categories_parsed:
                print(link)
                print(name)
                categories_parsed_names.append(name)
                categories_parsed.append(link)
                name_to_list.append(name)
                name_to_list.insert(0, ' ')
                name_to_list.insert(0, ' ')
                name_to_list.insert(0, ' ')
                name_to_list.insert(0, ' ')
                with open('Structure.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(name_to_list)
            else:
                print('Ignored {}'.format(link))
            time.sleep(0.1)

    else:
        links = driver.find_elements_by_xpath("//div[@class='ag ag-category-grid box']/a")
        for link in links:
            name_to_list = []
            name = link.get_attribute('title')
            link = link.get_attribute('href')
            if link not in categories_parsed:
                print(link)
                print(name)
                categories_parsed_names.append(name)
                categories_parsed.append(link)
                name_to_list.append(name)
                name_to_list.insert(0, ' ')
                name_to_list.insert(0, ' ')
                name_to_list.insert(0, ' ')
                name_to_list.insert(0, ' ')
                with open('Structure.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(name_to_list)
            else:
                print('Ignored {}'.format(link))
            time.sleep(0.1)

    driver.get(item)
    links = driver.find_elements_by_xpath("//span[@class='grid-text']/h2")
    if links:
        for link in links:
            name_to_list = []
            name = link.text
            name_to_list.append(name)
            name_to_list.insert(0, ' ')
            name_to_list.insert(0, ' ')
            name_to_list.insert(0, ' ')
            name_to_list.insert(0, ' ')
            if name not in categories_parsed:
                categories_parsed_names.append(name)
                with open('Structure.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(name_to_list)
                time.sleep(0.15)
            else:
                print('Ignored {}'.format(link))
            time.sleep(0.15)

    driver.execute_script("window.history.go(-1)")
    time.sleep(0.2)


def parse_level_3(item):
    driver.get(item)
    time.sleep(0.5)

    links = driver.find_elements_by_xpath("//span[contains(@class,'grid-text')]/div[@class='shopAll']/a")
    cats_or_prods = driver.find_elements_by_xpath("//div[contains(@class,'shopAll')]/p")

    if links:
        names_level_3 = []
        links_level_3 = []
        cats_or_prods_list_level_3 = []

        for link, cat_or_prod in zip(links, cats_or_prods):
            cat_or_prod_text = cat_or_prod.text
            cats_or_prods_list_level_3.append(cat_or_prod_text)
            name = link.get_attribute('text')
            name = name.replace('Shop ', '')
            names_level_3.append(name)
            link_level_3 = link.get_attribute('href')
            links_level_3.append(link_level_3)

        for name, link, cat_or_prod in zip(names_level_3, links_level_3, cats_or_prods_list_level_3):
            if link not in categories_parsed:
                name_to_list = []
                time.sleep(0.15)
                print(link)
                print(name)
                print(cat_or_prod)
                categories_parsed_names.append(name)
                categories_parsed.append(link)
                name_to_list.append(name)
                name_to_list.insert(0, ' ')
                name_to_list.insert(0, ' ')
                name_to_list.insert(0, ' ')
                with open('Structure.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(name_to_list)
                if 'Products' not in cat_or_prod:
                    if 'PRODUCTS' not in cat_or_prod:
                        print('Parsing {}'.format(name))
                        parse_level_4(link)
                time.sleep(0.15)
            else:
                print('Ignored {}'.format(link))

    else:
        links = driver.find_elements_by_xpath("//div[contains(@class,'grid__text ')]/a")
        if links:
            name_tags = driver.find_elements_by_xpath("//div[contains(@class,'grid__text ')]/a/h2")
            cats_or_prods = driver.find_elements_by_xpath("//div[contains(@class,'grid__text ')]/a/div")
            names_level_3 = []
            links_level_3 = []
            cats_or_prods_list_level_3 = []

            for name_tag, link, cat_or_prod in zip(name_tags, links, cats_or_prods):
                cat_or_prod_text = cat_or_prod.text
                cats_or_prods_list_level_3.append(cat_or_prod_text)
                name = name_tag.text
                names_level_3.append(name)
                link_level_3 = link.get_attribute('href')
                links_level_3.append(link_level_3)

            for name, link, cat_or_prod in zip(names_level_3, links_level_3, cats_or_prods_list_level_3):
                if link not in categories_parsed:
                    name_to_list = []
                    time.sleep(0.15)
                    print(link)
                    print(name)
                    print(cat_or_prod)
                    categories_parsed_names.append(name)
                    categories_parsed.append(link)
                    name_to_list.append(name)
                    name_to_list.insert(0, ' ')
                    name_to_list.insert(0, ' ')
                    name_to_list.insert(0, ' ')
                    with open('Structure.csv', 'a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(name_to_list)
                    if 'Products' not in cat_or_prod:
                        if 'PRODUCTS' not in cat_or_prod:
                            print('Parsing {}'.format(name))
                            parse_level_4(link)
                    time.sleep(0.15)
                else:
                    print('Ignored {}'.format(link))
        else:
            links = driver.find_elements_by_xpath("//div[@class='ag ag-category-grid box']/a")
            for link in links:
                name_to_list = []
                name = link.get_attribute('title')
                link = link.get_attribute('href')
                if link not in categories_parsed:
                    print(link)
                    print(name)
                    categories_parsed_names.append(name)
                    categories_parsed.append(link)
                    name_to_list.append(name)
                    name_to_list.insert(0, ' ')
                    name_to_list.insert(0, ' ')
                    name_to_list.insert(0, ' ')
                    with open('Structure.csv', 'a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(name_to_list)
                else:
                    print('Ignored {}'.format(link))
                time.sleep(0.15)


    driver.get(item)
    links = driver.find_elements_by_xpath("//span[@class='grid-text']/h2")
    if links:
        for link in links:
            name_to_list = []
            name = link.text
            name_to_list.append(name)
            name_to_list.insert(0, ' ')
            name_to_list.insert(0, ' ')
            name_to_list.insert(0, ' ')
            if name not in categories_parsed:
                categories_parsed_names.append(name)
                with open('Structure.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(name_to_list)
                time.sleep(0.15)
            else:
                print('Ignored {}'.format(link))
            time.sleep(0.15)

    driver.execute_script("window.history.go(-1)")
    time.sleep(0.35)


def parse_level_2(item):
    driver.get(item)
    time.sleep(0.35)

    links = driver.find_elements_by_xpath("//span[contains(@class,'grid-text')]/div[@class='shopAll']/a")
    cats_or_prods = driver.find_elements_by_xpath("//div[contains(@class,'shopAll')]/p")

    if links:
        names_level_2 = []
        links_level_2 = []
        cats_or_prods_list_level_2 = []

        for link, cat_or_prod in zip(links, cats_or_prods):
            cat_or_prod_text = cat_or_prod.text
            cats_or_prods_list_level_2.append(cat_or_prod_text)
            name = link.get_attribute('text')
            name = name.replace('Shop ', '')
            names_level_2.append(name)
            link_level_2 = link.get_attribute('href')
            links_level_2.append(link_level_2)

        for name, link, cat_or_prod in zip(names_level_2, links_level_2, cats_or_prods_list_level_2):
            if link not in categories_parsed:
                name_to_list = []
                time.sleep(0.15)
                print(link)
                print(name)
                print(cat_or_prod)
                categories_parsed_names.append(name)
                categories_parsed.append(link)
                name_to_list.append(name)
                name_to_list.insert(0, ' ')
                name_to_list.insert(0, ' ')
                with open('Structure.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(name_to_list)
                if 'Products' not in cat_or_prod:
                    if 'PRODUCTS' not in cat_or_prod:
                        print('Parsing {}'.format(name))
                        parse_level_3(link)
                time.sleep(0.15)
            else:
                print('Ignored {}'.format(link))

    else:
        links = driver.find_elements_by_xpath("//div[contains(@class,'grid__text ')]/a")
        if links:
            name_tags = driver.find_elements_by_xpath("//div[contains(@class,'grid__text ')]/a/h2")
            cats_or_prods = driver.find_elements_by_xpath("//div[contains(@class,'grid__text ')]/a/div")
            names_level_2 = []
            links_level_2 = []
            cats_or_prods_list_level_2 = []

            for name_tag, link, cat_or_prod in zip(name_tags, links, cats_or_prods):
                cat_or_prod_text = cat_or_prod.text
                cats_or_prods_list_level_2.append(cat_or_prod_text)
                name = name_tag.text
                names_level_2.append(name)
                link_level_2 = link.get_attribute('href')
                links_level_2.append(link_level_2)

            for name, link, cat_or_prod in zip(names_level_2, links_level_2, cats_or_prods_list_level_2):
                if link not in categories_parsed:
                    name_to_list = []
                    time.sleep(0.15)
                    print(link)
                    print(name)
                    print(cat_or_prod)
                    categories_parsed_names.append(name)
                    categories_parsed.append(link)
                    name_to_list.append(name)
                    name_to_list.insert(0, ' ')
                    name_to_list.insert(0, ' ')
                    with open('Structure.csv', 'a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(name_to_list)
                    if 'Products' not in cat_or_prod:
                        if 'PRODUCTS' not in cat_or_prod:
                            print('Parsing {}'.format(name))
                            parse_level_3(link)
                    time.sleep(0.15)
                else:
                    print('Ignored {}'.format(link))
        else:
            links = driver.find_elements_by_xpath("//div[@class='ag ag-category-grid box']/a")
            for link in links:
                name_to_list = []
                name = link.get_attribute('title')
                link = link.get_attribute('href')
                if link not in categories_parsed:
                    print(link)
                    print(name)
                    categories_parsed_names.append(name)
                    categories_parsed.append(link)
                    name_to_list.append(name)
                    name_to_list.insert(0, ' ')
                    name_to_list.insert(0, ' ')
                    with open('Structure.csv', 'a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(name_to_list)
                else:
                    print('Ignored {}'.format(link))
                time.sleep(0.15)

    driver.get(item)
    links = driver.find_elements_by_xpath("//span[@class='grid-text']/h2")
    if links:
        for link in links:
            name_to_list = []
            name = link.text
            name_to_list.append(name)
            name_to_list.insert(0, ' ')
            name_to_list.insert(0, ' ')
            if name not in categories_parsed:
                categories_parsed_names.append(name)
                with open('Structure.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(name_to_list)
                time.sleep(0.15)
            else:
                print('Ignored {}'.format(link))
            time.sleep(0.15)

    driver.execute_script("window.history.go(-1)")
    time.sleep(0.35)


def parse_level_1(item):
    driver.get(item)
    time.sleep(0.35)

    links = driver.find_elements_by_xpath("//div[contains(@class,'shopAll')]/a")
    cats_or_prods = driver.find_elements_by_xpath("//div[contains(@class,'shopAll')]/p")

    if links:
        names_level_1 = []
        links_level_1 = []
        cats_or_prods_list_level_1 = []

        for link, cat_or_prod in zip(links, cats_or_prods):
            cat_or_prod_text = cat_or_prod.text
            cats_or_prods_list_level_1.append(cat_or_prod_text)
            name = link.get_attribute('text')
            name = name.replace('Shop ', '')
            names_level_1.append(name)
            link_level_1 = link.get_attribute('href')
            links_level_1.append(link_level_1)

        for name, link, cat_or_prod in zip(names_level_1, links_level_1, cats_or_prods_list_level_1):
            if link not in categories_parsed:
                name_to_list = []
                time.sleep(0.15)
                print(link)
                print(name)
                print(cat_or_prod)
                categories_parsed_names.append(name)
                categories_parsed.append(link)
                name_to_list.append(name)
                name_to_list.insert(0, ' ')
                with open('Structure.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(name_to_list)
                if 'Products' not in cat_or_prod:
                    if 'PRODUCTS' not in cat_or_prod:
                        print('Parsing {}'.format(name))
                        parse_level_2(link)
                time.sleep(0.15)
            else:
                print('Ignored {}'.format(link))

    else:
        links = driver.find_elements_by_xpath("//div[contains(@class,'grid__text ')]/a")
        name_tags = driver.find_elements_by_xpath("//div[contains(@class,'grid__text ')]/a/h2")
        cats_or_prods = driver.find_elements_by_xpath("//div[contains(@class,'grid__text ')]/a/div")
        names = []
        links_level_1 = []
        cats_or_prods_list = []

        for name_tag, link, cat_or_prod in zip(name_tags, links, cats_or_prods):
            cat_or_prod_text = cat_or_prod.text
            cats_or_prods_list.append(cat_or_prod_text)
            name = name_tag.text
            names.append(name)
            link_level_1 = link.get_attribute('href')
            links_level_1.append(link_level_1)

        for name, link, cat_or_prod in zip(names, links_level_1, cats_or_prods_list):
            if link not in categories_parsed:
                name_to_list = []
                time.sleep(0.15)
                print(link)
                print(name)
                print(cat_or_prod)
                categories_parsed_names.append(name)
                categories_parsed.append(link)
                name_to_list.append(name)
                name_to_list.insert(0, ' ')
                with open('Structure.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(name_to_list)
                if 'Products' not in cat_or_prod:
                    if 'PRODUCTS' not in cat_or_prod:
                        print('Parsing {}'.format(name))
                        parse_level_2(link)
                time.sleep(0.15)
            else:
                print('Ignored {}'.format(link))

    time.sleep(0.15)

    driver.get(item)
    links = driver.find_elements_by_xpath("//span[@class='grid-text']/h2")
    if links:
        for link in links:
            name_to_list = []
            name = link.text
            name_to_list.append(name)
            name_to_list.insert(0, ' ')
            if name not in categories_parsed:
                categories_parsed_names.append(name)
                with open('Structure.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(name_to_list)
                time.sleep(0.15)
            else:
                print('Ignored {}'.format(link))
            time.sleep(0.15)

    driver.execute_script("window.history.go(-1)")
    time.sleep(0.35)


driver = webdriver.Chrome(r'C:\Users\Lenovo\Downloads\chromedriver_win32\chromedriver')
driver.maximize_window()
driver.get('https://www.webstaurantstore.com/lcnklmkldf')

items = driver.find_elements_by_xpath('//div[@class="error404-browse"]/ul/li/a')

item_hrefs = [] * 23
item_names = [] * 23
for item in items:
    item_hrefs.append(item.get_attribute('href'))
    item_names.append(item.get_attribute('text'))

item_hrefs = item_hrefs
item_names = item_names

categories_parsed = []
categories_parsed_names = []

for href, name in zip(item_hrefs, item_names):
    categories_parsed.append(href)
    categories_parsed_names.append(name)
    print(href)
    print(name)
    name_list = [name]
    with open('Structure.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(name_list)
    time.sleep(0.35)
    parse_level_1(href)
    time.sleep(0.5)