import sqlite3
import os
import pathlib

path = os.getcwd() + "/plugin/init/windows.pstree/windows.pstree.txt"
path = pathlib.Path(path)
f = open(path, 'r', encoding='utf-8')
t = f.read()
t = t.replace('Volatility 3 Framework 1.0.0-beta.1','')
t = t.replace('PID	PPID	ImageFileName	Offset(V)	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime','')
t = t.replace('\n\n',"\t")
t = "".join([s for s in t.strip().splitlines(True) if s.strip()])
my_list = t.split('\t')
result = [my_list[i * 10:(i + 1) * 10] for i in range((len(my_list) + 9) // 10 )] 

conn = sqlite3.connect("analyze.db")
cur = conn.cursor()
cur.execute("create table pstree (PID int, PPID int, ImageFileName text, Offset text, Threads int, Handles int, Sessionid int, Wow64 text, CreateTime text, ExitTime text)")

cur.executemany("insert into pstree values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", result)
conn.commit()

conn.close()