from email.mime.text import MIMEText
from typing import List, Tuple
import json
import smtplib
import socket
import sqlite3
import threading
import time
import urllib.request as req

import bs4

def ncut_crawler() -> Tuple[str, List[str], List[str]]:
    """勤益科大爬蟲，返回公告字串、標題串列、網址串列"""
    # 爬取資料
    url = "https://www.ncut.edu.tw/app/index.php?Action=mobileloadmod&Type=mobile_asso_cg_mstr&Nbr=1002"
    request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    ret_title = []
    ret_url = []
    titles = root.find_all("div", class_="mtitle")
    for title in titles:
        ret_title.append(title.a)
        ret_url.append(title.a["href"])
    # 處理資料
    deal_title = []
    deal_url = []
    ret_ = ""
    title_ = []
    url_ = []
    for i in ret_title:
        for j in i:
            deal_title.append(j.strip())
    for i in ret_url:
        if i.startswith("http"):
            deal_url.append(i)
        else:
            deal_url.append("https://www.ncut.edu.tw" + i)
    for i in range(5):
        ret_ += deal_title[i] + "\n"
        ret_ += deal_url[i] + "\n"
        title_.append(deal_title[i])
        url_.append(deal_url[i])
    return ret_, title_, url_

def ge_crawler() -> Tuple[str, List[str], List[str], List[str]]:
    """基礎通識中心爬蟲，返回公告字串、日期串列、標題串列、網址串列"""
    # 爬取資料
    url = "https://fec.ncut.edu.tw/app/index.php?Action=mobileloadmod&Type=mobile_rcg_mstr&Nbr=94"
    request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    ret_date = root.find_all("i", class_="mdate after")
    ret_title = []
    ret_url = []
    titles = root.find_all("div", class_="mtitle")
    for title in titles:
        ret_title.append(title.a)
        ret_url.append(title.a["href"])
    # 處理資料
    deal_date = []
    deal_title = []
    deal_url = []
    ret_ = ""
    date_ = []
    title_ = []
    url_ = []
    for i in ret_date:
        for j in i:
            deal_date.append(j.strip())
    for i in ret_title:
        for j in i:
            deal_title.append(j.strip())
    for i in ret_url:
        deal_url.append(i)
    for i in range(5):
        ret_ += deal_date[i] + " "
        ret_ += deal_title[i] + "\n"
        ret_ += deal_url[i] + "\n"
        date_.append(deal_date[i])
        title_.append(deal_title[i])
        url_.append(deal_url[i])
    return ret_, date_, title_, url_

def liberal_crawler() -> Tuple[str, List[str], List[str], List[str]]: # 因公告顯示較少 抓取四筆
    """博雅通識中心爬蟲，返回公告字串、日期串列、標題串列、網址串列"""
    # 爬取資料
    url = "https://liberal.ncut.edu.tw/index.php?Lang=zh-tw"
    request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    ret_date = root.find_all("i", class_="mdate before")
    ret_title = []
    ret_url = []
    titles = root.find_all("div", class_="mtitle")
    for title in titles:
        ret_title.append(title.a)
        ret_url.append(title.a["href"])
    # 處理資料
    deal_date = []
    deal_title = []
    deal_url = []
    ret_ = ""
    date_ = []
    title_ = []
    url_ = []
    for i in ret_date:
        for j in i:
            deal_date.append(j.strip())
    for i in ret_title:
        for j in i:
            deal_title.append(j.strip())
    for i in ret_url:
        deal_url.append(i)
    for i in range(4):
        ret_ += deal_date[i] + " "
        ret_ += deal_title[i] + "\n"
        ret_ += deal_url[i] + "\n"
        date_.append(deal_date[i])
        title_.append(deal_title[i])
        url_.append(deal_url[i])
    return ret_, date_, title_, url_

def oaa_crawler() -> Tuple[str, List[str], List[str], List[str], List[str]]: # 因公告更新較快 抓取十筆
    """教務處爬蟲，返回公告字串、日期串列、組別串列、標題串列、網址串列"""
    # 爬取資料
    url = "https://oaa.ncut.edu.tw/app/index.php?Action=mobileloadmod&Type=mobile_rcg_mstr&Nbr=853"
    request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    ret_date = root.find_all("div", class_="d-txt")
    ret_title = []
    ret_url = []
    titles = root.find_all("div", class_="mtitle")
    for title in titles:
        ret_title.append(title.a)
        ret_url.append(title.a["href"])
    # 處理資料
    deal_data = []
    deal_date = []
    deal_source = []
    deal_title = []
    deal_url = []
    ret_ = ""
    date_ = []
    source_ = []
    title_ = []
    url_ = []
    for i in ret_date:
        for j in i:
            if i.index(j) % 3 == 0:
                deal_data.append(j.strip())
    deal_date = [deal_data[i] for i in range(0, len(deal_data), 3)]
    deal_source = [deal_data[i] for i in range(2, len(deal_data), 3)]
    for i in ret_title:
        for j in i:
            deal_title.append(j.strip())
    for i in ret_url:
        deal_url.append(i)
    for i in range(10):
        ret_ += deal_date[i] + " " + deal_source[i] + " "
        ret_ += deal_title[i] + "\n"
        ret_ += deal_url[i] + "\n"
        date_.append(deal_date[i])
        source_.append(deal_source[i])
        title_.append(deal_title[i])
        url_.append(deal_url[i])
    return ret_, date_, source_, title_, url_

