from behave import *
import time


@given('a user is in the search page')
def step_impl(context):
    context.searchPage.navigate()
    time.sleep(3)


@when('the user filters the car model and the user sorts the price higher to lower')
def step_impl(context):
    context.searchPage.filter_model()
    time.sleep(3)
    context.searchPage.filter_model_year()
    time.sleep(3)
    context.searchPage.sort()
    time.sleep(3)
    context.searchPage.sort_price()
    time.sleep(3)


@then('verify the filtered and sorted data')
def step_impl(context):
    context.searchPage.verify_model()

