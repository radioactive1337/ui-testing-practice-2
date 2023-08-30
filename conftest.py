import pytest
from selenium import webdriver
from colorama import Fore


def pytest_addoption(parser):
    parser.addoption('--driver', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="session")
def driver(request):
    driver_name = request.config.getoption('driver')
    driver = None
    if driver_name == 'chrome':
        print(Fore.YELLOW + '\n----- Starting chrome driver ...')
        driver = webdriver.Chrome()
    elif driver_name == 'firefox':
        print(Fore.YELLOW + '\n----- Starting firefox driver ...')
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError('--driver should be chrome or firefox')
    yield driver
    print(Fore.YELLOW + '\n----- Quiting driver ...')
    driver.quit()
