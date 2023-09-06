import os

import pytest
from pages.UploadFilePage import UploadFilePage


@pytest.mark.parametrize("file", [(os.path.join(os.getcwd(), "resources\\qwe.jpg"))])
def test_uploadfilepage(driver, file):
    page = UploadFilePage(driver, "upload-file-demo")
    page.open()
    page.input_file(file)
    assert page.file_is_uploaded()
