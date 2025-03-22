from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = "input[name='email']"
        self.password_field = "input[name='password']"
        self.login_button = "button[type='submit']"
        self.error_message = "div[role='alert']"  # Update if needed
        self.dashboard_url = "https://dev.filestack.com/apps"  # Update to actual login URL

    def navigate(self):
        """ Open the login page """
        self.page.goto("https://dev.filestack.com/login")

    def login(self, username: str, password: str):
        """ Enter credentials and submit the form """
        self.page.fill(self.username_field, username)
        self.page.fill(self.password_field, password)
        self.page.click(self.login_button)
        


    def is_logged_in(self):
        print("🔹 Checking if login was successful...")

        try:
            self.page.wait_for_selector("#app", timeout=30000)  # Ensure this exists
            print(f"✅ Login successful! Current URL: {self.page.url}")
            return True
        except TimeoutError:
            print(f"❌ Timeout! Page URL: {self.page.url}")
            return False

    def get_error_message(self):
        """Wait for and return the login error message."""
    
        self.page.wait_for_timeout(2000)  # Small wait before checking error
        error_locator = self.page.locator("div.toast-msg-container.bg-special-merlotred")  # Updated selector
        error_locator.wait_for(state="visible", timeout=20000)  # Wait for error to appear
        return error_locator.inner_text()



