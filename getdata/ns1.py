import os,time,sys,json
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor,wait
import handle_sql
import pickle

# path = sys.argv[1]
# proxies = {'http': 'http://123.55.2.106:21339'}
head ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}


def parse_detail(url):
    det_t = []
    try:
        result = requests.get(url, headers=head)
        # result = req.reserve_prox(url)
        bse = BeautifulSoup(result.text, features="lxml")
        # tbody = bse.find(name="div",attrs={"class":"zxlist"})
        table = bse.find(name="table")
        if bse and table:
            trs = table.find_all(name="tr")
            if len(trs) == 10:
                for tr in trs:
                    tds = tr.find_all("td")
                    if len(tds) == 2:
                        if tds[1].string:
                            det_t.append(tds[1].string)
                        elif tds[1].find("a"):
                            a = tds[1].find_all("a")
                            if len(a) ==2:
                                det_t.append(a[0].string+" "+a[1].string)
                        elif tds[1].find("span"):
                            span = tds[1].find("span")
                            if span:
                                text = ""
                                for i in span.stripped_strings:
                                    text += i+" "
                                det_t.append(text)
                            else:
                                print(url + "not find span")
                        else:
                            det_t.append(tds[1].string)
                    else:
                        print(url + "解析出现问题!")
                det_l.append(det_t)
            else:
                print(url+"解析出现问题!")
        else:
            print(url + "解析出现问题!")

    except Exception as e:
        print(url)
        print(e)

    # return PDB_list
if __name__ == '__main__':
    det_l = []
    if sys.platform == "win32":
        splits = "\\"
    else:
        splits = "/"

    t = ThreadPoolExecutor(8)
    t_l = []
    for sub in range(14000,17090):
        print(sub)
        url = "http://ccsipb.lnu.edu.cn/ns1/view.asp?ac=LNU%07d"%sub
        w = t.submit(parse_detail, url)
        w.done()
        t_l.append(w)
    wait(t_l)
    print("===完成===")
    cursor = handle_sql.ConnSql()
    cursor.insert_ns1_detail(det_l)
    cursor.finished()



