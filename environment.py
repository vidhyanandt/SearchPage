from web.chrome_browser import Browser
from drivers.AUTO1_Search import SearchPage


# before all will work before all the scenario
def before_all(context):
    context.chrome_browser = Browser()
    context.searchPage = SearchPage()


# after all will work after all the scenario
def after_all(context):
    context.chrome_browser.close()
