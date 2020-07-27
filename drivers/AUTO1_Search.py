import os
from selenium.webdriver.common.by import By
from web.chrome_browser import Browser
from datetime import datetime


class SearchPageLocators(object):
    URL = "https://www.autohero.com/de/search/"
    FILTER_MODEL = (By.XPATH, "//span[contains(text(),'Erstzulassung ab')]")
    FILTER_MODEL_YEAR = (By.XPATH, "//option[contains(text(),'2015')]")
    SORT = (By.XPATH, "//select[@name='sort']")
    SORT_PRICE = (By.XPATH, "//option[contains(text(),'Höchster Preis')]")


class SearchPage(Browser):
    # SearchPage Actions

    # NAVIGATING TO THE URL
    def navigate(self):
        self.driver.get(SearchPageLocators.URL)

    # FILTER THE MODEL
    def filter_model(self):
        assert self.driver.find_element(*SearchPageLocators.FILTER_MODEL).is_displayed()
        self.driver.find_element(*SearchPageLocators.FILTER_MODEL).click()

    # FILTER THE MODEL YEAR
    def filter_model_year(self):
        assert self.driver.find_element(*SearchPageLocators.FILTER_MODEL_YEAR).is_displayed()
        self.driver.find_element(*SearchPageLocators.FILTER_MODEL_YEAR).click()

    # SORT THE PRICE
    def sort(self):
        assert self.driver.find_element(*SearchPageLocators.SORT).is_displayed()
        self.driver.find_element(*SearchPageLocators.SORT).click()

    # SORT THE PRICE FROM HIGHEST TO LOWEST
    def sort_price(self):
        assert self.driver.find_element(*SearchPageLocators.SORT_PRICE).is_displayed()
        self.driver.find_element(*SearchPageLocators.SORT_PRICE).click()
        self.driver.refresh()

    # VERIFY THE FILTERED MODEL, PRICE (Assume we are on first page with 24 items)
    def verify_model(self):
        # Declarations
        lis_model = []
        price_trimmed = []
        model_year = []
        lis_price = []
        price_sort = []

        # Loop into the container on the first page
        for i in range(1, 25):
            model = self.driver.find_element_by_xpath("//div[@class='root___2j9X2']//div["
                                                      + str(i) +
                                                      "]//div[1]//a[1]//ul[1]//li[1]").get_attribute("innerText")
            year = self.driver.find_element_by_xpath("//div[@class='root___2j9X2']//div["
                                                     + str(i) +
                                                     "]//div[1]//a[1]//div[3]//div[1]/span").get_attribute("innerText")
            lis_model.append(model)
            lis_price.append(year)

        # Write into the logs
        self.history("The model data fetched from search page " + str(lis_model))
        self.history("The price data fetched from search page " + str(lis_price))

        # Trimming and replacing values
        for i in range(0, len(lis_model)):
            model = str(lis_model[i])
            model_year.append(model[5:len(model)])
            price = str(lis_price[i])
            b = str(price.replace(".", ""))
            price_trimmed.append(b[:-2])

        # Write into the logs
        self.history("The model data trimmed with only year " + str(model_year))
        self.history("The price data trimmed with only number " + str(price_trimmed))

        # Verify the years are in the filtered criteria
        for value in model_year:
            if int(value) < 2015:
                assert False

        # Sorting the list
        price_sort = price_trimmed
        price_sort.sort(reverse=True)

        # Write into the logs
        self.history("The price data sorted with trimmed data " + str(price_sort))

        # Assertion for the model year
        for value in model_year:
            if int(value) < 2015:
                self.history("The non-matched filtered criteria for model is " + str(value))
                assert False

        # Assertion for the price sorting in descending
        if price_trimmed != price_sort:
            self.history("The non-matched sorted criteria for price in the list is " + str(price_trimmed))
            assert False

    # LOGS
    @staticmethod
    def history(logs):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        filehandle = open(os.getcwd() + "/" + "logs.txt", "a")
        filehandle.write(dt_string + " ---- " + logs + '\n')
