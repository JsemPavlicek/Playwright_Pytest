import pytest
from playwright.sync_api import sync_playwright

def test_google_title(playwright):
    browser = playwright.chromium.launch(headless= False)
    page = browser.new_page()
    page.goto('https://www.google.com')
    page.wait_for_timeout(5000)
    assert page.title() == 'Google'
    browser.close()

# instalace všech balíčků: pip install pytest pytest-playwright playwright