def osa_crawler() -> Tuple[str, List[str], List[str]]:
    """學生事務處爬蟲，返回公告字串、標題串列、網址串列"""
    # 爬取資料
    url = "https://osca.ncut.edu.tw/index.php"
    request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    ret_title = []
    ret_url = []
    titles = root.find_all("div", class_="mtitle")
    for title in titles:
        ret_title.append(title.a)
        ret_url.append(title.a["href"])
    # 處理資料
    deal_title = []
    deal_url = []
    ret_ = ""
    title_ = []
    url_ = []
    for i in ret_title:
        for j in i:
            deal_title.append(j.strip())
    for i in ret_url:
        if i.startswith("http"):
            deal_url.append(i)
        else:
            deal_url.append("https://osca.ncut.edu.tw" + i)
    for i in range(24, 29):
        ret_ += deal_title[i] + "\n"
        ret_ += deal_url[i] + "\n"
        title_.append(deal_title[i])
        url_.append(deal_url[i])
    return ret_, title_, url_

def oga_crawler() -> Tuple[str, List[str], List[str], List[str]]:
    """總務處爬蟲，返回公告字串、日期串列、標題串列、網址串列"""
    # 爬取資料
    url = "https://oga.ncut.edu.tw/"
    request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    ret_date = root.find_all("i", class_="mdate after")
    ret_title = []
    ret_url = []
    titles = root.find_all("div", class_="mtitle")
    for title in titles:
        ret_title.append(title.a)
        ret_url.append(title.a["href"])
    # 處理資料
    deal_date = []
    deal_title = []
    deal_url = []
    ret_ = ""
    date_ = []
    title_ = []
    url_ = []
    for i in ret_date:
        for j in i:
            deal_date.append(j.strip())
    for i in ret_title:
        for j in i:
            deal_title.append(j.strip())
    for i in ret_url:
        deal_url.append(i)
    for i in range(4, 9):
        ret_ += deal_date[i] + " "
        ret_ += deal_title[i] + "\n"
        ret_ += deal_url[i] + "\n"
        date_.append(deal_date[i])
        title_.append(deal_title[i])
        url_.append(deal_url[i])
    return ret_, date_, title_, url_

def teco_crawler() -> Tuple[str, List[str], List[str]]:
    """研究發展處爬蟲，返回公告字串、標題串列、網址串列"""
    # 爬取資料
    url = "https://ord.ncut.edu.tw/app/index.php?Action=mobileloadmod&Type=mobile_rcg_mstr&Nbr=277"
    request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    ret_title = []
    ret_url = []
    titles = root.find_all("div", class_="mtitle")
    for title in titles:
        ret_title.append(title.a)
        ret_url.append(title.a["href"])
    # 處理資料
    deal_title = []
    deal_url = []
    ret_ = ""
    title_ = []
    url_ = []
    for i in ret_title:
        for j in i:
            deal_title.append(j.strip())
    for i in ret_url:
        deal_url.append(i)
    for i in range(5):
        ret_ += deal_title[i] + "\n"
        ret_ += deal_url[i] + "\n"
        title_.append(deal_title[i])
        url_.append(deal_url[i])
    return ret_, title_, url_

def oia_crawler() -> Tuple[str, List[str], List[str]]: # 因公告顯示較少 抓取四筆
    """國際事務處爬蟲，返回公告字串、標題串列、網址串列"""
    # 爬取資料
    url = "https://oia.ncut.edu.tw/app/index.php?Action=mobileloadmod&Type=mobile_rcg_mstr&Nbr=800"
    request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    ret_title = []
    ret_url = []
    titles = root.find_all("div", class_="mtitle")
    for title in titles:
        ret_title.append(title.a)
        ret_url.append(title.a["href"])
    # 處理資料
    deal_title = []
    deal_url = []
    ret_ = ""
    title_ = []
    url_ = []
    for i in ret_title:
        for j in i:
            deal_title.append(j.strip())
    for i in ret_url:
        deal_url.append(i)
    for i in range(4):
        ret_ += deal_title[i] + "\n"
        ret_ += deal_url[i] + "\n"
        title_.append(deal_title[i])
        url_.append(deal_url[i])
    return ret_, title_, url_

def library_crawler() -> Tuple[str, List[str], List[str]]:
    """圖書館爬蟲，返回公告字串、標題串列、網址串列"""
    # 爬取資料
    url = "https://library.ncut.edu.tw/app/index.php?Action=mobileloadmod&Type=mobile_rcg_mstr&Nbr=120"
    request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    ret_title = []
    ret_url = []
    titles = root.find_all("div", class_="mtitle")
    for title in titles:
        ret_title.append(title.a)
        ret_url.append(title.a["href"])
    # 處理資料
    deal_title = []
    deal_url = []
    ret_ = ""
    title_ = []
    url_ = []
    for i in ret_title:
        for j in i:
            deal_title.append(j.strip())
    for i in ret_url:
        deal_url.append(i)
    for i in range(5):
        ret_ += deal_title[i] + "\n"
        ret_ += deal_url[i] + "\n"
        title_.append(deal_title[i])
        url_.append(deal_url[i])
    return ret_, title_, url_

