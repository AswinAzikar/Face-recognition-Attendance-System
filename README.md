# Face Attendance Realtime(Live Face Detection)
Face Attendance Realtime is a project that utilizes face recognition technology to automate the attendance process. It provides a real-time and efficient solution for recording attendance using a webcam and a database.

## Features
   1. Real-time face detection and recognition using OpenCV and face_recognition libraries.
   2.  Integration with Firebase Realtime Database for storing student information and attendance data.
   3.  Utilizes Firebase Storage for storing student images.
   4.  Graphical user interface for displaying student information and attendance status.
   5.  Automatic updating of attendance records based on time elapsed since the last attendance.

## Installation
   1. Clone the repository:
   
      `git clone https://github.com/your-username/face-attendance-realtime.git`
   
  
  2. Install the required dependencies:
   
     `pip install -r requirements.txt`
  3.  Set up Firebase credentials:
        Obtain a service account key file from Firebase and save it as serviceAccountKey.json in the project root     directory.
  4. Update the database URL:
        Replace `http://xxxxxxx`in the initialize_app function with your Firebase Realtime Database URL in the main.py file and AddToDatabase.py.

## Usage

  5. Capture and Encode Student Images:
        Prepare a folder of student images in the Images directory. Each image should be named with the student's unique identifier.
        Run the encode_images.py script to encode the student images and generate the EncodeFile.p file.

  6. Run the Attendance System:
        Run the main.py script to start the attendance system.
        Ensure that your webcam is connected and functioning properly.
        The system will detect faces in the webcam feed and compare them with the known student encodings to recognize and record attendance.

  7.  View Attendance Data:
        The attendance data is automatically updated in the Firebase Realtime Database.
        You can access the attendance data through the Firebase console or retrieve it programmatically using the Firebase API.
 
 
## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## Acknowledgments

  * The project utilizes the following libraries: OpenCV, face_recognition, cvzone, and firebase_admin.
  
  * Special thanks to the contributors and maintainers of the above libraries for their valuable work.
  
## References
* OpenCV Documentation: https://docs.opencv.org/
* face_recognition Documentation: https://github.com/ageitgey/face_recognition

Feel free to customize the README file according to your specific project details, instructions, and acknowledgments.

