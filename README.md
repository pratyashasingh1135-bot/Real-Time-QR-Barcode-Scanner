 Real-Time QR & Barcode Scanner using OpenCV + Pyzbar
📌 Project Overview

This project is a Real-Time QR and Barcode Scanner built using Python, OpenCV, and Pyzbar.
It uses the system camera to continuously scan frames and detect barcodes or QR codes.
When detected, the data is displayed on the screen and also saved to a text file.

🚀 Features

Real-time camera scanning

Supports both QR Codes and Barcodes

Draws a green outline around detected codes

Displays decoded text on the video feed

Automatically saves scanned data in my_scanned_data.txt

Press Q to exit the scanner

📦 Requirements

Install the following Python libraries before running the script:

pip install opencv-python
pip install pyzbar
pip install numpy

🔧 Additional Setup (Windows Only)

Install the ZBar dependency:

pip install pyzbar


If any issue occurs, install ZBar manually:

Download from: https://github.com/mchehab/zbar

🧠 How It Works

Opens the webcam using OpenCV

Reads each frame in real-time

Uses pyzbar.decode() to search for barcodes/QRs

Draws polygon outlines around detected codes

Extracts text and displays it on screen

Saves scanned data into a text file

📜 Code
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, 640)   # Set width
cap.set(4, 480)   # Set height

print("Scanner Started... Opening camera.")

while True:
    success, img = cap.read()   # Read frame from camera
    if not success:
        print("Camera failed to read the frame!")
        break
    
    # --- BARCODE / QR CODE SCANNING ---
    for barcode in decode(img):

        myData = barcode.data.decode('utf-8')   # Extract scanned data
        print(f"Detected: {myData}")

        # --- DRAW THE OUTLINE BOX AROUND BARCODE ---
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (0, 255, 0), 5)

        # --- DISPLAY THE SCANNED TEXT ON THE SCREEN ---
        x, y, w, h = barcode.rect
        cv2.putText(img, myData, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (255, 0, 0),
                    2)

        # --- OPTIONAL: SAVE THE SCANNED DATA TO A TEXT FILE ---
        with open('my_scanned_data.txt', 'a') as f:
            f.write(f"{myData}\n")

    # Show live camera feed with scanning
    cv2.imshow('Real-Time Scanner', img)

    # Press 'q' to exit the scanner
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close all windows
cap.release()
cv2.destroyAllWindows()

▶️ How to Run

Save the script as scanner.py

Run the script:

python scanner.py


Point your camera toward a QR code or Barcode

Press Q to quit

📁 Output File

All scanned data is stored in:

my_scanned_data.txt


Each scan is saved on a new line.

💡 Future Improvements

Add sound notification (beep)

Prevent duplicate scans

GUI button controls

Save scanned data with timestamps

Build an EXE file
