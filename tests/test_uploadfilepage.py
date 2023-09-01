import os

import pytest
from pages.upload_file_page import UploadFilePage


@pytest.mark.parametrize("file", [(os.path.join(os.getcwd(), "resources\\qwe.jpg"))])
def test_uploadfilepage(driver, file):
    page = UploadFilePage(driver, "https://www.lambdatest.com/selenium-playground/upload-file-demo")
    page.open()
    page.input_file(file)
    assert page.verify_uploaded_file()
