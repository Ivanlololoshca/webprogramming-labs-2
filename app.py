from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Левенец Иван Вачеслав Григорович</title>
        </head>
    <body>
   <header>
         НГТУ ФБИ-11 Лабораторная работа 1 
        <h1> web-cервер на flask </h1>
   <header>

    </body>
    <footer>
        @copy; Левенец Иван Вачеслав Григорович ФБИ-11 3курс,2023
    <footer>
</html>
"""
