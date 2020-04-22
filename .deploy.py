#!${DEV_HOME}/tools/bin/python3
#--coding:utf-8

import os, json, pickle, random
from jinja2 import Environment, FileSystemLoader

static_dir      = os.environ["DEV_HOME"] + "/app/static"
deploy_dir      = os.environ["FB_HOME"] + "/public/"

file_loader = FileSystemLoader(os.environ["DEV_HOME"] + "/app/templates")
env = Environment(loader=file_loader)


def render_template(path) :
    return env.get_template(path).render(
              _title = "test_page"
            , _msg   = "test"
            )

if __name__ == "__main__" :

    pages = list()
    pages.append({'name' : 'root', 'template' : 'index.html'});
    pages.append({'name' : 'home', 'template' : 'index.html'});

    for page in pages :
        dir_path = deploy_dir
        if page['name'] != 'root' :
            dir_path += page['name'] + "/"
            os.makedirs(dir_path, exist_ok=True)
        with open(dir_path + "index.html", "w") as f :
            f.write(render_template('index.html'))
