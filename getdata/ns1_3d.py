import os,time,sys,json
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor,wait
import handle_sql

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
    det_d = {}
    try:
        result = requests.get(url, headers=head)
        # result = req.reserve_prox(url)
        bse = BeautifulSoup(result.text, features="lxml")
        # tbody = bse.find(name="div",attrs={"class":"zxlist"})
        table = bse.find(name="table")
        if bse and table:
            trs = table.find_all("tr")
            for tr in trs:
                tds = tr.find_all("td")
                if len(tds) == 2:
                    if tds[0].string:
                        if det_d.get(tds[0].string):
                            det_d[tds[0].string + "s"] = tds[1].string
                        else:
                            det_d[tds[0].string] = tds[1].string
                    # else:

            print(det_d)
            det_l.append(det_d)
    except Exception as e:
        print(e)

    # return PDB_list
if __name__ == '__main__':
    ns1_l = []
    det_l = []
    if sys.platform == "win32":
        splits = "\\"
    else:
        splits = "/"
    PDB_list = parse()
    # PDB_list = ["3F5T","3P31","3P39"]
    t = ThreadPoolExecutor(8)
    t_l = []
    for sub in PDB_list:
        url = "http://ccsipb.lnu.edu.cn/ns1/pdb/structure.asp?s=%s"%sub
        w = t.submit(parse_detail, url)
        w.done()
        t_l.append(w)
    wait(t_l)
    print("===完成===")
    cursor = handle_sql.ConnSql()
    cursor.insert_ns1_3d(ns1_l)
    cursor.insert_ns1_3d_detail(det_l)
    cursor.finished()



