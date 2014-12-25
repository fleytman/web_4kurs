# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect
from app import app, db, models
from forms import SearchForm

#Подключение search.html и передача методов GET,POST
@app.route('/', methods = ['GET', 'POST'])
@app.route('/search', methods = ['GET', 'POST'])
def search():
    form = SearchForm()
    #При нажатие на кнопку "Найти" в form.search.data передут введёные данные
    if form.validate_on_submit():
        flash("Введённый штрихкод: ".decode("utf8") + unicode(form.search.data))

        for foodstuff_name, in db.session.query(models.Foodstuff.foodstuff_name).filter_by(gtin = form.search.data):
            flash("Название продукта: ".decode("utf8")+unicode(foodstuff_name))
        for trademark, in db.session.query(models.Foodstuff.trademark).filter_by(gtin = form.search.data):
            flash("Марка производителя: ".decode("utf8")+unicode(trademark))
        for measure, in db.session.query(models.Foodstuff.measure).filter_by(gtin = form.search.data):
            flash("Мера: ".decode("utf8")+unicode(measure))
        for ingredients, in db.session.query(models.Foodstuff.ingredients).filter_by(gtin = form.search.data):
            flash("Состав: ".decode("utf8")+unicode(ingredients))

        #Страница перенаправит приложение после нажатия на кнопку "Найти"
        return redirect('/search')
    return render_template("search.html",
         title="search",
         form = form)