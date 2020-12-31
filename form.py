from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, FileField, IntegerField, SubmitField, PasswordField
from wtforms import validators


# To DO 
# These should be added to the template as well later
NATIONAL_ID_SEC = 'ثبت نام کارت ملی'
PASSPORT_SEC = 'ثبت نام گذرنامه'
DRIVING_SEC = 'ثبت نام گواهینامه'
DRIVING_SCHOOL_SEC = 'ثبت آموزشگاه رانندگی'
TRAFFIC_REC_SEC = 'خلافی خودرو'

class Login(FlaskForm):
    user_name = StringField('نام کاربری')
    password = PasswordField('رمز ورود')



class DemandForm(FlaskForm):
    f_name = StringField('نام',
                         [validators.DataRequired(message='لطفا این فیلد را پر کنید')])
    l_name = StringField('نام خانوادگی',
                         [validators.DataRequired(message='لطفا این فیلد را پر کنید')])
    national_id = IntegerField('کد ملی',
                               [validators.DataRequired(message='لطفا این فیلد را پر کنید')])
    birth_certificate_id = IntegerField('شماره شناسنامه',
                                        [validators.DataRequired(message='لطفا این فیلد را پر کنید')])
    finger_print = FileField('عکس اثر انگشت')
    personal_image = FileField('عکس پرسنلی')
    submit = SubmitField('ارسال')

# To DO
# [] Define classes inherit from the Demand for each section

class DrivingSchoolForm(FlaskForm):
    name = StringField('نام آموزشگاه',
                       [validators.DataRequired()])
    address = StringField('آدرس',
                          [validators.DataRequired()])
    tel_number = IntegerField('تلفن',
                              [validators.DataRequired()])
    api_address = IntegerField('آدرس API',
                               [validators.DataRequired()])


class TrafficRecordForm(FlaskForm):
    vin = IntegerField('کد VIN',
                        [validators.DataRequired()])
