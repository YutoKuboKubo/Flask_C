from flask import request, redirect, url_for, render_template, flash, session
from salary import app

@app.route('/')
def show_entries():
    input_data = session.get("input_data", None)
    return render_template('input.html', input=input_data)

@app.route('/output', methods =['GET', 'POST'])
def output():
    session["input_data"] = ""
    if request.method == 'POST':
        input_salary = request.form["salary"]
        if input_salary == "":
            flash('給与が未入力です。入力してください。')
            return redirect(url_for("show_entries"))
        elif len(input_salary) > 10:
            flash('給与には最大9,999,999,999まで入力可能です。')
            session["input_data"] = input_salary
            return redirect(url_for("show_entries"))
        elif int(input_salary) < 0:
            flash('給与にはマイナスの値は入力できません。') 
            session["input_data"] = input_salary
            return redirect(url_for("show_entries"))
        else:
            input_salary = int(request.form["salary"])
            if input_salary <= 1000000:
                input_tax = int(input_salary * 0.1)
            else:
                input_tax = int(1000000 * 0.1 + (input_salary - 1000000) * 0.2)
            input_pay = input_salary - input_tax
            return render_template("output.html", salary=input_salary, pay=input_pay, tax=input_tax)
    
@app.route('/back')
def back():
    return redirect(url_for("show_entries"))
