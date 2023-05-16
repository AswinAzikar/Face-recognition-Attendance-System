import csv
import os
import pickle
from datetime import datetime

import firebase_admin
import numpy as np
import cv2
import face_recognition
import cvzone
from firebase_admin import db, credentials, storage

# Database credential
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://xxxx/",
    'storageBucket': "xxx"
})

bucket = storage.bucket()

cap = cv2.VideoCapture(0)  # captures the video from webcam
cap.set(3, 640)  # width
cap.set(4, 480)  # Height

imgBackground = cv2.imread("Resources/bg.png")

# Importing the mode images into a list
folderModePath = "Resources/Modes"
ModePathList = os.listdir(folderModePath)
imgModeList = []
for path in ModePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# Load the encoding file (Face Recognition)
file = open('EncodeFile.p', 'rb')
encodeListWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListWithIds
print(studentIds)

modeType = 0
counter = 0
id = -1
imgStudent = []

# Load the face cascade classifier
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    success, img = cap.read()

    # Detect faces in the current frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # This code block will resize the image captured and convert it to RGB
    imgS = cv2.resize(img, [0, 0], None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # This code block will take the above converted images and encode them to compare with the existing encoded data
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[156:156 + 480, 47:47 + 640] = img
    imgBackground[156:156 + 480, 729:729 + 320] = imgModeList[modeType]

    if len(faces) > 0:
        # This code block extracts the encoded zip and compares
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                # Known face detected
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 47 + x1, 156 + y1, x2 - x1, y2
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                id = studentIds[matchIndex]

                if counter == 0:
                    cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1

            if counter != 0:
                # Getting the data
                if counter == 1:
                    studentsInfo = db.reference(f'Students/{id}').get()
                    print(studentsInfo, id)

                    # Getting image from the storage
                    blob = bucket.blob(f'Images/{id}.png')
                    array = np.frombuffer(blob.download_as_string(), np.uint8)
                    imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)

                    # Update attendance
                    datetimeObject = datetime.strptime(studentsInfo['Last_Attendance_time'], "%Y-%m-%d %H:%M:%S")
                    secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
                    print(secondsElapsed)

                    if secondsElapsed > 3600:
                        ref = db.reference(f'Students/{id}')
                        studentsInfo['total_attendance'] += 1
                        ref.child('total_attendance').set(studentsInfo['total_attendance'])
                        ref.child('Last_Attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    else:
                        modeType = 3
                        counter = 0
                        imgBackground[156:156 + 480, 729:729 + 320] = imgModeList[modeType]

                if modeType != 3:
                    if 10 < counter < 20:
                        modeType = 2

                    imgBackground[156:156 + 480, 729:729 + 320] = imgModeList[modeType]  # small rectangle in Mode pic

                    if counter <= 10:
                        # The below code prints student data in text into the graphics
                        cv2.putText(imgBackground, str(studentsInfo['total_attendance']), (770, 325),
                                    cv2.FONT_HERSHEY_COMPLEX, .8, (0, 0, 0), 1)

                        cv2.putText(imgBackground, str(id), (840, 465),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

                        # We are not providing auto-scaling feature to the name
                        cv2.putText(imgBackground, str(studentsInfo['Name']), (840, 503),
                                    cv2.FONT_HERSHEY_COMPLEX, .4, (50, 50, 50), 1)

                        cv2.putText(imgBackground, str(studentsInfo['Major']), (840, 538),
                                    cv2.FONT_HERSHEY_COMPLEX, .4, (0, 0, 0), 1)

                        imgBackground[293:293 + 150, 830:830 + 130, :] = cv2.resize(imgStudent, (130, 150))

                    counter = counter + 1
                    if counter >= 20:
                        counter = 0
                        modeType = 0
                        studentsInfo = []
                        imgStudent = []
                        imgBackground[156:156 + 480, 729:729 + 320] = imgModeList[modeType]
    else:
        modeType = 0
        counter = 0
    cv2.imshow("Face Attendance", imgBackground)

 ##################csv######################
  # Fetch attendance data from Firebase
    ref = db.reference("Students")
    students_data = ref.get()

   # Specify
    # the output CSV file path
    output_file = "AttendanceCSV/attendance.csv"

    # Write attendance data to the CSV file
    with open(output_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Name", "Total Attendance"])  # Write header
            for student_id, student_info in students_data.items():
                 attendance = student_info.get("total_attendance", 0)
                 name = str(student_info.get("Name", ""))  # Convert to string
                 writer.writerow([student_id, name, attendance])

            # print(f"Attendance data has been downloaded and saved to '{output_file}'.")

            # # Display the image with live face detection
            # for (x, y, w, h) in faces:
            #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # cv2.imshow("Face Detection", img)

    cv2.waitKey(1)


