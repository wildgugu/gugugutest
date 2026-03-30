from playwright.sync_api import sync_playwright


url="www.baidu.com"
if __name__ == '__main__':
    # 使用sync_playwright上下文管理器
    with sync_playwright() as p:
        # 启动Firefox浏览器
        browser =p.firefox.launch()
        # 创建一个新页面
        page = browser.new_page()
        # 导航到指定URL
        page.goto(f"http://{url}")
        # 定位ID为chat-submit-button的元素
        locator_a=page.locator("#chat-submit-button")
        # 定位ID为s-top-left下的target属性包含blank的子元素
        locator_b=page.locator('#s-top-left>[target*="blank"]')
        # 定位href属性包含chat，有target属性，class属性以guide开头的元素
        locator_c=page.locator('[href*="chat"][target][class^=guide]')
        # 打印locator_c元素的内部文本
        print(locator_c.inner_text())
        # 打印locator_b所有元素的内部文本列表
        print(locator_b.all_inner_texts())
        # 以下两行被注释，分别是获取第一个元素的内部文本和获取索引为0的元素的内部文本
        #locator_b.first.inner_text()
        #locator_b.nth(0).inner_text()
        # 打印locator_a元素的内部文本
        print(locator_a.inner_text())
        # 打印页面的标题
        print(page.title())
        # 关闭浏览器
        browser.close()

    #:nth-of-type(n)选择器匹配属于其父元素的特定类型的第n个子元素。
    #:nth-child(n)选择器匹配属于其父元素的第n个子元素。
    #:nth-last-of-type(n)选择器匹配属于其父元素的特定类型的倒数第n个子元素。
    #:nth-last-child(n)选择器匹配属于其父元素的倒数第n个子元素。