# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect
from app import app
from forms import SearchForm

#Подлючение index.html
@app.route('/index')
def index():
    return render_template("index.html",
        title = 'Home')

#Подключение search.html и передача методов GET,POST
@app.route('/', methods = ['GET', 'POST'])
@app.route('/search', methods = ['GET', 'POST'])
def search():
    form = SearchForm()
    #При нажатие на кнопку "Найти" в form.searc.data передут введёные данные
    if form.validate_on_submit():
        flash("Введённый штрих код: ".decode("utf8") + unicode(form.search.data))
        #Страница перенаправит приложение после нажатия на кнопку "Найти"
        return redirect('/search')
    return render_template("search.html",
         title="search",
         form = form)