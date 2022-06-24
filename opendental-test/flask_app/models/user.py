from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
  db = 'demo'
  def __init__(self,data):
    print(f"############################################################# {data}")
    self.patient_number = data['PatNum']
    self.first_name = data['FName']
    self.last_name = data['LName']
    self.gender = data['Gender']
    self.adress = data['Adress']
    # self.created_at = data['created_at']
    # self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
    # this query is only returning one iteration of patient
    query = "SELECT * FROM patient;"
    print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    result = connectToMySQL(cls.db).query_db(query)
    emails = []
    for row in result:
      emails.append(cls(row))
    return result
  
  @classmethod
  def get_one(cls):
    print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    query = "SELECT * FROM patient WHERE PatNum = 7;"
    results = connectToMySQL(cls.db).query_db(query)
    return cls(results[0])

  # this method is for getting the user's id that has been put into session[]
  @classmethod
  def get_by_id(cls,data):
    query = "SELECT * FROM patients WHERE PatNum = %(patient_number)s;"
    results = connectToMySQL(cls.db).query_db(query,data)
    return cls(results[0])