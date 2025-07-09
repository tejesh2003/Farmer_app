from app.database import db

class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.Float, nullable=False)
    village = db.Column(db.String(100), nullable=False)
    crop = db.Column(db.String(100), nullable=False)
    sowing_date = db.Column(db.Date, nullable=False)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)
    schedules = db.relationship('Schedule', backref='farm', lazy=True)
