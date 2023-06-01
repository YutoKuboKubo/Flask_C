from calcsalary_app import app
from flask import request, redirect, url_for, render_template, flash, session


@app.route('/', methods=["GET", "POST"])
def input():
    if request.method == "POST":
        salary = int(request.form['salary'])
        if salary > 1000000:
            tax_amount = int((salary - 1000000) * 0.2 + (1000000 * 0.1))
        else:
            tax_amount = int(salary * 0.1)
        payment = salary - tax_amount
        salary = "{:,}".format(salary)
        tax_amount = "{:,}".format(tax_amount)
        payment = "{:,}".format(payment)
        return render_template('output.html', salary=salary, tax_amount=tax_amount, payment=payment)
    return render_template('input.html')

@app.route('/output', methods=["GET", "POST"])
def output():
    if request.method == "POST":
        return render_template('input.html')
    return render_template('output.html')