def pe_crawler() -> Tuple[str, List[str], List[str], List[str]]:
    """體育室爬蟲，返回公告字串、日期串列、標題串列、網址串列"""
    # 爬取資料
    url = "https://opes.ncut.edu.tw/"
    request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    ret_date = root.find_all("i", class_="mdate before")
    ret_title = []
    ret_url = []
    titles = root.find_all("div", class_="mtitle")
    for title in titles:
        ret_title.append(title.a)
        ret_url.append(title.a["href"])
    # 處理資料
    deal_date = []
    deal_title = []
    deal_url = []
    ret_ = ""
    date_ = []
    title_ = []
    url_ = []
    for i in ret_date:
        for j in i:
            deal_date.append(j.strip())
    for i in ret_title:
        for j in i:
            deal_title.append(j.strip())
    for i in ret_url:
        deal_url.append(i)
    for i in range(5):
        ret_ += deal_date[i] + " "
        ret_ += deal_title[i] + "\n"
        ret_ += deal_url[i] + "\n"
        date_.append(deal_date[i])
        title_.append(deal_title[i])
        url_.append(deal_url[i])
    return ret_, date_, title_, url_

def art_crawler() -> Tuple[str, List[str], List[str]]: # 因最新公告並非每場展覽皆有而改抓歷次展覽介紹
    """藝術中心爬蟲，返回公告字串、標題串列、網址串列"""
    # 爬取資料
    url = "https://art.ncut.edu.tw/app/index.php?Action=mobileloadmod&Type=mobile_rcg_mstr&Nbr=859"
    request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    ret_title = []
    ret_url = []
    titles = root.find_all("div", class_="mtitle")
    for title in titles:
        ret_title.append(title.a)
        ret_url.append(title.a["href"])
    # 處理資料
    deal_title = []
    deal_url = []
    ret_ = ""
    title_ = []
    url_ = []
    for i in ret_title:
        for j in i:
            deal_title.append(j.strip())
    for i in ret_url:
        deal_url.append(i)
    for i in range(5):
        ret_ += deal_title[i] + "\n"
        ret_ += deal_url[i] + "\n"
        title_.append(deal_title[i])
        url_.append(deal_url[i])
    return ret_, title_, url_

def csie_crawler() -> Tuple[str, List[str], List[str], List[str]]:
    """資工系爬蟲，返回公告字串、日期串列、標題串列、網址串列"""
    # 爬取資料
    url = "https://csie.ncut.edu.tw/news.php"
    request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    ret_date = root.find_all("div", class_="date")
    ret_title = []
    ret_url = []
    titles = root.find_all("div", class_="news-list")
    for title in titles:
        ret_title.append(title.a)
        ret_url.append(title.a["href"])
    # 處理資料
    deal_date = []
    deal_title = []
    deal_url = []
    ret_ = ""
    date_ = []
    title_ = []
    url_ = []
    for i in ret_date:
        for j in i:
            for k in j:
                n = k
                n = n.replace("Date / ","")
                deal_date.append(n)
    for i in ret_title:
        for j in i:
            deal_title.append(j)
    for i in ret_url:
        deal_url.append("https://csie.ncut.edu.tw/" + i)
    for i in range(5):
        ret_ += deal_date[i] + " "
        ret_ += deal_title[i] + "\n"
        ret_ += deal_url[i] + "\n"
        date_.append(deal_date[i])
        title_.append(deal_title[i])
        url_.append(deal_url[i])
    return ret_, date_, title_, url_

def em_crawler() -> Tuple[str, List[str], List[str], List[str]]:
    """電機系爬蟲，返回公告字串、日期串列、標題串列、網址串列"""
    # 爬取資料
    url = "https://eeweb.ncut.edu.tw/news.php"
    request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    ret_date = root.find_all("div", class_="date")
    ret_title = []
    ret_url = []
    titles = root.find_all("div", class_="news-list")
    for title in titles:
        ret_title.append(title.a)
        ret_url.append(title.a["href"])
    # 處理資料
    deal_date = []
    deal_title = []
    deal_url = []
    ret_ = ""
    date_ = []
    title_ = []
    url_ = []
    for i in ret_date:
        for j in i:
            for k in j:
                deal_date.append(k.strip())
    for i in ret_title:
        for j in i:
            deal_title.append(j)
    for i in ret_url:
        deal_url.append("https://eeweb.ncut.edu.tw/" + i)
    for i in range(5):
        ret_ += deal_date[i] + " "
        ret_ += deal_title[i] + "\n"
        ret_ += deal_url[i] + "\n"
        date_.append(deal_date[i])
        title_.append(deal_title[i])
        url_.append(deal_url[i])
    return ret_, date_, title_, url_

def ee_crawler() -> Tuple[str, List[str], List[str], List[str]]:
    """電子系爬蟲，返回公告字串、日期串列、標題串列、網址串列"""
    # 爬取資料
    url = "https://eet.ncut.edu.tw/news.php"
    request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    ret_date = root.find_all("div", class_="index_news_date")
    ret_title = []
    ret_url = []
    titles = root.find_all("div", class_="index_news_title")
    for title in titles:
        ret_title.append(title.a)
        ret_url.append(title.a["href"])
    # 處理資料
    deal_date = []
    deal_title = []
    deal_url = []
    ret_ = ""
    date_ = []
    title_ = []
    url_ = []
    for i in ret_date:
        for j in i:
            if i.index(j) % 2 == 0:
                deal_date.append(j)
    for i in ret_title:
        for j in i:
            deal_title.append(j)
    for i in ret_url:
        deal_url.append("https://eet.ncut.edu.tw/" + i)
    for i in range(5):
        ret_ += deal_date[i] + " "
        ret_ += deal_title[i] + "\n"
        ret_ += deal_url[i] + "\n"
        date_.append(deal_date[i])
        title_.append(deal_title[i])
        url_.append(deal_url[i])
    return ret_, date_, title_, url_

