import pytest

from main.pages.file_download_page.file_download_page import FileDownloadPage
from tests.base_test import BaseTest


@pytest.mark.smoke
class TC0012UserIsAbleToDownloadFilesTest(BaseTest):
    file_download_page = FileDownloadPage()

    def test_user_is_able_to_download_files(self):
        self.site \
            .click_on_link("File Download")

        self.file_download_page \
            .the_page_url_contains("download") \
            .the_element_text_equals(self.file_download_page.HEADERS_PAGE_ELEMENT(), "File Downloader") \
            .the_elements_are_displayed(self.file_download_page.FILES_ELEMENTS()) \
            .click_on_files_links()
