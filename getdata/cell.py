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
        table = bse.find(name="table",attrs={"class":"table table-striped"})
        # n_tr = bse.find(name="tr", attrs={"class": "x-grid3-row "})
        if bse and table:
            trs = table.find_all(name="tr")
            if len(trs) == 10:
                for tr in trs:
                    tds = tr.find_all("td")
                    if len(tds) == 2:
                        con  = ""
                        for i in tds[1].stripped_strings:
                            con += i
                        det_t.append(con)

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
    for sub in range(1,17):
        print(sub)
        # url = "http://ccsipb.lnu.edu.cn/bio_data_bacteria/index.php/c_front_fungus/queryById/F%d"%sub
        url = "http://ccsipb.lnu.edu.cn/bio_data_bacteria/index.php/c_front_cell/queryById/LNUC%03d"%sub
        w = t.submit(parse_detail, url)
        w.done()
        t_l.append(w)
    wait(t_l)
    print("===完成===")
    cursor = handle_sql.ConnSql()
    cursor.insert_cell_detail(det_l)
    cursor.finished()



