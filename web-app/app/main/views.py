from app import app
from flask import render_template
import os
import yaml

@app.route('/')
def home():
    yaml_path = '/app/web-app/slas.yaml'
    
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
    
    slas = data.get('slas', [])
    
    return render_template('home.html', slas=slas)
