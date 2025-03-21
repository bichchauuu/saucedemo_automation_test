from behave import given, when, then

@given('I am on the login page')
def step_impl(context):
    context.browser.get('https://www.saucedemo.com')

@when('I enter "{username}" and "{password}"')
def step_impl(context, username, password):
    context.browser.find_element_by_id('user-name').send_keys(username)
    context.browser.find_element_by_id('password').send_keys(password)

@when('I click the login button')
def step_impl(context):
    context.browser.find_element_by_id('login-button').click()

@then('I should see the products page')
def step_impl(context):
    assert context.browser.current_url == 'https://www.saucedemo.com/inventory.html'