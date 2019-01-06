import argparse
from database import init_db
from utils import create_users, create_qualifications, assign_qualifications
from assign import AssignWorkers

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--init', help='Initialize the database and create tables', type=bool)
parser.add_argument('-a', '--add_dataset', help='Add a dataset to the database', type=str)

if __name__ == '__main__':
    args = parser.parse_args()

    if args.init:
        # Initialize DB, create tables
        init_db()

        # Fill DB with sample data
        create_users()
        create_qualifications()
        assign_qualifications()
    elif args.add_dataset:
        AssignWorkers(args.add_dataset)
