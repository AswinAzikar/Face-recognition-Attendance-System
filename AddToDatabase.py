import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json") #mentioning service account key from firebase
firebase_admin.initialize_app(cred, {
    'databaseURL': "http://xxxxxxx"   # mention the database url 
})

ref = db.reference('Students')

data = {

    "3673": {
        "Name": " bill gates",
        "Major": "CS ",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },

## Add more data here using above template ##

}
