import pytest
import allure
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

def test_example(browser):
    with allure.step("Open Example.com"):
        browser.goto("https://example.com")

    try:
        with allure.step("Verify Page Title"):
            assert "Wrong Title" in browser.title()  # Intentional failure
    except AssertionError:
        screenshot_path = "allure-results/screenshot.png"
        browser.screenshot(path=screenshot_path)  # Capture screenshot
        allure.attach.file(screenshot_path, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
        raise  # Re-raise the assertion error