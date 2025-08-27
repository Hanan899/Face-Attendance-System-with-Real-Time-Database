import cv2 as cv
import face_recognition
import pickle
import os

studentFacesPaths = os.listdir('Images')

studentFacesList = []
studentIDs =[]

for path in studentFacesPaths:
    studentFacesList.append(cv.imread(os.path.join('Images', path)))
    studentIDs.append(os.path.splitext(path)[0])


def doEncoding(images):
    encodeList = []
    for img in images:
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    
    return encodeList



print("Encoding ... please wait ... ")
encodedImages = doEncoding(studentFacesList)
encodedImagesWithIDs = [encodedImages, studentIDs]
print("Encoding complete")

file = open('EncodedImages.p', 'wb')
pickle.dump(encodedImagesWithIDs, file)
file.close()

print("File saved")
