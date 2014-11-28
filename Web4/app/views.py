# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect
from app import app
from forms import SearchForm

@app.route('/index')
def index():
    return render_template("index.html",
        title = 'Home')

@app.route('/', methods = ['GET', 'POST'])
@app.route('/search', methods = ['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash("Введённый штрих код: ".decode("utf8") + unicode(form.search.data))
        return redirect('/search')
    return render_template("search.html",
         title="search",
         form = form)