import os,time,sys,json
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor,wait
import handle_sql
import pickle

# path = sys.argv[1]
# proxies = {'http': 'http://123.55.2.106:21339'}
head ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

def parse():
    PDB_list = []
    try:
        url = "http://ccsipb.lnu.edu.cn/ns1/pdb/index.asp"
        result = requests.get(url,headers=head)
        # result = req.reserve_prox(url)
        bse = BeautifulSoup(result.text,features="lxml")
        # tbody = bse.find(name="div",attrs={"class":"zxlist"})
        table = bse.find(name="table")
        if bse and table:
            trs = table.find_all("tr")
            for tr in trs[1:]:
                ns1_d = {}
                tds = tr.find_all("td")
                if len(tds) == 4:
                    a = tds[0].find("a")
                    ns1_d["PDB_ID"] = a.string
                    ns1_d["Title"] = tds[1].string
                    ns1_d["Method"] = tds[2].string
                    ns1_d["Resolution"] = tds[3].string

                    PDB_list.append(a.string)
                ns1_l.append(ns1_d)
                # lis = ul.find_all("li",attrs={"class":"iterm"})
                # if lis:
                #     for li in lis:
                #         art = li.find("a",attrs={"class":"iterm_XX"})
                #         if art:
                #             if art.string:
                #                 article_list.append((art.attrs.get('href'),art.string))

                # else:
                #     break
    except Exception as e:
        print(e)
            

    return PDB_list


def parse_detail(url):
    det_t = []
    try:
        result = requests.get(url, headers=head)
        # result = req.reserve_prox(url)
        bse = BeautifulSoup(result.text, features="lxml")
        # tbody = bse.find(name="div",attrs={"class":"zxlist"})
        div = bse.find(name="div")
        if bse and div:
            labels = div.find_all(name="label")
            text = div.find(name="textarea")
            if len(labels) == 13:
                for label in labels[1:12:2]:
                    if not label.string:
                        a = label.find("a")
                        if a:
                            det_t.append(a.string)
                    else:
                        det_t.append(label.string)
                if text.string:
                    det_t.append(text.string)
                else:
                    print(url+"text not find")
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
    # PDB_list = parse()
    # PDB_list = ["3F5T","3P31","3P39"]
    t = ThreadPoolExecutor(8)
    t_l = []
    for sub in range(1,12707):
        print(sub)
        url = "http://ccsipb.lnu.edu.cn/16sdb/detailedQuery/?id=%d"%sub
        w = t.submit(parse_detail, url)
        w.done()
        t_l.append(w)
    wait(t_l)
    print("===完成===")
    cursor = handle_sql.ConnSql()
    # cursor.insert_ns1_3d(ns1_l)
    cursor.insert_16srna(det_l)
    cursor.finished()



