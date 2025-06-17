import socket
import RPi.GPIO as GPIO
import time

# GPIO setup
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Server setup
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Listening on port {PORT}...")

try:
    conn, addr = server.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024).decode().strip()
        if not data:
            break

        print(f"Received digit: {data}")
        try:
            digit = int(data)
        except ValueError:
            print("Invalid input, not a digit.")
            continue

        if 0 <= digit <= 9:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("LED ON")
            time.sleep(2)
            GPIO.output(LED_PIN, GPIO.LOW)
            print("LED OFF")
        else:
            print("Digit out of range (0–9)")

except Exception as e:
    print(f"Error: {e}")
finally:
    conn.close()
    server.close()
    GPIO.cleanup()
