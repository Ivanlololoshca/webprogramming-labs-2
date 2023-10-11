from flask import Blueprint, redirect, url_for, render_template, request
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab_3():
    return render_template('lab3.html')

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполни поле простофиля !!!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполни поле простофиля !!!'

    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():
     return render_template('order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    if request.agrs.get('milk') == 'on'
        price += 30
    if request.agrs.get('sugar') == 'on'
        price += 20
    return render_template('pay.html', price=price)


