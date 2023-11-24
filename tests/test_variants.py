from pages.variants_page import VariantsPage


def test_check_logo(driver):
    variants_page = VariantsPage(driver)
    variants_page.log_in()
    logo = variants_page.find_logo()
    assert logo.is_displayed()

def test_check_titles(driver):
    variants_page = VariantsPage(driver)
    variants_page.log_in()

    main_title = variants_page.find_main_title()
    assert main_title.is_displayed()
    assert main_title.text == 'НТЦ ПРОТЕЙ'

    second_title = variants_page.find_second_title()
    assert second_title.is_displayed()
    assert second_title.text == 'Нет, лисичка не логотип Протея, логотип Протея вот такой.'

    third_title = variants_page.find_third_title()
    assert third_title.is_displayed()
    assert third_title.text == 'Лисички нравятся лично автору. Всем фыр ^^'
