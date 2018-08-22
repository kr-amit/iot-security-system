

print('imoprting modules')
import face_recognition
import cv2




import urllib.request as u



import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class Gmail(object):
    def __init__(self, email, password,to):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        self.to=to
        session = smtplib.SMTP(self.server, self.port)        
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, subject, body, to):
        headers = ["From: " + self.email,"Subject: " + subject,"To: " + to,"",""]
        headers = "\r\n".join(headers)
        self.session.sendmail(self.email,to,headers + "\r\n\r\n" + body)

    def SendMail(self,ImgFileName,sub,new,e):
        img_data = open(ImgFileName, 'rb').read()
        msg = MIMEMultipart()
        msg['Subject'] = sub
        msg['From'] = self.email
        msg['To'] = e

        text = MIMEText(new)
        msg.attach(text)
        image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
        msg.attach(image)
        self.session.sendmail(self.email, e, msg.as_string())

e = 'yashagar0412@gmail.com'
eid='homesafetyiot@gmail.com'
password='7539518426'







def click():
    ret,frame1 = video_capture.read() 
    cv2.imwrite('c1.png',frame1)
    u.urlopen('http://192.168.43.88/intruder')
    try:
        gm = Gmail(eid,password,e)
    except Exception:
        print("Login failed, check internet connection or provided credentials")



    print("Login Successful")
    sub = "Intruder Detected"
    new = "An intruder maybe detected at your doorstep "+"http://192.168.43.88"
    img="c1.png"
    gm.SendMail(img,sub,new,e)
    
    




def signal():
    u.urlopen('http://192.168.43.88/ledOFF')



amit_image = face_recognition.load_image_file("amit.jpg")
amit_face_encoding = face_recognition.face_encodings(amit_image)[0]
b_image = face_recognition.load_image_file("b.jpg")
b_face_encoding = face_recognition.face_encodings(b_image)[0]
k_image = face_recognition.load_image_file("joint.jpg")
k_face_encoding = face_recognition.face_encodings(k_image)[0]




face_locations = []
face_encodings = []
face_names = []
process_this_frame = True




amit_detect_count=0
b_detect_count=0
joint_detect_count=0
unknown_detect_count=0




video_capture = cv2.VideoCapture(0)



while True:
    ret, frame = video_capture.read()

    
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    
    if process_this_frame:
    
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        try:
            for face_encoding in face_encodings:
                match = face_recognition.compare_faces([amit_face_encoding,b_face_encoding,k_face_encoding],face_encoding)
                if match[0]:
                    name="amit"
                    amit_detect_count+=1
                    print('amit :' + amit_detect_count)
                    if amit_detect_count>5:
                        signal()
                elif match[1]:
                    name="bankit"
                    b_detect_count+1
                    print("b :{}".format(b_detect_count))
                    if b_detect_count>5:
                        signal()#u.urlopenn('http://192.168.43.88/ledOFF')
                elif match[2]:
                    name="joint"
                    joint_detect_count+=1
                    if joint_detect_count>5:
                        signal()#u.urlopenn('http://192.168.43.88/ledOFF')
                else:
                    name="unknown"
                    if unknown_detect_count>5:
                        click()
                face_names.append(name)
            
        except:
            print('unexpected error!!')
        
    process_this_frame = not process_this_frame
    
    for (top, right, amitottom, left), name in zip(face_locations, face_names):
        # Scale  up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        amitottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, amitottom), (0, 0, 255), 2)

        # Draw a labell with a name amitelow the face
        cv2.rectangle(frame, (left, amitottom - 35), (right, amitottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, amitottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)
    
    key= cv2.waitKey(10)
    if key==27:
        break

    # Hit 'q' on the keyamitoard to quit!
    #if cv2.waitKey(1) & 0xFF == ord('q'):
     #   break

# Release handle to the weamitcam
video_capture.release()
cv2.destroyAllWindows()
    
    



