import pytest

from main.pages.frames_page.frames_page import FramesPage
from main.pages.frames_page.nested_frames_page.nested_frames_page import NestedFramesPage
from main.utils.browser_manager.browser_manager import BrowserManager
from tests.base_test import BaseTest

@pytest.mark.smoke
class TC0015TextInTheNestedFramesIsShownCorrectlyTest(BaseTest):
    frames_page = FramesPage()
    nested_frames_page = NestedFramesPage()

    def test_text_in_the_nested_frames_is_shown_correctly(self):
        _LINK_NAMES = ["Nested Frames", "iFrame"]

        self.site \
            .click_on_link("Frames")

        self.frames_page \
            .the_page_url_contains("frames") \
            .the_element_text_equals(self.frames_page.HEADERS_PAGE_ELEMENTS(), "Frames") \
            .the_elements_in_list_equal(self.frames_page.LINKS_ELEMENTS(), _LINK_NAMES) \
            .click_on_nested_frames_link()

        BrowserManager().switch_to_frame(self.nested_frames_page.MIDDLE_FRAME_SET_ELEMENT())
        BrowserManager().switch_to_frame(self.nested_frames_page.LEFT_FRAME_ELEMENT())

        self.nested_frames_page\
            .the_element_text_equals(self.nested_frames_page.TEXT_ELEMENT(), "LEFT")

        BrowserManager().switch_to_default_content()

        BrowserManager().switch_to_frame(self.nested_frames_page.MIDDLE_FRAME_SET_ELEMENT())
        BrowserManager().switch_to_frame(self.nested_frames_page.MIDDLE_FRAME_ELEMENT())

        self.nested_frames_page \
            .the_element_text_equals(self.nested_frames_page.MIDDLE_TEXT_ELEMENT(), "MIDDLE")

        BrowserManager().switch_to_default_content()
        
        BrowserManager().switch_to_frame(self.nested_frames_page.MIDDLE_FRAME_SET_ELEMENT())
        BrowserManager().switch_to_frame(self.nested_frames_page.RIGHT_FRAME_ELEMENT())

        self.nested_frames_page \
            .the_element_text_equals(self.nested_frames_page.TEXT_ELEMENT(), "RIGHT")
        
        BrowserManager().switch_to_default_content()
        
        BrowserManager().switch_to_frame(self.nested_frames_page.BOTTOM_FRAME_ELEMENT())

        self.nested_frames_page \
            .the_element_text_equals(self.nested_frames_page.TEXT_ELEMENT(), "BOTTOM")
        
        BrowserManager().switch_to_default_content()
