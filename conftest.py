import pytest
from selenium import webdriver
from colorama import Fore


def pytest_addoption(parser):
    parser.addoption(
        "--driver",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox"
    )
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="Choose the mode: true or false"
    )


@pytest.fixture(scope="function")
def driver(request):
    driver_name = request.config.getoption("driver")
    headless = request.config.getoption("headless")
    if driver_name == "chrome":
        print(Fore.LIGHTYELLOW_EX + "\nStarting chrome driver ...")
        opt = webdriver.ChromeOptions()
        if headless == "true":
            opt.add_argument("--headless")
        driver = webdriver.Chrome(options=opt)
    elif driver_name == 'firefox':
        print(Fore.LIGHTYELLOW_EX + "\nStarting firefox driver ...")
        opt = webdriver.FirefoxOptions()
        if headless == "true":
            opt.add_argument("--headless")
        driver = webdriver.Firefox(options=opt)
    else:
        raise pytest.UsageError("\n--driver should be chrome or firefox")
    yield driver
    print(Fore.LIGHTYELLOW_EX + "\nQuiting driver ...")
    driver.quit()
