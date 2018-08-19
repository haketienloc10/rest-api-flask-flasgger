from selenium import webdriver

browser = webdriver.PhantomJS("../flask-scrapy/tool/phantomjs");
browser.get("https://tiki.vn/loa-bluetooth-harman-kardon-aura-studio-2-hang-chinh-hang-p896610.html?src=category-page")
element = browser.page_source
print(type(element))
browser.quit()