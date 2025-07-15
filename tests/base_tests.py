import allure

from pages.elements_page import TextBoxPage


@allure.feature('TextBox')
class TestTextBox:

    @allure.title('Check TextBox')
    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()
