from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
from datetime import datetime,timedelta
import time as t
from threading import Thread
'''import RPi.GPIO as m

m.setmode(m.BCM)
m.setup(21,m.OUT)
m.setwarnings(False)
m.output(21,0)
def longbell():
    m.output(21,1)
    t.sleep(6)
    m.output(21,0)

def shortbell():
    m.output(21,1)
    t.sleep(2)
    m.output(21,0)
    t.sleep(1)'''
app=Flask(__name__)
app.secret_key = 'PBSAasdertyuiop2020'
@app.route('/')
def login():
    return render_template('login.html')
@app.route('/loginvalidation',methods = ["POST"])
def loginvalid():
    username = request.form['username']
    password = request.form['password']
    if username=="admin" and password=="asdf":
        return render_template('selection2.html')
    else:
        return render_template('login.html')


di = {0:"decision"}
#de = {0:"normaldays",1:"internal",2:"endsem",3:"stop"}
def total(act,start,end):
	print(di)
	a = datetime.strptime(start,"%Y-%m-%d")
	b = datetime.strptime(end,"%Y-%m-%d")
	delta = b-a
	print("Total number of days: ",delta.days)
	print(act)
	while di[0]== act:
		#di[0] = "decision"
		print(di)
		break
	else:
		di[0] = act
		print(di)
		dates = {}
		for i in range(0,delta.days):
			day = a + timedelta(days=i)
			dates[str(day)[0:10]] = i+1
		print("Total dates dictionary:",dates)
		if(act == "normaldays"):
			s = {"08:00:00":2,"08:50:00":3,"09:40:00":4,"10:30:00":5,"10:45:00":6,"11:35:00":7,"12:25:00":8,"13:15:00":9,"14:05:00":10,"14:55:00":11,"15:10:00":12,"16:00:00":13,"16:50:00":14,"17:40:00":15}
			c = {"08:00:00":2,"08:50:00":1,"09:40:00":2,"10:30:00":3,"10:45:00":1,"11:35:00":4,"12:25:00":5,"13:15:00":1,"14:05:00":2,"14:55:00":3,"15:10:00":1,"16:00:00":4,"16:50:00":5,"17:40:00":6}
			s_k = list(s.keys())
			l = {"07:45:00":1}
			q = 0
		elif(act=="internal"):
			s = {"08:50:00":2,"08:55:00":3,"09:00:00":4,"09:30:00":5,"10:00:00":6,"10:25:00":7,"10:50:00":10,"10:55:00":11,"11:00:00":12,"11:30:00":13,"12:00:00":14,"12:25:00":15,"13:20:00":18,"13:25:00":19,"13:30:00":20,"14:00:00":21,"14:30:00":22,"14:55:00":23,"15:20:00":26,"15:25:00":27,"15:30:00":28,"17:15:00":29,"17:11:00":30,"16:55:00":31}
			l = {"08:45:00":1,"10:30:00":8,"10:45:00":9,"12:30:00":16,"13:15:00":17,"15:00:00":24,"15:15:00":25,"17:00:00":32}
			c = {"08:50:00":1,"08:55:00":2,"09:00:00":3,"09:30:00":1,"10:00:00":2,"10:25:00":1,"10:50:00":1,"10:55:00":2,"11:00:00":3,"11:30:00":1,"12:00:00":2,"12:25:00":1,"13:20:00":1,"13:25:00":1,"13:30:00":3,"14:00:00":1,"14:30:00":2,"14:55:00":1,"15:20:00":1,"15:25:00":2,"15:30:00":3,"17:15:00":1,"17:11:00":2,"16:55:00":1}
			s_k = list(s.keys())
			q = 0
		elif(act=="semester"):
			s = {"08:50:00":2,"08:55:00":3,"09:00:00":4,"09:30:00":5,"10:00:00":6,"10:30:00":7,"11:00:00":8,"11:30:00":9,"11:45:00":10,"13:50:00":13,"13:55:00":14,"14:00:00":15,"14:30:00":16,"15:00:00":17,"15:30:00":18,"16:00:00":19,"16:30:00":20,"16:45:00":21}
			l = {"08:45:00":1,"12:00:00":11,"13:45:00":12,"17:00:00":22}
			c = {"08:50:00":1,"08:55:00":2,"09:00:00":3,"09:30:00":1,"10:00:00":2,"10:30:00":3,"11:00:00":4,"11:30:00":5,"11:45:00":1,"13:50:00":1,"13:55:00":2,"14:00:00":3,"14:30:00":1,"15:00:00":2,"15:30:00":3,"16:00:00":4,"16:30:00":5,"16:45:00":1}
			s_k = list(s.keys())
			q = 0
		elif(act=="stop"):
			s = {}
			l = {}
			c = {}
			s_k = list(s.keys())
			q = 0
		elif(act=="stay"):
			s = {}
			l = {}
			c = {}
			s_l = list(s.keys())
			q = 0
		while q<len(dates) and act== di.get(0):
			p = 0
			while p < len(s)+len(l) and act == di.get(0):
				date = t.strftime("%Y-%m-%d")
				m = t.strftime("%H:%M:%S")
				if m in l and date in dates:
					print(m)
					p = 1 if l.get(m) is None else l.get(m)
					print("p = ",p)
					q = len(dates) if dates.get(date) is None else dates.get(date)
					print("q = ",q)
					print("long bell")
					#longbell()
					t.sleep(1)
				elif m in s and date in dates:
					p = 1 if s.get(m) is None else s.get(m)
					print("p = ", p)
					q = len(dates) if dates.get(date) is None else dates.get(date)
					print("q = ", q)
					r = c.get(m)
					print("The bell should ring", r," times")
					for i in range(r):
						print("bell rings")
						#shortbell()
						t.sleep(1)

