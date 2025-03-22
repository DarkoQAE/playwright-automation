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
            assert "Wrong Title" in browser.title()  # Intentional failure
    except AssertionError:
        screenshot_path = "allure-results/screenshot.png"
        browser.screenshot(path=screenshot_path)  # Capture screenshot
        allure.attach.file(screenshot_path, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
        raise  # Re-raise the assertion error