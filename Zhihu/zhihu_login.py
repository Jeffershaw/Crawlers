from lxml import etree
import requests

base_url = "https://www.zhihu.com"
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
sess = requests.session()
sess.headers = head
page = sess.get(base_url+"/#signin")
x_page = etree.HTML(page.text)
result = x_page.xpath("//input[@name='_xsrf']")
xsrf_value = result[0].values()[-1]
form_data = {"_xsrf":xsrf_value,
             "password":"your pass",
             "captcha_type":"cn",
             "phone_num":"your number"}
result = x_page.xpath("//img[@class='Captcha-image']")
print(result[0].values())
head["X-Xsrftoken"] = xsrf_value
sess.headers = head
main_page = sess.post(url=base_url+"/login/phone_num",data=form_data)

