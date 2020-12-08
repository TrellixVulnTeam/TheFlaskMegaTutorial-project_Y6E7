from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me {}'.format(
            form.username.data, form.remember_me.data))
        flash('Login dummy')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)

@app.route('/')
@app.route('/index')
def index():
    links = [
        {'name':'Login','class':'login'},
        {'name':'Add','class':'inprogress'},
        {'name':'Poop','class':'inprogress'},
        {'name':'Le booze','class':'inprogress'},
        {'name':'List','class':'index'}
    ]
    user = {'username':'geexmmo'}
    devices = [
        {'number':'1001','address':{'mac':'DE:AD:BE:EF:FF'}},
        {'number':'1002','address':{'mac':'FF:FE:EB:DA:ED'}},
        {'number':'1003','address':{'mac':'FF:FF:EE:FF:FF'}}]
    return render_template('index.html', title='Home', user=user, links=links, devices=devices)

@app.route('/inprogress')
def inprogress():
    return render_template('inprogress.html')