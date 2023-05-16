import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-be5e1-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {

    "3673": {
        "Name": "AARDRA S",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3887": {
        "Name": "ABHIJITH KRISHNA AK",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3798": {
        "Name": "ABHIJITH R",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3657": {
        "Name": "ABHINAV J",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3799": {
        "Name": "ABHIRAM S KUMAR",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3686": {
        "Name": "AISWARYA NAIR",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3621": {
        "Name": "AJOY K",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3938": {
        "Name": "AKASH P",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3635": {
        "Name": "AKASH A R",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3811": {
        "Name": "AKASH S",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3694": {
        "Name": "AKHIL MOHAN",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3800": {
        "Name": "AKSHAY VINOD",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3640": {
        "Name": "ALLEN R MATHEW",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3674": {
        "Name": "AMAL S",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3998": {
        "Name": "AMAL. S",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3942": {
        "Name": "AMINA N",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3649": {
        "Name": "AMISH SUBRAMANIAN",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3627": {
        "Name": "AMRITHA. A",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3623": {
        "Name": "ANAKHA G",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3804": {
        "Name": "ANANDHU R",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3933": {
        "Name": "ANCHANA G",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3696": {
        "Name": "ANJU M",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3671": {
        "Name": "ARAVIND A",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3633": {
        "Name": "ASHWIN CHANDRAN",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3682": {
        "Name": "ASHWIN MANMATHAN S",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3651": {
        "Name": "AZAD A S",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3680": {
        "Name": "DANIS T DAS",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3669": {
        "Name": "HARIPRIYA R",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3658": {
        "Name": "HARISANKAR",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3641": {
        "Name": "HARSHVARDHAN V",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3618": {
        "Name": "JESTIN JOY",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3647": {
        "Name": "JINO MATHEW THANKACHEF",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3724": {
        "Name": "JITHIN THANKACHAN",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3777": {
        "Name": "JOBY MATHEW",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3624": {
        "Name": "JOLSNA SABU",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3616": {
        "Name": "KEVIN K JOHN",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3969": {
        "Name": "MILKA JAMES",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3656": {
        "Name": "PRANAV PRASAD",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3652": {
        "Name": "PRANAV A",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3637": {
        "Name": "RAJASREE NAIR S",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3810": {
        "Name": "ROOPA R",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3631": {
        "Name": "SAJITHA J",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3626": {
        "Name": "SIMON K MATHEW",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3840": {
        "Name": "SYAMRAJ R",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3619": {
        "Name": "VAISHNAV MURALI",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3634": {
        "Name": "VISHNU J PILLAI",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3636": {
        "Name": "VISHNU RAVI",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    },
    "3620": {
        "Name": "VISWAJITH V",
        "Major": "BCA",
        "Starting_year": 2021,
        "Standing": "G",
        "Year": 2,
        "Last_Attendance_time": "2023-04-12 00:08:50"
    }
}

for key, value in data.items():
    ref.child(key).set(value)
