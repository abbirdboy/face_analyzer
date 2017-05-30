from .app import app, db
from datetime import datetime

# each uploaded image
class Face_Image(db.Model):
    __tablename__ = face_images

    id = db.Column(db.Integer, primary_key=True)
    upload_ip = db.Column(db.String(15))
    upload_time = db.Column(db.DateTime)
    image_url = db.Column(db.Text)
    analyses = db.relationship('')

    def __init__(self, upload_ip, upload_time=None, image_url):
        self.upload_ip = upload_ip
        if upload_time is None:
            upload_time = datetime.utcnow()
        self.upload_time = upload_time
        self.image_url = image_url

# completed analysis
class Analysis(db.Model):
    pass

    # work in progress
