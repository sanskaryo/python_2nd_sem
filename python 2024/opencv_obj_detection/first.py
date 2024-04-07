import cv2
import dlib
from scipy.spatial import distance

# Function to calculate the Euclidean distance between two points
def euclidean_dist(pt1, pt2):
    return distance.euclidean(pt1, pt2)

# Function to calculate the eye aspect ratio (EAR)
def eye_aspect_ratio(eye):
    # Compute the Euclidean distances between the two sets of vertical eye landmarks (x, y)-coordinates
    A = euclidean_dist(eye[1], eye[5])
    B = euclidean_dist(eye[2], eye[4])

    # Compute the Euclidean distance between the horizontal eye landmark (x, y)-coordinates
    C = euclidean_dist(eye[0], eye[3])

    # Compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    return ear

# Constants
EAR_THRESHOLD = 0.25  # Eye aspect ratio to indicate blink
CONSECUTIVE_FRAMES = 20  # Number of consecutive frames for which the EAR must be below the threshold to trigger an alarm

# Load face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Load alarm sound (you may need to install the playsound library)
# pip install playsound
from playsound import playsound

# Start webcam
cap = cv2.VideoCapture(0)

# Initialize variables
frame_counter = 0
alarm_on = False

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray, 0)

    for face in faces:
        landmarks = predictor(gray, face)
        left_eye = []
        right_eye = []

        for n in range(36, 42):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            left_eye.append((x, y))

        for n in range(42, 48):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            right_eye.append((x, y))

        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)

        ear = (left_ear + right_ear) / 2.0

        if ear < EAR_THRESHOLD:
            frame_counter += 1
            if frame_counter >= CONSECUTIVE_FRAMES:
                if not alarm_on:
                    alarm_on = True
                    playsound("alarm_sound.mp3")
                    print("Wake up!")
        else:
            frame_counter = 0
            alarm_on = False

        cv2.putText(frame, "EAR: {:.2f}".format(ear), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
