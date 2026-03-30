from playwright.sync_api import sync_playwright

if __name__ == '__main__':
    with sync_playwright() as p:
        brower=p.chromium.launch()
        page=brower.new_page()
        page.goto("https://www.baidu.com")
        locater=page.get_by_text("问题")
        #byrole=qqpage.get_by_role('pagedescription')  
        print(locater.inner_text())
        brower.close()
