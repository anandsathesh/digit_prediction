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

> Output images are in the op file





---

🧑‍💻 Author

[Anand S]



---

