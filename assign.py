import csv
from database import db
from classes import Qualification, UserQualification


class AssignWorkers:
    name = None
    questions = []

    required_qualification_ids = []
    required_qualifications = {}

    selected_users = []

    def __init__(self, tasks):
        self.name = input("What is the name of your dataset? ")

        # Read the dataset file
        with open(tasks, 'r') as file:
            file = csv.reader(file)
            next(file, None)  # Skip the header
            for i, line in enumerate(file):
                self.questions.append(line[0])

        print("Found {} questions in your tasks file".format(len(self.questions)))

        # For every qualification, let the requester decide if is required and on what level
        print("Are one of the following qualifications required to work on your dataset? (answer with y or n)")
        qualifications = db.query(Qualification).all()
        for qualification in qualifications:
            answer = input("{}: ".format(qualification.name))
            if answer.lower() in ['y', 'yes']:
                level = int(input("On what level? [100, 200, 300] "))
                self.required_qualification_ids.append(qualification.id)
                self.required_qualifications[str(qualification.id)] = {'level': level, 'name': qualification.name}

        # Give an overview of select qualifications
        print("The following qualifications are selected for your dataset:")
        for qualification in self.required_qualifications:
            print(self.required_qualifications[qualification]['name'])

        # Select users that have the selected qualifications
        user_qualifications = db.query(UserQualification).all()
        for user_qualification in user_qualifications:
            if user_qualification.qualification_id in self.required_qualification_ids:
                if user_qualification.user not in self.selected_users:
                    self.selected_users.append(user_qualification.user)

        # Give an overview of the selected users that can work on the dataset
        print("The following workers were selected based on the qualifications")
        for selected_user in self.selected_users:
            print("[{}] {}".format(selected_user.id, selected_user.name))
