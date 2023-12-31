import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kuzminovig')
def test_selene():
    browser.open('https://github.com')

    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('eroshenkoam/allure-example')
    browser.element('#query-builder-test').press_enter()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#76")).should(be.visible)
