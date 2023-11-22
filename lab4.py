from flask import Blueprint, render_template, request, make_response
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab_4():
    return render_template('lab4.html')

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'slava' and password == '123':
        return render_template('success.html', username=username)
    
    if username == 'slava':
        error = 'Вспоминаем пароль'
        return render_template('login.html', error=error, username=username, password = password)
    
    error = 'Вспоминаем логин и пароль'
    return render_template('login.html', error=error, username=username, password = password)

@lab4.route('/lab4/holodos', methods=['GET','POST'])
def holodos():
    if request.method == 'GET':
        return render_template('holodos.html')
   
    temp = request.form.get('temp')
    error=''

    if temp == '':
        error = 'Не задана температура'
    else:
        if temp:
            temp=int(temp)
            if (temp>-13) and 0>temp:
                if (temp>-13) and (-8>temp):
                    snow = '❄️❄️❄️'
                elif (temp>-9) and (-4>temp):
                    snow = '❄️❄️'
                elif (temp>-5) and (0>temp):
                    snow = '❄️'
                return render_template('su.html',temp=temp,snow=snow)

            if temp <-12:
                error = 'Cлишком низкое значение'
            if temp >-1:
                error = 'Cлишком высокое значение'

    return render_template('holodos.html',temp=temp,error=error)

    


@lab4.route('/lab4/yach', methods=['GET','POST'])
def corn():
    if request.method == 'GET':
        return render_template('yach.html')
    
    corn=request.form.get('corn')
    weight=request.form.get('weight')
    error=''

    
    if weight == '':
        error = 'Не введен вес'
    else:
    
        weight=int(weight)

        
        if weight > 50:
            sale = 0.9
            message = 'Применена скидка за большой объем'
        else:
            sale = 1
            message=''

        
        if corn == 'barley':
            corn = 'Ячмень'
            price = 12000 * weight * sale
        
        elif corn == 'oats':
            corn = 'Овёс'
            price = 8500 * weight * sale
        
        elif corn == 'wheat':
            corn = 'Пшеница'
            price = 8700 * weight * sale
        
        else:
            corn = 'Рожь'
            price = 14000 * weight * sale

        if (weight > 0) and (501 > weight):
                return render_template('yach2.html',corn=corn,weight=weight,price=price,message=message)
        
        if weight < 0 or weight == 0:
            error = 'Неверное значение веса'
        elif weight > 500:
            error = 'Объем отсутствует в наличии'
        
    return render_template('yach.html',corn=corn,weight=weight,error=error)


@lab4.route('/lab4/cookies', methods=['GET','POST'])
def cookies():
    if request.method == 'GET':
        return render_template('cookies.html')
   
    color = request.form.get('color')
    background_color = request.form.get('background_color')
    size = request.form.get('size')
    
    if size == '':
        return render_template('cookies.html')
    size = int(size)
    if size >=5 and size <=30:
        if color != background_color:
            size = str(size)
            res = make_response(render_template('cookies.html', color=color, background_color= background_color, size=size))
            res.set_cookie('background_color', background_color, path='/')
            res.set_cookie('color', color, path='/')
            res.set_cookie('size', size, path='/')
            return res, 303
    return render_template('cookies.html')
