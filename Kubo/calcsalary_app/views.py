from calcsalary_app import app
from flask import request, redirect, url_for, render_template, flash, session


@app.route('/', methods=["GET", "POST"])
def input():
    input_val = session.get('input_data', None)
    return render_template('input.html', data=input_val)

MILLION = 1000000
UPPER_TAX = 0.2
LOWER_TAX = 0.1
@app.route('/output', methods=['GET', 'POST'])
def output():
    if request.method == "POST":
        if request.form['salary'] == '':
            flash('給与が未入力です。入力してください。')
        else:
            salary = int(request.form['salary'])
            if salary >= 10000000000:
                flash('給与には最大9,999,999,999まで入力可能です。')
                session['input_data'] = salary  # セッションに値を保存し、input.htmlに渡す
                return redirect(url_for('input'))
            elif salary < 0:
                flash('給与にはマイナスの値は入力できません。')
                session['input_data'] = salary  # セッションに値を保存し、input.htmlに渡す
                return redirect(url_for('input'))
            else:
                session.pop('input_data', None)  # セッションを削除
                if salary > MILLION:
                    tax_amount = int((salary - MILLION) * UPPER_TAX + (MILLION * LOWER_TAX))
                else:
                    tax_amount = int(salary * LOWER_TAX)
                payment = salary - tax_amount
                salary = "{:,}".format(salary)
                tax_amount = "{:,}".format(tax_amount)
                payment = "{:,}".format(payment)
                return render_template('output.html', salary=salary,
                                       tax_amount=tax_amount, payment=payment)
    return render_template('input.html')
