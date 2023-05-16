import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials

from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-be5e1-default-rtdb.firebaseio.com"
    , 'storageBucket': "faceattendancerealtime-be5e1.appspot.com"
})

# Importing the student images
folderPath = "Images"
PathList = os.listdir(folderPath)  # this function will list all the files in the 'folderParth'
# print(PathList)
imgList = []
studentIds = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    # print(path)

    studentIds.append(
        os.path.splitext(path)[0])  # append function will add the studentIds from the name of the studentImage files
    # splitext splits the '1234.jpg' to'1234' and '.jpg'

    fileName = f'{folderPath}/{path}'
    # This line of code creates a file path by joining the folderPath and
    # path variables using the os.path.join() function.
    # It creates a string that represents
    # the full file path of the image file.
    bucket = storage.bucket()
    # This line of code creates an instance of the Firebase storage bucket.
    blob = bucket.blob(fileName)
    # This line of code creates a blob object within the Firebase storage bucket,
    # with the name of the file being the same as the fileName variable.
    blob.upload_from_filename(fileName)
    # This line of code uploads the image file to the Firebase storage bucket.
    # It reads the contents of the image file specified by fileName and
    # sends it to the Firebase storage bucket to be stored as a blob.


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


encodeListKnown = findEncodings(imgList)
encodingListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Successful!")

# The below code just save the encoded details of the images and store it in a file
file = open('EncodeFile.p', 'wb')
pickle.dump(encodingListKnownWithIds, file)
file.close()
print("File saved!")
# we need to import this file for face recognition
