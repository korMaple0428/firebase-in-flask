#!${DEV_HOME}/tools/bin/python3
#--coding:utf-8

import os, json, pickle, random
from flask          import Flask, render_template, request, redirect, url_for, session
from app.util       import Common, Test

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def root():
    return render_template(
            'index.html', 
                _title  = "test_page"
            ,   _msg    = 'test'
            )

@app.route('/home', methods = ['GET'])
def home():
    return render_template(
            'index.html', 
                _title  = "test_page"
            ,   _msg    = 'test'
            )

