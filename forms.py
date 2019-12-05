from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired


class TestForm(FlaskForm):
    url = URLField('URL', validators=[DataRequired()])
    display = ['url']


class SearchForm(FlaskForm):
    selectData = [
        ('평택시', '평택시'),
        ('가평군', '가평군'),
        ('경기도', '경기도'),
        ('고양시', '고양시'),
        ('과천시', '과천시'),
        ('광명시', '광명시'),
        ('광주시', '광주시'),
        ('구리시', '구리시'),
        ('군포시', '군포시'),
        ('김포시', '김포시'),
        ('남양주시', '남양주시'),
        ('동두천시', '동두천시'),
        ('부천시', '부천시'),
        ('성남시', '성남시'),
        ('수원시', '수원시'),
        ('시흥시', '시흥시'),
        ('안산시', '안산시'),
        ('안성시', '안성시'),
        ('안양시', '안양시'),
        ('양주시', '양주시'),
        ('양평군', '양평군'),
        ('여주시', '여주시'),
        ('연천군', '연천군'),
        ('오산시', '오산시'),
        ('용인시', '용인시'),
        ('의왕시', '의왕시'),
        ('의정부시', '의정부시'),
        ('이천시', '이천시'),
        ('파주시', '파주시'),
        ('포천시', '포천시'),
        ('하남시', '하남시'),
        ('화성시', '화성시')
    ]
    location = SelectField('location', choices=selectData, validators=[DataRequired()])
    query = StringField('query', validators=[DataRequired()])
    display = ['location', 'query']