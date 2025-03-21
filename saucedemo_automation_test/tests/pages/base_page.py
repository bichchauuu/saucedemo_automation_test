class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def click(self, *args):
        self.find_element(*args).click()

    def send_keys(self, keys, *args):
        self.find_element(*args).send_keys(keys)

    def get_title(self):
        return self.driver.title

    def wait_for_element(self, *args):
        # Implement wait logic here
        pass

    # Add more common methods as needed for page objects