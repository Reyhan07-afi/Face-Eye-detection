
import cv2

# 1. Open webcam
cap = cv2.VideoCapture(0)

# 2. Load Haar Cascade models
face_cascade = cv2.CascadeClassifier(
    "models/haarcascade_frontalface_default.xml"
)

eye_cascade = cv2.CascadeClassifier(
    "models/haarcascade_eye.xml"
)

while True:

    # 3. Capture frame
    ret, frame = cap.read()

    if not ret:
        print("Cannot access webcam")
        break

    # 4. Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 5. Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    # 6. Process each detected face
    for (x, y, w, h) in faces:

        # Draw blue rectangle around face
        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (255, 0, 0),
            3
        )

        # 7. Extract face ROI
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # 8. Detect eyes
        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.3,
            minNeighbors=5
        )

        # 9. Draw green rectangles around eyes
        for (ex, ey, ew, eh) in eyes:

            cv2.rectangle(
                roi_color,
                (ex, ey),
                (ex+ew, ey+eh),
                (0, 255, 0),
                3
            )

    # 10. Display output
    cv2.imshow("Face and Eye Detection", frame)

    # 11. Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 12. Release resources
cap.release()
cv2.destroyAllWindows()
