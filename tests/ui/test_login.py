import pytest
import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage  # Ensure this file exists

# Explicitly clear old environment variables before loading new ones
for var in ["USERNAME", "PASSWORD", "INVALID_PASSWORD"]:
    os.environ.pop(var, None)

# Load environment variables from cred.env
load_dotenv("cred.env", override=True)

# Read credentials
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
INVALID_PASSWORD = os.getenv("INVALID_PASSWORD")

# Debugging: Print loaded credentials
print(f"🔹 Loaded Credentials - USERNAME: {USERNAME}, PASSWORD: {PASSWORD}, INVALID_PASSWORD: {INVALID_PASSWORD}")

@pytest.fixture(scope="function")
def browser():
    """ Set up Playwright browser instance """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True when done debugging
        page = browser.new_page()
        yield page
        browser.close()

def test_successful_login(browser):
    login_page = LoginPage(browser)
    login_page.navigate()
    login_page.login(USERNAME, PASSWORD)

    browser.screenshot(path="debug_login.png")  # Take a screenshot

    assert login_page.is_logged_in(), f"❌ Login failed! Current URL: {browser.url}"

def test_unsuccessful_login_wrong_password(browser):
    """ Test login with an incorrect password """
    login_page = LoginPage(browser)
    login_page.navigate()
    login_page.login(USERNAME, INVALID_PASSWORD)

    error_message = login_page.get_error_message()
    assert error_message == "Login Failed", f"❌ Incorrect error message displayed: {error_message}"