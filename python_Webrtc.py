import cv2
import base64
import requests
# Open the video stream
cap = cv2.VideoCapture(0)

# Set up the server connection
server_url = "http://localhost:8080/update_image"

# Capture and send frames from the video stream
while True:
    # Capture a frame from the video stream
    ret, frame = cap.read()

    # Check if the video has ended
    if not ret:
        break

    # Encode the frame in JPEG format
    ret, jpeg = cv2.imencode('.jpg', frame)

    # Encode the JPEG data in base64
    jpeg_b64 = base64.b64encode(jpeg).decode("utf-8")
    print(jpeg_b64)
    # Send the frame to the server
    requests.post(server_url, json={"image": jpeg_b64})
