import sqlite3

def connect():
    conn=sqlite3.connect("storage.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS storage (id INTEGER PRIMARY KEY, start text, end text, task text, note text);")
    conn.commit()
    conn.close

def add_entry(start, end, task, note):
    conn=sqlite3.connect("storage.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO storage VALUES (NULL, ?, ?, ?, ?)",(start, end, task, note))
    conn.commit()
    conn.close

def search_entry(task="", start="", end="", note=""):
    conn=sqlite3.connect("storage.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM storage WHERE task LIKE ? AND start LIKE ? AND end LIKE ? AND note LIKE ?",('%' + task + '%', '%' + start + '%', '%' + end + '%', '%' + note + '%'))
    rows=cur.fetchall()
    conn.close
    return rows


def edit_entry(id, task, start, end, note):
    conn=sqlite3.connect("storage.db")
    cur=conn.cursor()
    cur.execute("UPDATE storage SET task=?, start=?, end=?, note=?", (task, start, end, note))
    conn.commit()
    conn.close


def delete_entry(id):
    conn=sqlite3.connect("storage.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM storage WHERE id=?", (id,))
    conn.commit()
    conn.close()

def show_all():
    conn=sqlite3.connect("storage.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM storage")
    rows=cur.fetchall()
    conn.close
    return rows

def export_all():
    with open('report.csv', 'w+') as write_file:
        conn = sqlite3.connect("storage.db")
        cur = conn.cursor()
        for row in cur.execute('SELECT * FROM storage'):
            write_file.write(str(row))