from pymongo import MongoClient
from MerakiWeb.config.database import db

collection = db['vacancies']

class Vacancy:
    def __init__(self, title, description, location):
        self.title = title
        self.description = description
        self.location = location

    def save(self):
        vacancy_data = {
            'title': self.title,
            'description': self.description,
            'location': self.location
        }
        collection.insert_one(vacancy_data)

    @staticmethod
    def find_all():
        return collection.find()

    @staticmethod
    def find_by_location(location):
        return collection.find({'location': location})

    @staticmethod
    def find_by_title(title):
        return collection.find({'title': title})