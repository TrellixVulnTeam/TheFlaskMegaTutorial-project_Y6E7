from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    links = [
        {'name':'Add','href':'/newdevice'},
        {'name':'List','href':'/index'}
    ]
    user = {'username':'geexmmo'}
    devices = [
        {'number':'1001','address':{'mac':'DE:AD:BE:EF:FF'}},
        {'number':'1002','address':{'mac':'FF:FE:EB:DA:ED'}},
        {'number':'1003','address':{'mac':'FF:FF:EE:FF:FF'}}]
    return render_template('index.html', title='Home', user=user, links=links, devices=devices)