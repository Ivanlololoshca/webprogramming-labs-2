from flask import Blueprint, redirect, url_for, render_template

lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/example/')
def example():
    name = 'Григорович В.С. Левенец И.А.' 
    lab_num = 'Лабораторная работа 2'
    group = 'ФБИ-11'
    course = '3 курс'
    fruits = [
      {'name':'яблоки', 'price':100},
      {'name':'груши', 'price':120},
      {'name':'апельсины', 'price':80},
      {'name':'мандарины', 'price':95},
      {'name':'манго', 'price':375},
    ]
    books = [
      {'name':'Царство живтоных', 'price':328},
      {'name':'Поваренная книга', 'price':1000},
      {'name':'Опасная природа', 'price':3392},
      {'name':'Том Круз', 'price':32494},
      {'name':'Гарри Поттер', 'price':4833},
    ]
    return render_template('example.html')

@lab2.route('/lab2/')
def lab__2():
    return render_template('lab2.html')


@lab2.route('/lab2/smex/')
def smex():
    return render_template('smex.html')


