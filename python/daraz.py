from marshmallow import pre_dump
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def Chrome(headless=False):
    # add fake user agent
    chrome_options = Options()

    # return webdriver
    # support to get response status and headers
    d = webdriver.DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'performance': 'ALL'}

    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("user-agent={}".format(
    #     fake_useragent.UserAgent().random))
    # chrome_options.add_experimental_option(
    #     'excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(
        executable_path=r'i://clients//chromedriver.exe', options=chrome_options, desired_capabilities=d)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def main(keyword):
    keyword = keyword.replace(' ', '+')
    driver = Chrome(True)
    url = 'https://www.daraz.pk/catalog/?q='+keyword

    driver.get(url)
    # find div with id root
    root = driver.find_element_by_id('root')
    # find div with class product-list

    product_div = root.find_element_by_xpath(
        '//div[@data-qa-locator="general-products"]')
    products_card = product_div.find_elements_by_xpath(
        '//div[@class="gridItem--Yd0sa"]')
    print(len(products_card))

    print("="*30)
    product = product_div.find_elements_by_xpath(
        '//div[@class="inner--SODwy"]')
    title = product_div.find_elements_by_xpath(
        '//div[@class="title--wFj93"]')
    price = product_div.find_elements_by_xpath(
        '//div[@class="price--NVB62"]')
    img_Src = product_div.find_elements_by_xpath(
        '//img[@class="image--WOyuZ "]')
    print(len(title))
    print(len(price))
    print(len(img_Src))

    for i in range(len(title)):
        print("="*30)
        print(title[i].text)
        print(price[i].text)
        print(img_Src[i].get_attribute('src'))
    # print(product.text)


if __name__ == '__main__':
    main("Iphone 12")
