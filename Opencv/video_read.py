# Read a Video Stream from Webcam
import cv2

# Capture the Webcam Object
cap = cv2.VideoCapture(0)

#Create a classifier Object using pre-trained data on faces
cascade_classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

while True:
	ret,image = cap.read()

	if ret==False:
		continue

	
	#Detect Faces in the Image
	faces = cascade_classifier.detectMultiScale(image,1.3,5)
	#print(faces)

	if(len(faces)>0):
		#Loop over each detected face and draw one rectangle
		for face in faces:
			x,y,w,h = face
			cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)

	#Display the Image
	cv2.imshow("My Video",image)

	# Quit Button
	key_pressed = (cv2.waitKey(1) & 0xFF)
	if key_pressed == ord('q'):
		break

cap.release()
cv2.destroyAllWindows() 











