from app.models.schedule import Schedule

def save_schedule(schedule):
    from app.database import db
    db.session.add(schedule)
    db.session.commit()
    return schedule

def get_all_schedules():
    return Schedule.query.all()
