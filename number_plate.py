import cv2
import pytesseract
import datetime
import csv
import threading

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640) # width
cap.set(4, 480) # height

min_area = 500
count = 0

# Create CSV file and write headers
with open('number_plates_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Detected Text", "Date and Time", "Location", "Image File"])

default_location = "Road No. 7, Banjara Hills, 500002ber_"

def append_to_csv():
    while True:
        if count > 0:
            with open('number_plates_data.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["", "", "", f"scanned_img_{count-1}.jpg"])

threading.Thread(target=append_to_csv).start()

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
            
            # Get location information
            location = default_location
            print("Location:", location)
            
            # Save image and text to CSV file
            with open('number_plates_data.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([text, current_time, location, f"scanned_img_{count}.jpg"])

            cv2.imwrite(f"plates/scanned_img_{count}.jpg", img_roi)
            count += 1

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