def new(d_s,d_l,c):
    p = 0
    s_k = list(d_s.keys())
    while p < len(d_s)+len(d_l):
        m = t.strftime("%H:%M:%S")
        if m in d_l:
            print(m)
            p = 1 if d_l.get(m) is None else d_l.get(m)
            print("p = ",p)
            print("long bell")
            #longbell()
            t.sleep(1)
        elif m in d_s:
            print(m)
            p = 1 if d_s.get(m) is None else d_s.get(m)
            print("p = ",p)
            r = c.get(m)
            print("The bell should ring", r," times")
            for i in range(r):
                print("bell rings")
                #shortbell()
                t.sleep(1)
    print("while loop exits")

def EMERGENCY():
    print("longbell")
    #longbell()
    date = t.strftime("%Y-%m-%d")
    a = datetime.strptime(date,"%Y-%m-%d")
    b = a + timedelta(days=1)
    s_d = str(a)[0:10]
    print(s_d)
    e_d = str(b)[0:10]
    print(e_d)
    #all("stay",s_d,e_d)
    thr = Thread(target = total, args=["stay",s_d,e_d])
    thr.start()

@app.route('/classify',methods = ["GET","POST"])
def classify():
    action = request.form['regular']
    #print(action)
    if action == 'regular':
            return render_template('selection1.html')
    #elif action == 'examination':
    #        return render_template('selection page.html')
    elif action == 'emergency':
            thr = Thread(target = EMERGENCY)
            thr.start()
            return render_template('login.html')
    elif action == 'create':
            return redirect(url_for('create'))
    #elif action == 'stop':
    #        return render_template('selection2.html')
