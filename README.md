# digit_prediction
🔢 Raspberry Pi Controlled by Handwritten Digit Recognition (MNIST + OpenCV)

This project allows you to control an LED connected to a Raspberry Pi using handwritten digit recognition via a deep learning model trained on the MNIST dataset.
You draw a digit (0–9) on your laptop, the model predicts it, and sends it over Wi-Fi to the Raspberry Pi, which performs an action — like turning on an LED!


---

🧠 Technologies Used

Python

TensorFlow / Keras (MNIST model)

OpenCV (for drawing interface)

Socket programming (TCP)

Raspberry Pi GPIO control



---

📦 Project Structure

digit_control_project/
├── digit_predictor.py      # Runs on your laptop (digit drawing + prediction + send to Pi)
├── mnist_model.h5          # Trained digit recognition model
├── digit_receiver.py       # Runs on Raspberry Pi (receives digit, controls LED)
└── README.md               # This file


---

🖥 How it Works

1. User draws a digit (0–9) using the mouse on the laptop.


2. A CNN model trained on the MNIST dataset predicts the digit.


3. The digit is sent over TCP to the Raspberry Pi using sockets.


4. The Raspberry Pi receives the digit and turns ON an LED for 2 seconds.




---

🛠 Requirements

Laptop Side

Python 3

TensorFlow

OpenCV (pip install opencv-python)

Trained MNIST model (mnist_model.h5)


Raspberry Pi Side

Raspberry Pi 4 (or any Pi)

Python 3

RPi.GPIO

1x LED

330Ω resistor

Breadboard + jumper wires



---

⚙ Setup Instructions

1. Train & Save the Model (Laptop)

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255
x_test  = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255
y_train = to_categorical(y_train)
y_test  = to_categorical(y_test)

model = Sequential([
    Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D(pool_size=(2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))
model.save("mnist_model.h5")


---

2. Run on Laptop

python digit_predictor.py

Draw a digit with your mouse.

Press p to predict and send.

Press c to clear.

Press Esc to exit.


🧠 Don't forget to replace "YOUR_PI_IP_HERE" in the code with your actual Pi IP.


---

3. Raspberry Pi Wiring

Component	GPIO Pin

LED +	GPIO 18
LED −	GND



---

4. Run on Raspberry Pi

python3 digit_receiver.py

Waits for incoming digit

Turns on the LED for 2 seconds when a digit is received



---

🚀 Future Ideas

Use digits to control different devices (e.g., 0 → LED, 1 → Fan, 2 → Servo)

Add web dashboard for status

Extend to voice or image commands

Replace socket with MQTT for cloud-based control



---

📸 Demo

> Include a GIF or image showing you drawing the digit and the Pi lighting up the LED.




---

🧑‍💻 Author

[Anand S]



---

