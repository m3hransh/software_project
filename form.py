from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, FileField, IntegerField, SubmitField
from wtforms import validators


class Login(FlaskForm):
    user = StringField('')

class BaseForm(FlaskForm):
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

