import pytest
from selenium import webdriver
from datetime import datetime
import os
from configs.config_handler import ConfigHandler

@pytest.fixture(scope="function")
def browser_setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(ConfigHandler.get_url())
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.instance.driver
        os.makedirs("failure_screenshots", exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        screenshot_file = f"failure_screenshots/{item.name}_{timestamp}.png"
        driver.save_screenshot(screenshot_file)