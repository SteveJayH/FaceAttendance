# FaceAttendance
Can automatically check group’s attendance using web-cam in real-time. Coded by python, openCV.
Project from Machine learning division, "TAVE" circle at Seoul, South Korea for studying several IT techniques.
Recognizing face is open-source. \
\
"I made making checklist(출석기록표) part by recognized face".

## How to use
/face_recognition/knowns/ --> Put each member's image. Name of image need to match to member's face. One face per one image. \
/face_recognition/camer.py --> Test camera whether works, cv2 work. \
/face_recognition/gen_face_encodings.py --> Not implemented. (Wanted to make acquiring face in the mp4 video) \
/face_recognition/real_time_attendance.py --> **Main thing** It checks the face inside the /knowns folder and check in real-time by webcam. It makes the excel(.csv) file which checks the first time visit.
/face_recognition/CheckList.xlsx --> **Output** Name and each checked time.
