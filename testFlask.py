#!C:\Users\LAPTOP\AppData\Local\Programs\Python\Python38\python.exe
print("Content-Type: text/html\n")
print("python")


from flask import Flask, jsonify,request
import PIL.Image as Image
import io
import base64
import cv2
import face_recognition
import numpy as np
import os

app = Flask(__name__)

@app.route('/',methods=['POST'])
def hello_world():
    data = request.json
    print(data['image1'])
    print(data['image2'])

    byte_data1=str(data['image1'])
    new_byte_data1 = byte_data1.replace(" ", "+")
    b1 = base64.b64decode(new_byte_data1)
    pil_img1 = Image.open(io.BytesIO(b1))

    rgb_image1 = pil_img1.convert('RGB')
    rgb_image1.save("new_image1.jpg", quality=95)

    byte_data2 = str(data['image2'])
    new_byte_data2 = byte_data2.replace(" ", "+")
    b2 = base64.b64decode(new_byte_data2)
    pil_img2 = Image.open(io.BytesIO(b2))

    rgb_image2 = pil_img2.convert('RGB')
    rgb_image2.save("new_image2.jpg", quality=95)




    image1 = face_recognition.load_image_file("new_image1.jpg")
    face_encoding1 = face_recognition.face_encodings(image1)[0]

    image2 = face_recognition.load_image_file("new_image2.jpg")
    face_encoding2 = face_recognition.face_encodings(image2)[0]

    result = face_recognition.compare_faces([face_encoding1], face_encoding2)
    print("Result: ", result[0])

    os.remove("new_image1.jpg")
    os.remove("new_image2.jpg")

    return jsonify({'result':str(result[0])})
    return "hi from xaamp"


if __name__ == '__main__':
    app.run()
print("hi")
