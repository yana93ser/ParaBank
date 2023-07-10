from allure_commons._allure import attach
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
selenoid_capabilities = {
    "browserName": "chrome",
    "browserVersion": "100.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True
    }
}

options.capabilities.update(selenoid_capabilities)
driver = webdriver.Remote(
    command_executor="https://user1%1234@selenoid:autotests.cloud/wd/hub",
    options=options)

browser.config.driver = driver

attach.add_html(browser)
attach.add_screenshot(browser)
attach.add_logs(browser)
attach.add_video(browser)
browser.quit()
