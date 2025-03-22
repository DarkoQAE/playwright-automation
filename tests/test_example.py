import pytest
import allure
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Change to True
        yield browser
        browser.close()


def test_example(browser):
    page = browser.new_page()  # Open a new page
    with allure.step("Open Example.com"):
        page.goto("https://example.com")

    try:
        with allure.step("Verify Page Title"):
            assert "Example Domain" in page.title()  # Correct title
    except AssertionError:
        screenshot_path = "allure-results/screenshot.png"
        page.screenshot(path=screenshot_path)  # Use page.screenshot(), not browser.screenshot()
        allure.attach.file(screenshot_path, name="screenshot", attachment_type=allure.attachment_type.PNG)
        raise  # Re-raise the error so pytest marks it as failed