def ai_crawler() -> Tuple[str, List[str], List[str], List[str]]:
    """人工智慧系爬蟲，返回公告字串、日期串列、標題串列、網址串列"""
    # 爬取資料
    url = "https://ai.ncut.edu.tw/p/403-1063-726-1.php?Lang=zh-tw"
    request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    ret_date = root.find_all("i", class_="mdate before")
    ret_title = []
    ret_url = []
    titles = root.find_all("div", class_="mtitle")
    for title in titles:
        ret_title.append(title.a)
        ret_url.append(title.a["href"])
    # 處理資料
    deal_date = []
    deal_title = []
    deal_url = []
    ret_ = ""
    date_ = []
    title_ = []
    url_ = []
    for i in ret_date:
        for j in i:
            deal_date.append(j.strip())
    for i in ret_title:
        for j in i:
            deal_title.append(j.strip())
    for i in ret_url:
        deal_url.append(i)
    for i in range(5):
        ret_ += deal_date[i] + " "
        ret_ += deal_title[i] + "\n"
        ret_ += deal_url[i] + "\n"
        date_.append(deal_date[i])
        title_.append(deal_title[i])
        url_.append(deal_url[i])
    return ret_, date_, title_, url_

def send_email(web: str, text: str, to: str) -> None:
    """程式寄信通知"""
    msg = MIMEText(f'提醒您，{web}公告已更新！以下為前幾筆公告資料\n\n{text}', 'plain', 'utf-8') # 郵件內文
    msg['Subject'] = '您關注的公告已更新'   # 郵件標題
    msg['From'] = 'p920923@yahoo.com'    # 暱稱 或是 email
    msg['To'] = to             # 收件人 email

    smtp = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('p920923@yahoo.com','cnwwdhoekaccfnuh')
    status = smtp.send_message(msg)
    if status == {}:
        print('郵件傳送成功！')
    else:
        print('郵件傳送失敗！')
    smtp.quit()

def email_to_subscriber(web: str, text: str) -> None:
    """查詢需通知對象並寄出通知信"""
    # 查詢訂閱某網站的用戶
    website_name = web
    cursor.execute("""
        SELECT c.id, c.email
        FROM contacts c
        JOIN user_subscriptions up ON c.id = up.contact_id
        JOIN websites w ON up.news_type = w.name
        WHERE w.name = ?
    """, (website_name,))

    # 各別寄信通知
    results = cursor.fetchall()
    for row in results:
        try:
            print(f"ID: {row[0]}, Email: {row[1]}")
            send_email(web, text, row[1])
        except Exception as e:
            print(f'發生其它錯誤 {e}')

def connect_db() -> None:
    """建立一個資料庫連接"""
    conn = sqlite3.connect('data.db', check_same_thread=False)
    # 使查詢結果可以用欄位名稱來存取
    conn.row_factory = sqlite3.Row
    return conn

