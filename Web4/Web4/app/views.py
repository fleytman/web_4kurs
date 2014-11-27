# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect
from app import app
from forms import SearchForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
        title = 'Home')

@app.route('/search', methods = ['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash("¬веденный штрихкод: ".decode("cp1251") + unicode(form.search.data))
        return redirect('/index')
    return render_template("search.html",
         title="search",
         form = form)