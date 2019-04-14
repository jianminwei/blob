import datetime, re

from app import db

def slugify(s):
   return re.sub('[^\w]+', '-', s).lower()

entry_tags = db.Table('entry_tags',
        db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
        db.Column('entry_id', db.Integer, db.ForeignKey('entry.id'))
)


class Entry(db.Model):
   STATUS_PUBLIC = 0
   STATUS_DRAFT = 1

   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100))
   slug = db.Column(db.String(100), unique=True)
   body = db.Column(db.Text)
   status = db.Column(db.SmallInteger, default=STATUS_PUBLIC)
   created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
   modified_timestamp = db.Column( db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

   tags = db.relationship('Tag', secondary = entry_tags, backref = db.backref('entries', lazy = 'dynamic'))

   def __init__(self, *args, **kwargs):
      super(Entry, self).__init__(*args, **kwargs) # Call parent constructor.
      self.generate_slug()

   def generate_slug(self):
      self.slug = ''
      if self.title:
         self.slug = slugify(self.title)

   def __repr__(self):
      return '<Entry: %s>' % self.title

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    slug = db.Column(db.String(64), unique = True)

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '<Tag %s>' % self.name



if __name__ == '__main__':
    db.create_all()


    python = Tag(name='Python')
    flask = Tag(name='Flask')
    django = Tag(name='Django')
    random_thoughts = Tag(name='Random Thoughts')

    db.session.add_all([python, flask, django, random_thoughts])
    db.session.commit()

    python_entry = Entry(title='Python post', body='My first Python post', tags=[python])
    flask_entry = Entry(title='Flask post', body='My first Flask post', tags=[python, flask])
    flask_entry2 = Entry(title='More Flask', body='My Second Flask post', tags=[python, flask])
    django_entry = Entry(title='Django post', body='My Django post', tags=[python, django])
    random_entry= Entry(title='Random Thoughts post', body='Keep learning Python, JavaScript, Flask and React', tags=[random_thoughts])

    db.session.add_all([python_entry, flask_entry, flask_entry2, django_entry, random_entry])
    db.session.commit()



