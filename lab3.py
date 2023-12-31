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

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 20
    return render_template('pay.html', price=price)

@lab3.route('/lab3/rgd')
def rgd():
    errors = {}
    pocypatel = request.args.get('pocypatel')
    if pocypatel == '':
        errors['pocypatel'] = 'Заполни поле простофиля !!!'

    tip = request.args.get('tip')

    polc = request.args.get('polc')

    bag = request.args.get('bag')

    fre = request.args.get('fre')
    if fre =='':
         errors['fre'] = 'Заполни поле простофиля !!!'

    viezd = request.args.get('viezd')
    if viezd == '':
        errors['viezd'] = 'Заполни поле простофиля !!!'

    priezd = request.args.get('priezd')
    if priezd == '':
        errors['priezd'] = 'Заполни поле простофиля !!!'

    data = request.args.get('data')
    if data == '':
        errors['data'] = 'Заполни поле простофиля !!!'
    return render_template('rgd.html', pocypatel=pocypatel, tip=tip, polc=polc, bag=bag, fre=fre, viezd=viezd, priezd=priezd, data=data, errors=errors)    
        
@lab3.route('/lab3/bilet')
def bilet():
    pocypatel = request.args.get('pocypatel')
   
    tip = request.args.get('tip')

    polc = request.args.get('polc')

    bag = request.args.get('bag')

    fre = request.args.get('fre')
    
    viezd = request.args.get('viezd')
    
    priezd = request.args.get('priezd')

    data = request.args.get('data')
    if data == '':
        
     return render_template('bilet.html', pocypatel=pocypatel, tip=tip, polc=polc, bag=bag, fre=fre, viezd=viezd, priezd=priezd, data=data)
    
