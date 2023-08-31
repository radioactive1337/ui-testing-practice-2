import pytest
from selenium import webdriver
from colorama import Fore
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption("--headless", action="store", default="false", help="Choose the mode: true or false")


@pytest.fixture(scope="session")
def driver(request):
    driver_name = request.config.getoption("driver")
    headless = request.config.getoption("headless")
    driver = None
    if driver_name == "chrome":
        print(Fore.YELLOW + "\n----- Starting chrome driver ...")
        opt = webdriver.ChromeOptions()
        if headless == "true":
            opt.add_argument("--headless")
        driver = webdriver.Chrome(options=opt)
    elif driver_name == 'firefox':
        print(Fore.YELLOW + "\n----- Starting firefox driver ...")
        opt = webdriver.FirefoxOptions()
        if headless == "true":
            opt.add_argument("--headless")
        driver = webdriver.Firefox(options=opt)
    else:
        raise pytest.UsageError("--driver should be chrome or firefox")
    yield driver
    print(Fore.YELLOW + "\n----- Quiting driver ...")
    driver.quit()
