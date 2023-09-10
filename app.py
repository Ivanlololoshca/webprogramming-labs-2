from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/lab1")
def start():
    return redirect ("/menu", code=302)

@app.route("/menu")
def menu():
    return """



 #def start():
   # почему-то не работает с return start



<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>НГТУ, ФБИ-11, Лабораторные работы</title>
    </head>
        <body>
        <header>
            НГТУ,ФБИ-11, WEB-программирование, часть 2. Список лабораторных
        </header>
        <h1> web-cервер на flask </h1>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.

        <footer>
            @copy; Левенец Иван Вачеслав Григорович ФБИ-11 3курс,2023
        </footer>

    </body>

        
</html>
"""
