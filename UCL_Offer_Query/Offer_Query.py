# -*- coding: utf-8 -*-

#env: python3.6
#unfinished
import requests
from lxml import etree

base_url = "https://evision.ucl.ac.uk/urd/sits.urd/run/siw_lgn"
response = requests.get(base_url)
body = response.text

page = etree.HTML(body)

result = page.xpath("//input[@name='RUNTIME.DUMMY.MENSYS.1']")

head={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Content-Length":"464",
"Content-Type":"application/x-www-form-urlencoded",
"Cookie":"EVISIONID=7F3382D0D3D811E7BFAFA24D05C2DA69; JSESSIONID=A4735C8962C031CC2007B6BD03BC3D84; EVISIONLOGINLANG=""; EVISIONLOGINHTV=""; EVISIONID_TEST=COOKIE_TEST; JSESSIONID=ACEB99D01F28D7EA5E4E8FAC7ECFD84B; _ceg.s=ozq74z; _ceg.u=ozq74z; _ga=GA1.3.1782068710.1507576571; __utma=156947391.1782068710.1507576571.1510443807.1511197099.15; __utmz=156947391.1510003161.8.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)",
"Host":"evision.ucl.ac.uk",
"Origin":"https://evision.ucl.ac.uk",
"Referer":"https://evision.ucl.ac.uk/urd/sits.urd/run/siw_lgn",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}

data = {"%.DUM_MESSAGE.MENSYS.1":"",
"SCREEN_WIDTH.DUMMY.MENSYS.1":"1920",
"SCREEN_HEIGHT.DUMMY.MENSYS.1":"1080",
"%.DUMMY.MENSYS.1":"",
"RUNTIME.DUMMY.MENSYS.1":"2017112823150958%1BD1C9C0096761A669868DB3E5908681FD210B5ABB99260B4BB3F761B20C6C8DF79A86E6F9EBF879D38C98A859B743EE848D413A9BD2436D782847C47B7960015C%1BFA7ED58ED49111E7976AA9065BA039BA%1BNONE",
"PARS.DUMMY.MENSYS.1":"",
"MUA_CODE.DUMMY.MENSYS.1": "your account",
"PASSWORD.DUMMY.MENSYS.1":"your password",
"BP101.DUMMY_B.MENSYS.1":"Log in >>"}

result = page.xpath("//input[@name='%.DUM_MESSAGE.MENSYS.1']")
data["%.DUM_MESSAGE.MENSYS.1"] = result[0].get("value")
result = page.xpath("//input[@name='RUNTIME.DUMMY.MENSYS.1']")
data["RUNTIME.DUMMY.MENSYS.1"] = result[0].get("value")

sess = requests.session()
sess.headers=head
sess.post(base_url,data)
