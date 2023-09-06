from pages.DataTableDownloadPage import DataTableDownloadPage


def test_datatabledownloadpage(driver):
    page = DataTableDownloadPage(driver, "table-data-download-demo")
    page.open()
    page.copy_table()
    assert page.table_is_copied()
    page.wait(2)
    page.csv_download()
    page.xlsx_download()
    page.pdf_download()
    page.wait(1)
    page.open_and_switch_print_version()
    assert page.print_version_is_existed()
    assert page.pdf_is_dowloaded()
    assert page.xlsx_is_dowloaded()
    assert page.csv_is_dowloaded()
    page.switch_to_main_window()
