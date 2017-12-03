from tool.mail import send_mail
from selenium import webdriver
from lxml import etree
executable_path = r"C:\Users\Jeff\Desktop\phantomjs-2.1.1-windows\bin\phantomjs"
driver = webdriver.PhantomJS(executable_path)
driver.get("https://evision.ucl.ac.uk/urd/sits.urd/run/siw_lgn")
account = driver.find_element_by_name("MUA_CODE.DUMMY.MENSYS.1")
password = driver.find_element_by_name("PASSWORD.DUMMY.MENSYS.1")
account.send_keys("your account")
password.send_keys("pass")
lgn = driver.find_element_by_name("BP101.DUMMY_B.MENSYS.1")
lgn.click()
page =etree.HTML(driver.page_source)
result = page.xpath("//p[@class='sv-text-center']")
print(result[0]=='Application under assessment')
if(result[1]):
    print(result[1]=='Application under assessment')