def crawler_task() -> None:
    """爬蟲迴圈"""
    while True:
        try:
            # 爬蟲檢查 勤益科大 公告是否更新
            ret, title, url = ncut_crawler()
            update = False
            for i in range(len(url)-1, -1, -1):
                print(f'{title[i]} {url[i]}')
                # 使用 with 來處理資料庫連接與寫入
                with connect_db() as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO ncut_news (title, url) VALUES (?, ?)", (title[i], url[i]))
                    except sqlite3.IntegrityError as e:
                        print(f"資料已存在，跳過新增")
                    except sqlite3.DatabaseError as e:
                        print(f"資料庫操作發生錯誤: {e}")
                    except Exception as e:
                        print(f'發生其它錯誤 {e}')
                    else:
                        conn.commit()  # 寫入資料
                        update = True
                        print("資料已寫入")
            if update:
                email_to_subscriber("勤益科大", ret)
        except Exception as e:
            print(f'爬蟲發生錯誤 {e}')

        try:
            # 爬蟲檢查 基礎通識 公告是否更新
            ret, date, title, url = ge_crawler()
            update = False
            for i in range(len(url)-1, -1, -1):
                print(f'{date[i]} {title[i]} {url[i]}')
                # 使用 with 來處理資料庫連接與寫入
                with connect_db() as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO ge_news (date, title, url) VALUES (?, ?, ?)", (date[i], title[i], url[i]))
                    except sqlite3.IntegrityError as e:
                        print(f"資料已存在，跳過新增")
                    except sqlite3.DatabaseError as e:
                        print(f"資料庫操作發生錯誤: {e}")
                    except Exception as e:
                        print(f'發生其它錯誤 {e}')
                    else:
                        conn.commit()  # 寫入資料
                        update = True
                        print("資料已寫入")
            if update:
                email_to_subscriber("基礎通識", ret)
        except Exception as e:
            print(f'爬蟲發生錯誤 {e}')

        try:
            # 爬蟲檢查 博雅通識 公告是否更新
            ret, date, title, url = liberal_crawler()
            update = False
            for i in range(len(url)-1, -1, -1):
                print(f'{date[i]} {title[i]} {url[i]}')
                # 使用 with 來處理資料庫連接與寫入
                with connect_db() as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO liberal_news (date, title, url) VALUES (?, ?, ?)", (date[i], title[i], url[i]))
                    except sqlite3.IntegrityError as e:
                        print(f"資料已存在，跳過新增")
                    except sqlite3.DatabaseError as e:
                        print(f"資料庫操作發生錯誤: {e}")
                    except Exception as e:
                        print(f'發生其它錯誤 {e}')
                    else:
                        conn.commit()  # 寫入資料
                        update = True
                        print("資料已寫入")
            if update:
                email_to_subscriber("博雅通識", ret)
        except Exception as e:
            print(f'爬蟲發生錯誤 {e}')

        try:
            # 爬蟲檢查 教務處 公告是否更新
            ret, date, source, title, url = oaa_crawler()
            update = False
            for i in range(len(url)-1, -1, -1):
                print(f'{date[i]} {source[i]} {title[i]} {url[i]}')
                # 使用 with 來處理資料庫連接與寫入
                with connect_db() as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO oaa_news (date, source, title, url) VALUES (?, ?, ?, ?)", (date[i], source[i], title[i], url[i]))
                    except sqlite3.IntegrityError as e:
                        print(f"資料已存在，跳過新增")
                    except sqlite3.DatabaseError as e:
                        print(f"資料庫操作發生錯誤: {e}")
                    except Exception as e:
                        print(f'發生其它錯誤 {e}')
                    else:
                        conn.commit()  # 寫入資料
                        update = True
                        print("資料已寫入")
            if update:
                email_to_subscriber("教務處", ret)
        except Exception as e:
            print(f'爬蟲發生錯誤 {e}')

        try:
            # 爬蟲檢查 學務處 公告是否更新
            ret, title, url = osa_crawler()
            update = False
            for i in range(len(url)-1, -1, -1):
                print(f'{title[i]} {url[i]}')
                # 使用 with 來處理資料庫連接與寫入
                with connect_db() as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO osa_news (title, url) VALUES (?, ?)", (title[i], url[i]))
                    except sqlite3.IntegrityError as e:
                        print(f"資料已存在，跳過新增")
                    except sqlite3.DatabaseError as e:
                        print(f"資料庫操作發生錯誤: {e}")
                    except Exception as e:
                        print(f'發生其它錯誤 {e}')
                    else:
                        conn.commit()  # 寫入資料
                        update = True
                        print("資料已寫入")
            if update:
                email_to_subscriber("學務處", ret)
        except Exception as e:
            print(f'爬蟲發生錯誤 {e}')

        try:
            # 爬蟲檢查 總務處 公告是否更新
            ret, date, title, url = oga_crawler()
            update = False
            for i in range(len(url)-1, -1, -1):
                print(f'{date[i]} {title[i]} {url[i]}')
                # 使用 with 來處理資料庫連接與寫入
                with connect_db() as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO oga_news (date, title, url) VALUES (?, ?, ?)", (date[i], title[i], url[i]))
                    except sqlite3.IntegrityError as e:
                        print(f"資料已存在，跳過新增")
                    except sqlite3.DatabaseError as e:
                        print(f"資料庫操作發生錯誤: {e}")
                    except Exception as e:
                        print(f'發生其它錯誤 {e}')
                    else:
                        conn.commit()  # 寫入資料
                        update = True
                        print("資料已寫入")
            if update:
                email_to_subscriber("總務處", ret)
        except Exception as e:
            print(f'爬蟲發生錯誤 {e}')

        try:
            # 爬蟲檢查 研究發展處 公告是否更新
            ret, title, url = teco_crawler()
            update = False
            for i in range(len(url)-1, -1, -1):
                print(f'{title[i]} {url[i]}')
                # 使用 with 來處理資料庫連接與寫入
                with connect_db() as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO teco_news (title, url) VALUES (?, ?)", (title[i], url[i]))
                    except sqlite3.IntegrityError as e:
                        print(f"資料已存在，跳過新增")
                    except sqlite3.DatabaseError as e:
                        print(f"資料庫操作發生錯誤: {e}")
                    except Exception as e:
                        print(f'發生其它錯誤 {e}')
                    else:
                        conn.commit()  # 寫入資料
                        update = True
                        print("資料已寫入")
            if update:
                email_to_subscriber("研究發展處", ret)
        except Exception as e:
            print(f'爬蟲發生錯誤 {e}')

        try:
            # 爬蟲檢查 國際事務處 公告是否更新
            ret, title, url = oia_crawler()
            update = False
            for i in range(len(url)-1, -1, -1):
                print(f'{title[i]} {url[i]}')
                # 使用 with 來處理資料庫連接與寫入
                with connect_db() as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO oia_news (title, url) VALUES (?, ?)", (title[i], url[i]))
                    except sqlite3.IntegrityError as e:
                        print(f"資料已存在，跳過新增")
                    except sqlite3.DatabaseError as e:
                        print(f"資料庫操作發生錯誤: {e}")
                    except Exception as e:
                        print(f'發生其它錯誤 {e}')
                    else:
                        conn.commit()  # 寫入資料
                        update = True
                        print("資料已寫入")
            if update:
                email_to_subscriber("國際事務處", ret)
        except Exception as e:
            print(f'爬蟲發生錯誤 {e}')

        try:
            # 爬蟲檢查 圖書館 公告是否更新
            ret, title, url = library_crawler()
            update = False
            for i in range(len(url)-1, -1, -1):
                print(f'{title[i]} {url[i]}')
                # 使用 with 來處理資料庫連接與寫入
                with connect_db() as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO library_news (title, url) VALUES (?, ?)", (title[i], url[i]))
                    except sqlite3.IntegrityError as e:
                        print(f"資料已存在，跳過新增")
                    except sqlite3.DatabaseError as e:
                        print(f"資料庫操作發生錯誤: {e}")
                    except Exception as e:
                        print(f'發生其它錯誤 {e}')
                    else:
                        conn.commit()  # 寫入資料
                        update = True
                        print("資料已寫入")
            if update:
                email_to_subscriber("圖書館", ret)
        except Exception as e:
            print(f'爬蟲發生錯誤 {e}')

        try:
            # 爬蟲檢查 體育室 公告是否更新
            ret, date, title, url = pe_crawler()
            update = False
            for i in range(len(url)-1, -1, -1):
                print(f'{date[i]} {title[i]} {url[i]}')
                # 使用 with 來處理資料庫連接與寫入
                with connect_db() as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO pe_news (date, title, url) VALUES (?, ?, ?)", (date[i], title[i], url[i]))
                    except sqlite3.IntegrityError as e:
                        print(f"資料已存在，跳過新增")
                    except sqlite3.DatabaseError as e:
                        print(f"資料庫操作發生錯誤: {e}")
                    except Exception as e:
                        print(f'發生其它錯誤 {e}')
                    else:
                        conn.commit()  # 寫入資料
                        update = True
                        print("資料已寫入")
            if update:
                email_to_subscriber("體育室", ret)
        except Exception as e:
            print(f'爬蟲發生錯誤 {e}')

        try:
            # 爬蟲檢查 藝術中心 公告是否更新
            ret, title, url = art_crawler()
            update = False
            for i in range(len(url)-1, -1, -1):
                print(f'{title[i]} {url[i]}')
                # 使用 with 來處理資料庫連接與寫入
                with connect_db() as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO art_news (title, url) VALUES (?, ?)", (title[i], url[i]))
                    except sqlite3.IntegrityError as e:
                        print(f"資料已存在，跳過新增")
                    except sqlite3.DatabaseError as e:
                        print(f"資料庫操作發生錯誤: {e}")
                    except Exception as e:
                        print(f'發生其它錯誤 {e}')
                    else:
                        conn.commit()  # 寫入資料
                        update = True
                        print("資料已寫入")
            if update:
                email_to_subscriber("藝術中心", ret)
        except Exception as e:
            print(f'爬蟲發生錯誤 {e}')

        try:
            # 爬蟲檢查 資工系 公告是否更新
            ret, date, title, url = csie_crawler()
            update = False
            for i in range(len(url)-1, -1, -1):
                print(f'{date[i]} {title[i]} {url[i]}')
                # 使用 with 來處理資料庫連接與寫入
                with connect_db() as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO csie_news (date, title, url) VALUES (?, ?, ?)", (date[i], title[i], url[i]))
                    except sqlite3.IntegrityError as e:
                        print(f"資料已存在，跳過新增")
                    except sqlite3.DatabaseError as e:
                        print(f"資料庫操作發生錯誤: {e}")
                    except Exception as e:
                        print(f'發生其它錯誤 {e}')
                    else:
                        conn.commit()  # 寫入資料
                        update = True
                        print("資料已寫入")
            if update:
                email_to_subscriber("資工系", ret)
        except Exception as e:
            print(f'爬蟲發生錯誤 {e}')

        try:
            # 爬蟲檢查 電機系 公告是否更新
            ret, date, title, url = em_crawler()
            update = False
            for i in range(len(url)-1, -1, -1):
                print(f'{date[i]} {title[i]} {url[i]}')
                # 使用 with 來處理資料庫連接與寫入
                with connect_db() as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO em_news (date, title, url) VALUES (?, ?, ?)", (date[i], title[i], url[i]))
                    except sqlite3.IntegrityError as e:
                        print(f"資料已存在，跳過新增")
                    except sqlite3.DatabaseError as e:
                        print(f"資料庫操作發生錯誤: {e}")
                    except Exception as e:
                        print(f'發生其它錯誤 {e}')
                    else:
                        conn.commit()  # 寫入資料
                        update = True
                        print("資料已寫入")
            if update:
                email_to_subscriber("電機系", ret)
        except Exception as e:
            print(f'爬蟲發生錯誤 {e}')

        try:
            # 爬蟲檢查 電子系 公告是否更新
            ret, date, title, url = ee_crawler()
            update = False
            for i in range(len(url)-1, -1, -1):
                print(f'{date[i]} {title[i]} {url[i]}')
                # 使用 with 來處理資料庫連接與寫入
                with connect_db() as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO ee_news (date, title, url) VALUES (?, ?, ?)", (date[i], title[i], url[i]))
                    except sqlite3.IntegrityError as e:
                        print(f"資料已存在，跳過新增")
                    except sqlite3.DatabaseError as e:
                        print(f"資料庫操作發生錯誤: {e}")
                    except Exception as e:
                        print(f'發生其它錯誤 {e}')
                    else:
                        conn.commit()  # 寫入資料
                        update = True
                        print("資料已寫入")
            if update:
                email_to_subscriber("電子系", ret)
        except Exception as e:
            print(f'爬蟲發生錯誤 {e}')

        try:
            # 爬蟲檢查 人工智慧系 公告是否更新
            ret, date, title, url = ai_crawler()
            update = False
            for i in range(len(url)-1, -1, -1):
                print(f'{date[i]} {title[i]} {url[i]}')
                # 使用 with 來處理資料庫連接與寫入
                with connect_db() as conn:
                    cursor = conn.cursor()
                    try:
                        cursor.execute("INSERT INTO ai_news (date, title, url) VALUES (?, ?, ?)", (date[i], title[i], url[i]))
                    except sqlite3.IntegrityError as e:
                        print(f"資料已存在，跳過新增")
                    except sqlite3.DatabaseError as e:
                        print(f"資料庫操作發生錯誤: {e}")
                    except Exception as e:
                        print(f'發生其它錯誤 {e}')
                    else:
                        conn.commit()  # 寫入資料
                        update = True
                        print("資料已寫入")
            if update:
                email_to_subscriber("人工智慧系", ret)
        except Exception as e:
            print(f'爬蟲發生錯誤 {e}')

        print("最後檢查時間 ", time.ctime())
        time.sleep(60)  # 每 60 秒檢查一次

