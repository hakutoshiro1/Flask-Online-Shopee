from market import app,db
from flask import render_template,redirect,url_for
from market.models import Item,User
from market.forms import RegisterForm


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html',products=items)

@app.route('/register',methods=['GET','POST'])
def register_page():
    form= RegisterForm()

    if form.validate_on_submit():
        user=User(
            username=form.username.data,
            email=form.email.data,
            password_hash=form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('market_page'))
    
    if form.errors != {}:
        for i in form.errors.values():
            print(i)
    return render_template('register.html',form=form)