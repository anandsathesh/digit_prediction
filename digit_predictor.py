import cv2
import numpy as np
import tensorflow as tf
import socket

# Load the trained model
model = tf.keras.models.load_model("mnist_model.h5")

# Setup drawing canvas
canvas = np.zeros((280, 280), dtype=np.uint8)
drawing = False

# Drawing callback
def draw(event, x, y, flags, param):
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.circle(canvas, (x, y), 10, (255), -1)  # Thicker brush
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.namedWindow("Draw a Digit")
cv2.setMouseCallback("Draw a Digit", draw)

while True:
    cv2.imshow("Draw a Digit", canvas)
    key = cv2.waitKey(1)

    if key == 27:  # ESC key to exit
        break

    elif key == ord('c'):  # Clear canvas
        canvas[:] = 0

    elif key == ord('p'):  # Predict digit
        coords = cv2.findNonZero(canvas)
        if coords is not None:
            x, y, w, h = cv2.boundingRect(coords)
            roi = canvas[y:y+h, x:x+w]

            # Preprocessing
            roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
            roi = cv2.GaussianBlur(roi, (5, 5), 0)
            _, roi = cv2.threshold(roi, 100, 255, cv2.THRESH_BINARY)
            roi = cv2.bitwise_not(roi)
            roi = roi / 255.0
            roi = roi.reshape(1, 28, 28, 1)

            # Prediction
            prediction = model.predict(roi)
            predicted_digit = int(np.argmax(prediction))
            confidence = float(np.max(prediction))

            print(f"Predicted Digit: {predicted_digit} (Confidence: {confidence:.2f})")

            # Send to Raspberry Pi
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(("192.168.10.16", 9999))  # <<< Replace this
                s.sendall(str(predicted_digit).encode())
                s.close()
            except Exception as e:
                print("Failed to send to Pi:", e)
        else:
            print("Please draw a digit before predicting.")

cv2.destroyAllWindows()
