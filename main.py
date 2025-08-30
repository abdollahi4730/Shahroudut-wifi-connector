import re
from requests import get
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright._impl._errors import TimeoutError as PlaywrightTimeoutError
from Bot.settings import settings

def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=settings.headless)
    page = browser.new_page()
    page.goto('http://wifi.shahroodut/login', wait_until='networkidle')
    if 'Welcome' not in page.text_content('body'):
        username_loc = page.get_by_role("textbox", name="نام کاربری").click()
        page.get_by_role("textbox", name="نام کاربری").fill(settings.username)
        page.get_by_role("textbox", name="رمز ورود").click()
        page.get_by_role("textbox", name="رمز ورود").fill(settings.password)
        page.get_by_role("button", name="ورود").click()
        page.goto("http://wifi.shahroodut/status")
        print('Connect Successful!')
    else:
        print('Already connected!')

    browser.close()

    resp = get('https://icanhazip.com')
    print(f"Your ip address: {resp.text}")


if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)
