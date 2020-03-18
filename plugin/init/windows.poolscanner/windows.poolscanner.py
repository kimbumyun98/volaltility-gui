import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.poolscanner/windows.poolscanner.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('Tag	Offset	Layer	Name','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
result = [my_list[i * 4:(i + 1) * 4] for i in range((len(my_list) + 3) // 4 )] 
print(result) 

conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table poolscanner (Tag text, Offset text, Layer text, Name text)")

cur.executemany("insert into poolscanner values (?, ?, ?, ?)", result)
conn.commit()

cur.execute('select * from poolscanner')
for row in cur:
    print(row)

conn.close()