from flask import request, redirect, url_for, render_template, flash, session
from salary import app

BORDER = 1000000
TAX_LOW = 0.1
TAX_HIGHT = 0.2

@app.route('/', methods = ['GET', 'POST'])
def input():
    input_num = session.get('input_num', None)
    return render_template('input.html', input = input_num)


@app.route('/output', methods = ['GET', 'POST'])
def output():
    input_salary = request.form["salary"]
    # 値のチェック
    if input_salary == "":
        flash('給与が未入力です。入力してください。')
        return redirect(url_for('input'))
    if int(input_salary) < 0:
        flash('給与にはマイナスの値は入力できません。')
        session["input_num"] = input_salary
        return redirect(url_for('input'))
    if len(input_salary) > 10:
        flash('給与には最大9,999,999,999まで入力可能です。')
        session["input_num"] = input_salary
        return redirect(url_for('input'))

    if request.method == "POST":
        session["input_num"] = input_salary
        input_salary = int(input_salary)
        tax = 0 # 税額
        pay = input_salary # 支給額
        if (input_salary > BORDER):
            tax = (input_salary - BORDER) * TAX_HIGHT + BORDER * TAX_LOW
        else:
            tax += input_salary * TAX_LOW
        pay = pay - tax
    return render_template("output.html", salary = "{:,}".format(input_salary), pay = "{:,}".format(int(pay)), tax = "{:,}".format(int(tax)))