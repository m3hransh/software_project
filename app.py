from flask import Flask, render_template, redirect, session, url_for, request
from form import DemandForm, DrivingSchoolForm, TrafficRecordForm
from model import Demand
from form import NATIONAL_ID_SEC, PASSPORT_SEC, DRIVING_SCHOOL_SEC, DRIVING_SEC, TRAFFIC_REC_SEC

app = Flask(__name__)
# for extra security should be add to environment variables
app.config['SECRET_KEY'] = 'hard to geuess string'


@app.route('/')
def dashboard():
    """Main page for staffs."""
    messages = [
        {'name': 'مهران شهیدی', 'time': 3, 'image': 'img.jpg',
            'text': 'آقای محسن کلوندی نیاز به ویرایش دارد...'},
        {'name': 'امیرعباس اسدی', 'time': 5, 'image': 'img.jpg',
         'text': 'من عرفان سیف رو از سیستم حذف کردم'}
    ]
    return render_template('public/base.html', messages=messages)


def find_form(section):
    """"Return corrosponding form for the section"""
    if section == PASSPORT_SEC:
        form = DemandForm()
    elif section == NATIONAL_ID_SEC:
        form = DemandForm()
    elif section == DRIVING_SEC:
        form = DemandForm()
    elif section == DRIVING_SCHOOL_SEC:
        form = DrivingSchoolForm()
    elif section == TRAFFIC_REC_SEC:
        form = TrafficRecordForm()

    return form


@app.route('/form/<section>', methods=['GET', 'POST'])
def form(section):
    """ Demand registeration Page for staffs."""

    form = find_form(section)
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
    """Loging page for staffs."""
    return render_template('public/login.html')


@app.route('/track/<section>')
def track(section):
    """List of demands for specified section."""
    demands = [
        Demand('عرفان',
               'سیف',
               1234,
               461238471,
               49123412
               ),
        Demand('امیرعباس',
               'اسدی',
               4334,
               461298471,
               99123412
               )
    ]

    return render_template('public/tracking_staff.html', demands=demands, title=section)
