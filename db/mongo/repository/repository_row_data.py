from db.mongo.config import row_data


def insert_email(email):
    row_data.insert_one(email)