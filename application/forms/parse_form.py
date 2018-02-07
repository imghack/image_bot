from wtforms import Form, StringField, IntegerField, validators


class ParseForm(Form):
    url = StringField('url', [
        validators.DataRequired(),
        validators.Length(min=4, max=1000)
    ])
    quantity = IntegerField('quantity', [
        validators.DataRequired(),
        validators.NumberRange(min=1, max=100)
    ])
