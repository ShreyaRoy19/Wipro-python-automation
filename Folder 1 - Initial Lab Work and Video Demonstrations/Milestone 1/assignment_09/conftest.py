
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    print("\nOpening browser cleanly...")
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    yield driver  
    
    print("\nClosing browser cleanly...")
    driver.quit() 


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    
  
    extras = getattr(report, "extras", [])
    
    if report.when == "call":
        if report.failed and "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            # Capture base64 screenshot to embed directly in the HTML file
            screenshot = driver.get_screenshot_as_base64()
            extras.append(pytest_html.extras.image(screenshot, 'Failed Screenshot'))
        
        report.extras = extras
