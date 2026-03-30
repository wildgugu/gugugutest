from playwright.sync_api import sync_playwright

if __name__== '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://nga.178.com')
        page.wait_for_timeout(1500)
        page.set_viewport_size({'width': 1440, 'height': 720})
        print(page.content())
        print(page.title())
        page.get_by_role('link',name="cs:go").click()
        page.wait_for_timeout(1500)
        page.go_back()
        page.wait_for_timeout(1500)
        #page.go_forward()
        browser.close()
