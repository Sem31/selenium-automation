from selenium import webdriver
import pytest
import os
import sys
# from _pytest.runner import runtestprotocol


@pytest.fixture
def browser(request):
    sauce_username = username
    sauce_access_key = access-key
    remote_url = "https://ondemand.saucelabs.com:443/wd/hub"

    sauceOptions = {
        'screenResolution': '1280x768',
        'seleniumVersion': '3.141.59',
        'build': 'verizon ui-automation',
        'name': 'ui-automations',
        'username': sauce_username,
        'accessKey': sauce_access_key
    }

    desired_cap = {
        'platformName': 'Windows 10',
        'browserName': 'chrome',
        'browserVersion': 'latest',
        'sauce:options': sauceOptions
    }
    

    # This creates a webdriver object to send to Sauce Labs including the desired capabilities
    driver = webdriver.Remote(remote_url, desired_capabilities=desired_cap)
    yield driver
    # This is where you tell Sauce Labs to stop running tests on your behalf.
    # It's important so that you aren't billed after your test finishes.
    driver.quit()


# @pytest.fixture
# def browser():
#     os.chdir('..')
#     path = os.getcwd() + '/driver/chromedriver'
#     print(path)
#     driver = webdriver.Chrome(executable_path =path)
#     yield driver
#     driver.quit()

class BaseTest(object):

    def setup_class(self):
        print('start class')

    def teardown_class(self):
        print('end class')
