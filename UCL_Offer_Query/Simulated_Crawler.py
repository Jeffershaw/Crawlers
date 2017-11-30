
from selenium import webdriver

executable_path = r"C:\Users\Jeff\Desktop\phantomjs-2.1.1-windows\bin\phantomjs"
driver = webdriver.PhantomJS(executable_path)
driver.get("https://evision.ucl.ac.uk/urd/sits.urd/run/siw_lgn")
account = driver.find_element_by_name("MUA_CODE.DUMMY.MENSYS.1")
password = driver.find_element_by_name("PASSWORD.DUMMY.MENSYS.1")
account.send_keys("your account")
password.send_keys("pass")
lgn = driver.find_element_by_name("BP101.DUMMY_B.MENSYS.1")
lgn.click()
driver.page_source