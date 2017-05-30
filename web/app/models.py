from .app import app, db
from datetime import datetime

# each uploaded image
class Face_Image(db.Model):
    __tablename__ = 'face_image'

    id = db.Column(db.Integer, primary_key=True)

    # img metadata
    upload_ip = db.Column(db.String(15))
    upload_time = db.Column(db.DateTime)
    image_url = db.Column(db.Text)
    height = db.Column(db.Integer) # in pixels
    width = db.Column(db.Integer) # in pixels
    format = db.Column(db.String(5))

    # face bounding box
    face_box_x = db.Column(db.Float)
    face_box_y = db.Column(db.Float)
    face_box_w = db.Column(db.Float)
    face_box_h = db.Column(db.Float)

    analysis = db.relationship('Analysis', uselist=False, back_populates='face_image')

    def __init__(self, upload_ip, image_url, format, upload_time=None, face_box_x=0.0, face_box_y=0.0, face_box_w=0.0, face_box_h=0.0):
        self.upload_ip = upload_ip
        if upload_time is None:
            upload_time = datetime.utcnow()
        self.upload_time = upload_time
        self.image_url = image_url
        self.format = format

        self.face_box_x = face_box_x
        self.face_box_y = face_box_y
        self.face_box_w = face_box_w
        self.face_box_h = face_box_h


# AI analysis
class Analysis(db.Model):
    __tablename__ = 'analysis'

    id = db.Column(db.Integer, primary_key=True)

    type = db.Column(db.String(15)) # i.e. acne, emotion, gender

    user_grade = db.Column(db.Integer) # user label

    # prediction from model
    grade_1 = db.Column(db.Float)
    grade_2 = db.Column(db.Float)
    grade_3 = db.Column(db.Float)
    grade_4 = db.Column(db.Float)

    model_id = db.Column(db.String(15))

    face_image_id = db.Column(db.Integer, db.ForeignKey('face_image.id'))

    face_image = db.relationship("Face_Image", back_populates="analysis")

    def __init__(self, type, grade_1=0.0, grade_2=0.0, grade_3=0.0, grade_4=0.0, user_grade=0.0, model_id=''):
        self.type = type

        self.user_grade = user_grade
        self.model_id = model_id

        self.grade_1 = grade_1
        self.grade_2 = grade_2
        self.grade_3 = grade_3
        self.grade_4 = grade_4

    # work in progress