def handle_client(conn, addr) -> None:
    """處理單一客戶端連接"""
    print(f"與 {addr} 建立連接")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print(f"{addr} 已斷開連接")
                break

            # 解碼並反序列化數據
            msg = json.loads(data.decode('utf-8'))
            print(f"收到來自 {addr} 的消息: {msg}")

            # 驗證數據結構
            if not isinstance(msg, list) or len(msg) < 2:
                conn.sendall("數據格式錯誤".encode('utf-8'))
                continue

            email = msg[0]
            subscriptions = msg[1:]  # 剩下的為訂閱類型

            # 使用 with 來處理資料庫連接
            with connect_db() as db_conn:
                cursor = db_conn.cursor()

                # 插入聯絡人
                cursor.execute("""INSERT OR IGNORE INTO contacts (email) VALUES (?)""", (email,))

                # 查詢聯絡人 ID
                cursor.execute("""SELECT id FROM contacts WHERE email = ?""", (email,))
                contact_id = cursor.fetchone()[0]

                # 刪除舊有的信箱資料
                cursor.execute("""DELETE FROM user_subscriptions
                                  WHERE contact_id = (SELECT id FROM contacts WHERE email = ?)""", (email,))

                # 插入用戶訂閱數據
                for news_type in subscriptions:
                    cursor.execute(
                        """INSERT OR IGNORE INTO user_subscriptions (contact_id, news_type) VALUES (?, ?)""",
                        (contact_id, news_type)
                    )

                db_conn.commit()

            conn.sendall("資料已成功處理".encode('utf-8'))
        except sqlite3.Error as e:
            print(f"資料庫錯誤: {e}")
            conn.sendall("伺服器內部錯誤".encode('utf-8'))
        except ConnectionResetError:
            print(f"{addr} 強制斷開連接")
            break
    conn.close()

