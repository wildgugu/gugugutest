from playwright.sync_api import sync_playwright

if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page =browser.new_page()
        page.goto('https://www.baidu.com')
        page.locator("#chat-textarea").fill("你好")
        page.get_by_role("button",name="百度一下").click()
        page.wait_for_timeout(3000)
        browser.close()