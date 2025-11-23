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
