from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

@given('the user opens the saucedemo website')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()

@when('the user logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()

@then('the user adds the first product to the cart')
def step_impl(context):
    context.product_name = context.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    context.product_desc = context.driver.find_element(By.CLASS_NAME, "inventory_item_desc").text
    context.product_price = context.driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    context.driver.find_element(By.CLASS_NAME, "btn_inventory").click()

@then('the button changes from \'Add to cart\' to \'Remove\'')
def step_impl(context):
    button_text = context.driver.find_element(By.CLASS_NAME, "btn_inventory").text
    assert button_text == "Remove"

@then('the cart icon badge count updates to 1')
def step_impl(context):
    badge_count = context.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge_count == "1"

@when('the user navigates to the Cart screen')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

@then('the product name, description, and price displayed are correct')
def step_impl(context):
    cart_name = context.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    cart_desc = context.driver.find_element(By.CLASS_NAME, "inventory_item_desc").text
    cart_price = context.driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    assert cart_name == context.product_name
    assert cart_desc == context.product_desc
    assert cart_price == context.product_price

@when('the user clicks the Checkout button')
def step_impl(context):
    context.driver.find_element(By.ID, "checkout").click()

@when('the user fills in the required unique information and clicks continue')
def step_impl(context):
    unique_num = str(random.randint(1000, 9999))
    context.driver.find_element(By.ID, "first-name").send_keys("Test" + unique_num)
    context.driver.find_element(By.ID, "last-name").send_keys("User" + unique_num)
    context.driver.find_element(By.ID, "postal-code").send_keys(unique_num)
    context.driver.find_element(By.ID, "continue").click()

@then('the product name, description, and price on the Overview screen are correct')
def step_impl(context):
    ov_name = context.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    ov_desc = context.driver.find_element(By.CLASS_NAME, "inventory_item_desc").text
    ov_price = context.driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    assert ov_name == context.product_name
    assert ov_desc == context.product_desc
    assert ov_price == context.product_price

@when('the user clicks the Finish button')
def step_impl(context):
    context.driver.find_element(By.ID, "finish").click()

@then('the Checkout: Complete! page is displayed')
def step_impl(context):
    complete_text = context.driver.find_element(By.CLASS_NAME, "complete-header").text
    assert complete_text == "Checkout: Complete!"
    context.driver.quit()
