import csv
import datetime
import os
import cv2
import pytesseract
from flask import Flask, jsonify, render_template

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640) # width
cap.set(4, 480) # height

min_area = 500
count = 0

# Create CSV file and write headers
csv_file = 'testing.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Detected Text", "Date and Time", "Image Path"])

app = Flask(__name__)

# Load data from CSV file
data = []
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# Define API endpoint to return data in JSON format
@app.route('/api/data')
def get_data():
    return jsonify(data)

# Serve custom HTML page
@app.route('/')
def index():
    return render_template('index.html')

while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x,y,w,h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y+h, x:x+w]
            cv2.imshow("ROI", img_roi)

            # OCR
            config = r'--oem 3 --psm 6'
            text = pytesseract.image_to_string(img_roi, config=config)
            now = datetime.datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            print("Detected Text:", text)
            print("Current Time:", current_time)

            # Save image and text to CSV file
            image_path = f"plates/scaned_img_{count}.jpg"
            cv2.imwrite(image_path, img_roi)
            with open(csv_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([text, current_time, image_path])
            count += 1

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

if __name__ == '__main__':
    app.run(debug=True)