def start_server(host, port) -> None:
    """啟動伺服器"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"伺服器正在 {host}:{port} 運行並等待連接...")

    while True:
        conn, addr = server_socket.accept()
        # 為每個新連接啟動一個線程
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


# 使用 with 來處理資料庫連接與建立
with connect_db() as conn:
    # 建立 cursor 物件
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS websites (
        id INTEGER PRIMARY KEY,     -- 網站 ID，唯一
        name TEXT NOT NULL UNIQUE   -- 網站名稱 必須有值，唯一
    )""")
    try:
        cursor.execute("""INSERT INTO websites (name) VALUES
        ("勤益科大"),
        ("基礎通識"),
        ("博雅通識"),
        ("教務處"),
        ("學務處"),
        ("總務處"),
        ("研究發展處"),
        ("國際事務處"),
        ("圖書館"),
        ("體育室"),
        ("藝術中心"),
        ("電機系"),
        ("電子系"),
        ("資工系"),
        ("人工智慧系")
        """)
    except sqlite3.IntegrityError as e:
        print(f"websites 資料已存在，跳過新增")
    except sqlite3.DatabaseError as e:
        print(f"資料庫操作發生錯誤: {e}")
    except Exception as e:
        print(f'發生其它錯誤 {e}')
    cursor.execute("""CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,    -- 編號 主鍵，唯一且不可為 NULL
        email TEXT NOT NULL UNIQUE  -- Email 必須有值，唯一
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_subscriptions (
        contact_id INTEGER,       -- 對應 contacts 表的 id
        news_type TEXT,         -- 公告來源類型，例如 'ncut' 或 'csie'
        PRIMARY KEY (contact_id, news_type),
        FOREIGN KEY (contact_id) REFERENCES contacts(id)
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS ncut_news (
        id INTEGER PRIMARY KEY,    -- 編號 主鍵，唯一且不可為 NULL
        title TEXT NOT NULL,     -- 標題 必須有值
        url TEXT NOT NULL UNIQUE  -- 網址 必須有值，唯一
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS ge_news (
        id INTEGER PRIMARY KEY,    -- 編號 主鍵，唯一且不可為 NULL
        date TEXT NOT NULL,      -- 日期 必須有值
        title TEXT NOT NULL,     -- 標題 必須有值
        url TEXT NOT NULL UNIQUE  -- 網址 必須有值，唯一
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS liberal_news (
        id INTEGER PRIMARY KEY,    -- 編號 主鍵，唯一且不可為 NULL
        date TEXT NOT NULL,      -- 日期 必須有值
        title TEXT NOT NULL,     -- 標題 必須有值
        url TEXT NOT NULL UNIQUE  -- 網址 必須有值，唯一
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS oaa_news (
        id INTEGER PRIMARY KEY,    -- 編號 主鍵，唯一且不可為 NULL
        date TEXT NOT NULL,      -- 日期 必須有值
        source TEXT NOT NULL,      -- 組別 必須有值
        title TEXT NOT NULL,     -- 標題 必須有值
        url TEXT NOT NULL UNIQUE  -- 網址 必須有值，唯一
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS osa_news (
        id INTEGER PRIMARY KEY,    -- 編號 主鍵，唯一且不可為 NULL
        title TEXT NOT NULL,     -- 標題 必須有值
        url TEXT NOT NULL UNIQUE  -- 網址 必須有值，唯一
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS oga_news (
        id INTEGER PRIMARY KEY,    -- 編號 主鍵，唯一且不可為 NULL
        date TEXT NOT NULL,      -- 日期 必須有值
        title TEXT NOT NULL,     -- 標題 必須有值
        url TEXT NOT NULL UNIQUE  -- 網址 必須有值，唯一
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS teco_news (
        id INTEGER PRIMARY KEY,    -- 編號 主鍵，唯一且不可為 NULL
        title TEXT NOT NULL,     -- 標題 必須有值
        url TEXT NOT NULL UNIQUE  -- 網址 必須有值，唯一
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS oia_news (
        id INTEGER PRIMARY KEY,    -- 編號 主鍵，唯一且不可為 NULL
        title TEXT NOT NULL,     -- 標題 必須有值
        url TEXT NOT NULL UNIQUE  -- 網址 必須有值，唯一
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS library_news (
        id INTEGER PRIMARY KEY,    -- 編號 主鍵，唯一且不可為 NULL
        title TEXT NOT NULL,     -- 標題 必須有值
        url TEXT NOT NULL UNIQUE  -- 網址 必須有值，唯一
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS pe_news (
        id INTEGER PRIMARY KEY,    -- 編號 主鍵，唯一且不可為 NULL
        date TEXT NOT NULL,      -- 日期 必須有值
        title TEXT NOT NULL,     -- 標題 必須有值
        url TEXT NOT NULL UNIQUE  -- 網址 必須有值，唯一
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS art_news (
        id INTEGER PRIMARY KEY,    -- 編號 主鍵，唯一且不可為 NULL
        title TEXT NOT NULL,     -- 標題 必須有值
        url TEXT NOT NULL UNIQUE  -- 網址 必須有值，唯一
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS csie_news (
        id INTEGER PRIMARY KEY,    -- 編號 主鍵，唯一且不可為 NULL
        date TEXT NOT NULL,      -- 日期 必須有值
        title TEXT NOT NULL,     -- 標題 必須有值
        url TEXT NOT NULL UNIQUE  -- 網址 必須有值，唯一
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS em_news (
        id INTEGER PRIMARY KEY,    -- 編號 主鍵，唯一且不可為 NULL
        date TEXT NOT NULL,      -- 日期 必須有值
        title TEXT NOT NULL,     -- 標題 必須有值
        url TEXT NOT NULL UNIQUE  -- 網址 必須有值，唯一
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS ee_news (
        id INTEGER PRIMARY KEY,    -- 編號 主鍵，唯一且不可為 NULL
        date TEXT NOT NULL,      -- 日期 必須有值
        title TEXT NOT NULL,     -- 標題 必須有值
        url TEXT NOT NULL UNIQUE  -- 網址 必須有值，唯一
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS ai_news (
        id INTEGER PRIMARY KEY,    -- 編號 主鍵，唯一且不可為 NULL
        date TEXT NOT NULL,      -- 日期 必須有值
        title TEXT NOT NULL,     -- 標題 必須有值
        url TEXT NOT NULL UNIQUE  -- 網址 必須有值，唯一
    )""")

