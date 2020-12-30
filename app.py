from flask import Flask, render_template, redirect, session, url_for, request
from flask_bootstrap import Bootstrap
from form import BaseForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
# for extra security should be add to environment variables
app.config['SECRET_KEY'] = 'hard to geuess string'

@app.route('/')
def dashboard():
    messages = [
        {'name': 'مهران شهیدی', 'time': 3, 'image':'img.jpg',
            'text': 'آقای محسن کلوندی نیاز به ویرایش دارد...'},
        {'name': 'امیرعباس اسدی', 'time': 5, 'image':'img.jpg',
         'text': 'من عرفان سیف رو از سیستم حذف کردم'}
    ]
    return render_template('public/base.html', messages=messages)

@app.route('/form/<section>',methods=['GET', 'POST'])
def form(section):
    form = BaseForm()
    if request.method == 'POST':
        session['name'] = form.f_name.data + ' ' + form.l_name.data
        return '''<h2>
                نام: {}
                شماره ملی: {}
                {}
                ثبت شد'''.format(form.f_name.data+' ' + form.l_name.data,
                     form.national_id.data, form.validate_on_submit())

    return render_template('public/form.html', form=form, title=section)

@app.route('/login')
def login():
    return render_template('public/login.html')