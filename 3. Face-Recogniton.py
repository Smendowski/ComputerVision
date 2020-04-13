import numpy as np
import cv2
import pickle


face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')


recognizer.read("trainner.yml")

labels = {}
with open("labels.pickle", 'rb') as f:
	loaded_labels = pickle.load(f)
	# INVERSION OF KEYS AND VALUES
	labels = {v:k for k,v in loaded_labels.items()}


cap = cv2.VideoCapture(0)


while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
	for(x,y,w,h) in faces:
		#print(x,y,w,h)
		# Defining region of interests
		# Axis X - starts from x to w
		# Axis Y - starts from y to h
		# Coordinates and thier range
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]

		end_cord_x = x + w
		end_cord_y = y + h

		id_, confidence = recognizer.predict(roi_gray)
		if confidence>=80:
			print(id_)
			print(labels[id_])
			font = cv2.FONT_HERSHEY_SIMPLEX
			name = labels[id_]
			font_color = (255, 255, 255)
			font_border_bold = 2
			cv2.putText(frame, name, (x,y), font, 1, font_color, font_border_bold, 
				cv2.LINE_AA)



		img_item = "image.png"
		cv2.imwrite(img_item, roi_gray)

		# Draw Rectangle on the face's roi
		face_border_color = (255, 0, 0) # BGR 
		face_border_bold = 2
		cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y),
			face_border_color, face_border_bold)

		# Draw Rectangle to mark eyes
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for(ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0),2)


	cv2.imshow('frame', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
cap.destroyAllWindows()	