# 啟動爬蟲執行緒
crawler_thread = threading.Thread(target=crawler_task, daemon=True)
crawler_thread.start()

# 啟動伺服器
HOST = '0.0.0.0'
PORT = 12345
start_server(HOST, PORT)

# # 勤益科大
# ret_ = ncut_crawler()
# print(ret_[0]) # 印出公告
# # 基礎通識中心
# ret_ = ge_crawler()
# print(ret_[0]) # 印出公告
# # 博雅通識中心
# ret_ = liberal_crawler()
# print(ret_[0]) # 印出公告
# # 教務處
# ret_ = oaa_crawler()
# print(ret_[0]) # 印出公告
# # 學生事務處
# ret_ = osa_crawler()
# print(ret_[0]) # 印出公告
# # 總務處
# ret_ = oga_crawler()
# print(ret_[0]) # 印出公告
# # 研究發展處
# ret_ = teco_crawler()
# print(ret_[0]) # 印出公告
# # 國際事務處
# ret_ = oia_crawler()
# print(ret_[0]) # 印出公告
# # 圖書館
# ret_ = library_crawler()
# print(ret_[0]) # 印出公告
# # 體育室
# ret_ = pe_crawler()
# print(ret_[0]) # 印出公告
# # 藝術中心
# ret_ = art_crawler()
# print(ret_[0]) # 印出公告
# # 資工系
# ret_ = csie_crawler()
# print(ret_[0]) # 印出公告
# # 電機系
# ret_ = em_crawler()
# print(ret_[0]) # 印出公告
# # 電子系
# ret_ = ee_crawler()
# print(ret_[0]) # 印出公告
# # 人工智慧系
# ret_ = ai_crawler()
# print(ret_[0]) # 印出公告