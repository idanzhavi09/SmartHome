import cv2

# Load the Haar cascade files for detecting faces and full-body humans
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Create a VideoCapture object to read from the webcam
cap = cv2.VideoCapture(0)

# Create a window to display the webcam footage
cv2.namedWindow('Webcam Footage')

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    # Convert the frame to grayscale for faster processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame using the Haar cascade
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        #Start Automation            
    # Detect full-body humans in the frame using the Haar cascade
    bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    # Draw rectangles around the detected bodies
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
        # Print a message indicating that a full-body human has been detected
        print("Full-body human detected!")
    
    # Display the frame with the detected faces and bodies in a separate window
    cv2.imshow('Object Detection', frame)
    
    # Display the webcam footage in a separate window
    cv2.imshow('Webcam Footage', frame)
    
    # Press 'q' to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
