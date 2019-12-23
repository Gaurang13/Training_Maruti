from flask_restful import Resource
from flask import render_template, request, current_app, flash, redirect, url_for
from comman.utility import output_html
from Database.search import search

class search(Resource):
    def get(self):
        return output_html(render_template('search.html'), 200)
    def post(self):
        sname = request.form['sname']
        scategory = request.form['category']
        if sname:
            search(s_name = sname, s_category = scategory)
