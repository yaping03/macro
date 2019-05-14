import pymysql

class ConnSql:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root',password='zyp1230000',database='macro',charset="utf8")
        self.cursor = self.conn.cursor()

    def insert_ns1_3d(self,data):
        for dic in data:
            # if dic.get("Resolution"):
            #    resol = float(dic.get("Resolution"))
            # else:
            #     resol = 0.0
            sql='insert into ns1_3d(PDB_ID,Title,Method,Resolution) values(%s,%s,%s,%s);'
            res = self.cursor.execute(sql, (dic.get("PDB_ID"),dic.get("Title"),dic.get("Method"),dic.get("Resolution")))
        self.conn.commit()
        print("ns1_3d ok!!")

    def insert_ns1_3d_detail(self,data):
        for dic in data:
            # if dic.get("Resolution"):
            #    resol = float(dic.get("Resolution"))
            # else:
            #     resol = 0.0
            if not dic.get("Chains:s"):
                sql = 'insert into ns1_ns1_3d_detail(PDB_ID,Title,Method,Resolution,Reference,Author,' \
                      'Journal,Mole_Chains,Mole_Molecule,Mole_Details,Mole_Organism,Mole_Sequence) ' \
                      'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                res = self.cursor.execute(sql, (
                dic.get("PDB ID"), dic.get("Title"), dic.get("Method"), dic.get("Resolution"), dic.get("Reference"),
                dic.get("Author"),
                dic.get("Journal"), dic.get("Chains:"), dic.get("Molecule:"), dic.get("Details:"), dic.get("Organism:"),
                dic.get("Sequence:")))
            else:
                sql='insert into ns1_ns1_3d_detail(PDB_ID,Title,Method,Resolution,Reference,Author,' \
                    'Journal,Mole_Chains,Mole_Molecule,Mole_Details,Mole_Organism,Mole_Sequence,' \
                    'Mole_Chains1,Mole_Molecule1,Mole_Details1,Mole_Organism1,Mole_Sequence1) ' \
                    'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                res = self.cursor.execute(sql, (dic.get("PDB ID"),dic.get("Title"),dic.get("Method"),dic.get("Resolution"),dic.get("Reference"),dic.get("Author"),
                                            dic.get("Journal"),dic.get("Chains:"),dic.get("Molecule:"),dic.get("Details:"),dic.get("Organism:"),dic.get("Sequence:"),
                                               dic.get("Chains:s"),dic.get("Molecule:s"),dic.get("Details:s"),dic.get("Organism:s"),dic.get("Sequence:s")))

        self.conn.commit()
        print("ok!!")

    def insert_16srna(self,data):
        for lis in data:
            try:
                # print(lis)
                if len(lis) == 7:
                    sql='insert into 16srna(NO,Genus,Species,Subspecies,Typestrain,NCBI,Sequence) values(%s,%s,%s,%s,%s,%s,%s);'
                    res = self.cursor.execute(sql, (lis[0],lis[1],lis[2],lis[3],lis[4].encode("utf-8"),lis[5],lis[6]))

            except Exception as e:
                print(e)
        self.conn.commit()
        print("ok!!")

    def insert_ns1_detail(self,data):
        for lis in data:
            try:
                if len(lis) == 10:
                    sql='insert into ns1_detail(Accession_id,Sequence_name,Scientific_name,Taxonomic_identifier,Subtype,Host,Collection_year,\
                        Country,Protein_attributes,Sequence) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                    res = self.cursor.execute(sql, (lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6],lis[7],lis[8],lis[9]))

            except Exception as e:
                print(e)
        self.conn.commit()
        print("ok!!")

    def insert_fungus_detail(self,data):
        # s = []
        # n = []
        for lis in data:
            # print(lis)
            # print(len(lis))
            try:
                if len(lis) == 21 and lis[0]:
                    # s.append(lis[0])
                    sql='insert into fungus_detail(保藏号,名称,别名,属,种,亚种,来源,\
                        16s_rna,特性,是否测序,是否模式,培养基,保存条件,安全等级,参考文献,数量,其他库,保存形式,\
                        描述,发表论文,保存时间) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                    res = self.cursor.execute(sql, (lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6],lis[7],lis[8],
                                                    lis[9],lis[10],lis[11],
                                                    lis[12],lis[13],lis[14],lis[15],lis[16],lis[17],lis[18],lis[19],lis[20]))
                # else:
                    # n.append(" ")
            except Exception as e:
                print(e)
        self.conn.commit()
        print("ok!!")
        # print(s)
        # print(n)
        # print(len(s))
        # print(len(n))

    def insert_plasmid_detail(self,data):
        for lis in data:
            # print(lis)
            # print(len(lis))
            try:
                if len(lis) == 12 and lis[0]:
                    print(lis)
                    sql='insert into plasmid_detail(保藏号,质粒名称,质粒类型,载体大小,载体标签,载体抗性,保存菌株,\
                        质粒图谱,来源,保存时间,载体描述,备注) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                    res = self.cursor.execute(sql, (lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6],lis[7],lis[8],
                                                    lis[9],lis[10],lis[11]))
                else:
                    print(len(lis))
            except Exception as e:
                print(e)
        self.conn.commit()
        print("ok!!")

    def insert_cell_detail(self,data):
        for lis in data:
            # print(lis)
            # print(len(lis))
            try:
                if len(lis) == 10 and lis[0]:
                    print(lis)
                    sql='insert into cell_detail(保藏号,细胞名称,种属,组织来源,生长特性,细胞形态,背景描述,\
                        生长培养基,培养条件,备注) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                    res = self.cursor.execute(sql, (lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6],lis[7],lis[8],
                                                    lis[9]))
                else:
                    print(len(lis))
            except Exception as e:
                print(e)
        self.conn.commit()
        print("ok!!")

    def select_16srna(self):
        sql = 'select NO from 16srna;'
        self.cursor.execute(sql) #执行sql语句，返回sql影响成功的行数
        res=self.cursor.fetchall()
        no = 1
        for i in res:
            num = int(i[0][5:])
            if no != num:
                no +=1
                print(i)
            no += 1

    def select_fungus(self):
        sql = 'select Accession_id from ns1_detail;'
        self.cursor.execute(sql) #执行sql语句，返回sql影响成功的行数
        res=self.cursor.fetchall()
        no = 1
        for i in res:
            num = int(i[0][5:])
            if no != num:
                no +=1
                print(i)
            no += 1
    def select_fungus(self):
        sql = 'select 保藏号 from fungus_detail;'
        self.cursor.execute(sql) #执行sql语句，返回sql影响成功的行数
        res=self.cursor.fetchall()
        no = 1
        for i in res:
            num = int(i[0][4:])
            # print(num)
            if no != num:
                no +=1
                print(i)
            no += 1

    def finished(self):
        self.cursor.close()
        self.conn.close()

    def insert_test(self,data):
        dic = {'PDB ID': '3RVC', 'Title': 'Effector domain of NS1 from influenza A/PR/8/34 containing a W187A mutation ', 'Method': 'X-RAY DIFFRACTION', 'Resolution': '1.8', 'Reference': 'Conservation of a crystallographic interface suggests a role for ?-sheet augmentation in influenza virus NS1 multifunctionality.', 'Author': 'Kerry, P.S.,  Long, E.,  Taylor, M.A.,  Russell, R.J.,', 'Journal': '(2011) Acta Crystallogr.,Sect.F 67: 858-861 ','Chainsd':'aaa', 'Chains:': 'A', 'Molecule:': 'Nonstructural protein 1', 'Details:': None, 'Organism:': 'Influenza A virus (A/Puerto Rico/8/1934(H1N1))', 'Sequence:': 'I34A1'}

        # bbb = None
        # sql='insert into test(aaa,bbb) values(%s,%s);'
        # res = self.cursor.execute(sql, (bbb, bbb))
        # print(dic.get("Chainsd"))
        sql = 'insert into ns1_3d_detail(PDB_ID,Title,Method,Resolution,Reference,Author,' \
              'Journal,Mole_Chains,Mole_Molecule,Mole_Details,Mole_Organism,Mole_Sequence) ' \
              'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        res = self.cursor.execute(sql, (
        dic.get("PDB_ID"), dic.get("Title"), dic.get("Method"), dic.get("Resolution"), dic.get("Reference"),
        dic.get("Author"), \
        dic.get("Journal"), dic.get("Chains:"), dic.get("Molecule:"), dic.get("Details:"), dic.get("Organism:"),
        dic.get("Sequence:")))
        self.conn.commit()
        print("ok!!")

    def insert_char(self):
        sql = 'insert into test(aaa,bbb,完成) values(%s,%s,%s);'
        res = self.cursor.execute(sql, ("11","mm","aa1"))

        self.conn.commit()
        print("test ok!!")



def test():
    c = ConnSql()
    # c.insert_test([{"aaa":"111","bbb":222}])
    # c.select_16srna()
    # c.insert_char()
    c.select_fungus()
if __name__ == '__main__':
    test()