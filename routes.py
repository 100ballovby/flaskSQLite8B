from app import app
from flask import render_template, request
import sqlite3 as sql


@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST': # если мне отправили данные
        try: # попытаться сделать это:
            name = request.form['name']
            addr = request.form['address']
            city = request.form['city']
            pin = request.form['pin']
            # ^ вот тут я сохранил в переменные информацию из формы
            with sql.connect('main.db') as con:
                cur = con.cursor()
                cur.execute('INSERT INTO students (name, addr, city, pin) VALUES (?,?,?,?)',
                            (name, addr, city, pin))
                con.commit()
                msg = 'Successfully inserted'
        except: # если возникает ошибка
            con.rollback()
            msg = 'Error inserting'
        finally:
            con.close()
            return render_template('result.html', message=msg)
    else:
        return render_template('student.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/students')
def list_students():
    con = sql.connect('main.db')
    con.row_factory = sql.Row  # забираю все строки из БД

    cur = con.cursor()  # курсор производит все действия с БД
    cur.execute('SELECT * FROM students')
    # достать все данные из таблицы students

    rows = cur.fetchall()  # fetchall - собрать всех студентов и записать в переменную

    return render_template('result.html', rows=rows)
