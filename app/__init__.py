#!${DEV_HOME}/tools/bin/python3
#--coding:utf-8

import os, json, pickle, random
from flask          import Flask, render_template, request, redirect, url_for, session
from app.util       import Common, Test

app = Flask(__name__)

@app.route('/', methods = ['GET'])
@app.route('/<var>', methods = ['GET'])
def root(var = '') :
    with open(os.environ["DEV_HOME"]  + "/conf/deploy.json", "r") as f :
        pages = json.load(f)
        return render_template(pages[var])

