from selenium import webdriver
import smtplib
from lxml import etree

def chomp(x):
    if x.endswith("\r\n"): return x[:-2]
    if x.endswith("\n"): return x[:-1]
    return x

def extract_account_info():
    config = open("account.config","r")
    dict = {}
    for line in config:
        dict[line.split(':')[0]] = chomp(line.split(':')[1])
    config.close()
    return dict

def send_result_via_email(email, password, result):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    print('successfully login')
    server.sendmail(email, email, result.encode('utf8'))
    print('results sent')
    server.quit()

def get_result(page):
    results = page.xpath("//p[@class='sv-text-center']")
    str = ''
    for result in results:
        str += etree.tostring(result,method="text") + '\n'
    return str

dict = extract_account_info()
your_executable_path = dict['phantomjs_path']
your_username = dict['username']
your_password = dict['password']
your_gmail = dict['gmail']
your_gmail_password = dict['gmail_password']
driver = webdriver.PhantomJS(your_executable_path)
driver.get("https://evision.ucl.ac.uk/urd/sits.urd/run/siw_lgn")
account = driver.find_element_by_name("MUA_CODE.DUMMY.MENSYS.1")
password = driver.find_element_by_name("PASSWORD.DUMMY.MENSYS.1")
account.send_keys(your_username)
password.send_keys(your_password)
lgn = driver.find_element_by_name("BP101.DUMMY_B.MENSYS.1")
lgn.click()
page =etree.HTML(driver.page_source)
results = get_result(page)
send_result_via_email(your_gmail, your_gmail_password, results)
