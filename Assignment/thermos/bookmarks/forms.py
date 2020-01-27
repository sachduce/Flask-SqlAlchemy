from flask_wtf import Form
from wtforms import StringField
from flask_wtf.html5 import URLField
from wtforms.validators import url, DataRequired, Regexp


class BookmarkForm(Form):
    url = URLField('Add url to bookmark', validators=[DataRequired(), url()])
    description = StringField('Provide description')
    tags = StringField('Tags',
                       validators=[Regexp(r'^[a-zA-Z0-9, ]*$', message="Tags can only contain letters and numbers")])

    def validate(self):
        if not (self.url.data.startswith('http://') or self.url.data.startswith('https://')):
            self.url.data = 'https://' + self.url.data
        if not Form.validate(self):
            return False
        if not self.description.data:
            self.description.data = self.url.data

        stripped = [t.strip() for t in self.tags.data.split(',')]
        not_empty = [tag for tag in stripped if tag]
        tagset = set(not_empty)
        self.tags.data = ','.join(tagset)
        return True






