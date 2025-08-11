import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_type", action="store", default="chrome", help="Initializing browser"
    )


@pytest.fixture(scope="function")
def browser_invoke(request):
    global driver
    browser_type = request.config.getoption("browser_type").lower()
    service_obj = Service()

    if browser_type == "chrome":
        driver = webdriver.Chrome(service=service_obj)
    elif browser_type == "firefox":
        driver = webdriver.Firefox(service=service_obj)
    elif browser_type == "edge":
        driver = webdriver.Edge(service=service_obj)
    else:
        raise ValueError(f"Unsupported browser: {browser_type}")

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    # Ensure the reports directory exists
    reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if report.failed and not xfail:
            # Generate the file name by removing the directory path from the nodeid
            file_name = os.path.join(reports_dir, f"{os.path.basename(report.nodeid.replace('::', '_'))}.png")
            print(f"Test failed, capturing screenshot: {file_name}")
            _capture_screenshot(file_name)

            # Use an absolute path for embedding the screenshot in the report
            absolute_path = os.path.abspath(file_name)
            print(f"Absolute path for report: {absolute_path}")

            # Embed the screenshot HTML into the report
            html = f'<div><img src="file:///{absolute_path}" alt="screenshot" style="width:304px;height:228px;" onclick="window.open(this.src)" align="right"/></div>'
            extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(file_name):
    if driver:
        driver.get_screenshot_as_file(file_name)
    else:
        print("Driver is None, unable to capture screenshot.")
