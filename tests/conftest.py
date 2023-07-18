import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def setup_browser():
    browser.config.base_url = 'https://parabank.parasoft.com/parabank'
    browser.driver.maximize_window()

    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def open():
    browser.open('/')
