from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators 
    @validates('name', 'phone_number')
    def validate_name(self, key, value):
        author_objects = Author.query.all()
        author_names = [author_object.name for author_object in author_objects]
        if key == 'name':
            if value == '':
                raise ValueError('Name cannot be empty.')
            elif value in author_names:
                raise ValueError('Name must be unique.')
        elif key == 'phone_number':
            if len(value) != 10:
                raise ValueError('Number issues.')
        return value
    
    # @validates('phone_number')
    # def validate_number(self, key, number_value):
    #     if number_value != 10:
    #         raise ValueError('Phone number must be 10 digits.')
    #     return number_value

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators  


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
