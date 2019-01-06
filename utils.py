import random

import names

from database import db
from classes import User, Qualification, UserQualification


def create_users(amount=10):
    print("Creating {} users".format(amount))
    for i in range(0, amount):
        db.add(User(
            name=names.get_full_name()
        ))

    db.commit()


def create_qualifications():
    print("Creating sample qualifications")
    db.add(Qualification(
        name='Speaks english'
    ))
    db.add(Qualification(
        name='Speaks dutch'
    ))
    db.add(Qualification(
        name='Has university degree'
    ))
    db.add(Qualification(
        name='Has driving license'
    ))

    db.commit()


def assign_qualifications(amount=10):
    print("Assigning qualifications randomly")
    users = db.query(User).all()
    qualifications = db.query(Qualification).all()

    for i in range(0, amount):
        user = random.choice(users)
        qualification = random.choice(qualifications)
        level = random.choice([100, 200, 300])

        db.add(UserQualification(
            user_id=user.id,
            qualification_id=qualification.id,
            level=level
        ))

    db.commit()
