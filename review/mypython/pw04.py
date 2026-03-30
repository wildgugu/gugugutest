from playwright.sync_api import sync_playwright

if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context=browser.new_context()
        page = context.new_page()
        page.goto('https://www.baidu.com')
        page.get_by_role("link", name="贴吧").click()
        page.wait_for_timeout(1000)
        newpage= context.pages[1]
        print(newpage.title())
        newpage.wait_for_timeout(1000)
        page.bring_to_front()
        newpage.wait_for_timeout(1000)
        newpage.close()
        newpage.wait_for_timeout(1000)
        browser.close()