@app.route('/exam',methods=["POST","GET"])
def exam():
    a = request.form
    print(a)
    con = sql.connect("real1.db") 
    cur = con.cursor()
    cursor = con.execute("SELECT name from sqlite_master WHERE type = 'table' AND name = 'DATE';")
    result = cursor.fetchone()
    cur.execute("DROP TABLE IF EXISTS DATA")
    print("table droped successfully")
    cur.execute('''CREATE TABLE IF NOT EXISTS DATA(SNO INTEGER PRIMARY KEY AUTOINCREMENT,DAY TEXT NOT NULL,STARTDATE TEXT NOT NULL,ENDDATE TEXT NOT NULL)''')
    cur.execute("INSERT INTO DATA(DAY,STARTDATE,ENDDATE) VALUES (?,?,?)",(str(a['internal']),str(a['startDate']),str(a['endDate']),))
    con.commit()
    #con.close()
    print("database saved")
    flash("Successfully Saved")
    cursor =con.execute("select DAY,STARTDATE,ENDDATE from DATA")
    action = request.form['internal']
    for row in cursor:
        print(row[0])
        print(row[1])
        print(row[2])
        act = row[0]
        s_d = row[1]
        e_d = row[2]
    action = request.form['internal']
    #all(act,s_d,e_d)
    thr = Thread(target = total, args = [act,s_d,e_d])
    thr.start()
    return render_template('selection1.html')
    '''if act=="internal" and action==row[0]:
        inter(row[1],row[2])
        return render_template('selection1.html')
    elif act=="semester" and action == row[0]:
        endsem(row[1],row[2])
        return render_template('selection1.html')
    elif act=="normaldays" and action == row[0]:
        REGULAR(row[1],row[2])
        return render_template('selection1.html')
    elif act== 'stop' and action == row[0]:
        stay(row[1],row[2])
        return render_template('selection1.html')
    return render_template('selection1.html')'''
 

def stop():
    return "stop"
    

@app.route('/create',methods=["GET","POST"])
def create():
    time = []
    text = []
    bell = []
    if request.method=="POST":
        if request.form.get("submit"):
            print(len(request.form))
            data = request.form.to_dict(flat=False)
            total = len(data)+1
            t = int(total/3)
            for i in range(0,t):
                ti=data['time'+str(i)]
                te=data['text'+str(i)]
                be=data['select'+str(i)]
                time.append(ti)
                text.append(te)
                bell.append(be)
            con = sql.connect("real.db") 
            cur = con.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS SchoolBells(SNO INTEGER PRIMARY KEY AUTOINCREMENT,TIME TEXT NOT NULL,BELLS TEXT NOT NULL,COUNT INT NOT NULL)''')
            for i in range(0,len(time)):
                cur.execute("INSERT INTO SchoolBells(TIME,COUNT,BELLS) VALUES (?,?,?)",(str(time[i][0]),str(text[i][0]),str(bell[i][0]),))
            con.commit()
            con.close()
            print("database saved")
            flash("Successfully Saved")
            print(time)
            print(text)
            print(bell)
            d_s = {}
            d_l = {}
            c = {}
            for i in range(0,t):
                if bell[i][0] == 'short bell':
                    d_s[time[i][0]] = i+1
                    c[time[i][0]]=int(text[i][0])
                if bell[i][0] == 'long bell':
                    d_l[time[i][0]] = i+1
            print(d_s)
            print(d_l)
            print(c)
            #new(d_s,d_l,c)
            thr = Thread(target= new, args=[d_s,d_l,c])
            thr.start()
            return redirect(url_for('create'))
        elif request.form.get("display"):
            return redirect(url_for('alarmschedule'))
        elif request.form.get("clear"):
            return redirect(url_for('clear'))
        return render_template('create.html') 
    else:
        flash("Server Error")
        return render_template("create.html")

@app.route('/clear',methods=["GET","POST"])
def clear():
    con = sql.connect("real.db") 
    cur = con.cursor()
    cur.execute("DROP TABLE SchoolBells")
    con.commit()
    con.close()
    print("table dropped successfully")
    flash("Successfully Cleared the Database")
    return redirect(url_for('create'))

@app.route("/alarmschedule",methods=["GET","POST"])
def alarmschedule():
    if request.method=="POST":
        if request.form.get("submit"):
            return redirect(url_for('create'))
        elif request.form.get("clear"):
            return redirect(url_for('clear'))
        elif request.form.get("display"):
            return redirect(url_for('alarmschedule'))

    try:
        con = sql.connect("real.db")
        con.row_factory = sql.Row 
        cur = con.cursor()
        cur.execute("SELECT SNO,TIME,BELLS,COUNT FROM SchoolBells")
        rows = cur.fetchall()
        print(rows)
        return render_template('scheduledisplayer.html',items= rows)
    except:
        return "<h1>Error , Oops Server Error</h1>"


if __name__=='__main__':
    app.run(debug = True)
    #app.run(host='0.0.0.0',port=8080,debug=True,use_reloader=True)
        
