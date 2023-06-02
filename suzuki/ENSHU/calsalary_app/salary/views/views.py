from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP
import re

@app.route('/', methods=['GET', 'POST'])
def input():
    input_data = session.get('input_data', None)
    return render_template("input.html", input = input_data)    

@app.route('/output', methods=['GET', 'POST'])
def output():
    session["input_data"] = ""
    if request.form["salary"] == "":
        flash('ERROR！ 給与が未記入です。')
        return redirect(url_for('input')) # アラート
    if int(request.form["salary"]) > 9999999999:
        flash('ERROR！ 給与には最大9,999,999,999まで入力可能です。')
        return redirect(url_for('input'))
    if int(request.form["salary"]) < 0:
        flash('ERROR！ 給与にはマイナスの値は入力できません。')
        return redirect(url_for('input'))

    if request.method == "POST": # 給与
        input_salary = int(request.form["salary"])
        if (input_salary > 1000000):
            tax = (input_salary - 1000000) * 0.2 + 100000
        else:
            tax = input_salary * 0.1
        tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
        pay = input_salary - tax
    return render_template("output.html",  salary=input_salary, tax=tax, pay=pay)



#   カンマ区切り出力の為に出力テキストをView側で作成する場合       
#        text = "給与:" + "{:,}".format(input_salary) + " 円の場合、支給額：" + "{:,}".format(pay) + " 円、税額：" + "{:,}".format(tax) + " 円"
#    return render_template("output.html", text=text)

    