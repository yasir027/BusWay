


# 🚍 BusWay: Real-Time Bus Number Plate Detection & Tracking System

**BusWay** is a smart transit tracking system that detects bus number plates from live CCTV footage using computer vision and OCR. It extracts real-time information including the **bus number**, **timestamp**, and **location**, and stores this data—along with a snapshot—for potential real-time broadcast to users waiting at subsequent bus stops.

### 📌 Project Idea

In many cities, commuters miss buses by a margin of minutes. BusWay solves this problem by utilizing CCTV cameras and OCR to detect buses as they pass a checkpoint, instantly extracting key info that can be used to:
- Alert passengers in advance that a specific bus is nearing.
- Track bus movement through checkpoints.
- Log transit history and image-based records.


## 🚀 Features

- 🔍 **Live Number Plate Detection** using OpenCV.
- 🧠 **Optical Character Recognition** using Tesseract to read bus numbers.
- 🕒 **Timestamping**: Capture date & time of detection.
- 🌍 **Location Tagging** (static, can be extended to GPS-based).
- 🖼️ **Snapshot Capture** of detected number plates.
- 📁 **CSV Logging**: Save all extracted data and images for historical reference.
- 🧪 Includes supporting notebook (`ocr notebook`) and test scripts (`testing.py`).

---

## 📂 Repository Structure

```

.
├── modal/                      # Folder with detection models (e.g., Haar cascade XML)
├── plate/                      # Folder where captured plate images are saved
├── ocr notebook/               # Jupyter notebook with OCR experiments
├── number\_plate.py            # Main Python script for live detection
├── testing.py                 # Optional test script
├── index.html                 # Frontend mockup (optional)
├── number\_plates\_data.csv     # Logs detected plates, timestamps, and image references
├── number\_plates\_data.ods     # ODS spreadsheet version of the data
├── testing.csv                # Sample test CSV
├── requirements.txt           # Python dependencies
├── LICENSE                    # License info
└── README.md                  # You’re reading it!

````

---

## 🛠️ Technologies Used

- **Python 3.x**
- **OpenCV** – for image processing and video stream handling
- **Tesseract OCR** – for extracting text from images
- **Haar Cascade Classifier** – for detecting license plates
- **Threading** – for parallel CSV handling (future use)

---

## 🔧 How It Works

1. **Live Feed** from webcam/CCTV is captured via OpenCV.
2. **Haar Cascade** model detects vehicle number plates in each frame.
3. Detected plate area is extracted and passed to **Tesseract OCR**.
4. OCR reads the **bus number**, and the system logs:
    - 🕒 **Date & Time**
    - 🌍 **Location** (static, can be extended)
    - 📷 **Image of Plate**
5. All data is saved to a structured **CSV** file for recordkeeping or API broadcasting.

---

## ✅ Sample Output (number_plates_data.csv)

| Detected Text | Date and Time       | Location                       | Image File           |
|---------------|---------------------|--------------------------------|-----------------------|
| TS09UB4567    | 2025-06-02 12:34:56 | Road No. 7, Banjara Hills...   | scanned_img_0.jpg     |
| TS10UB8912    | 2025-06-02 12:35:42 | Road No. 7, Banjara Hills...   | scanned_img_1.jpg     |

---

## 🖥️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/BusWay.git
cd BusWay
````

### 2. Install Dependencies

Make sure Python 3.x is installed. Then:

```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR Engine

* [Windows Download](https://github.com/tesseract-ocr/tesseract)
* After installation, make sure to update the Tesseract path in `number_plate.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
```

### 4. Run the Detection Script

```bash
python number_plate.py
```

Press `q` to quit the detection window.

---

## 🧪 Testing

* `ocr notebook`: Experiments and validation of Tesseract OCR performance.
* `testing.py`: Additional test functions for image and OCR handling.
* `testing.csv`: Sample data for trial runs.

---

## 📈 Future Enhancements

* 📡 **Real-time broadcast to users** via WebSocket or Firebase.
* 📍 **Dynamic GPS-based location** integration.
* 🤖 **YOLO or Deep Learning**-based detection for better accuracy.
* 📲 **Mobile app** to receive alerts when a bus is approaching.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Contributing

Pull requests are welcome! If you want to contribute:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/fooBar`).
3. Commit your changes.
4. Push to the branch.
5. Open a Pull Request.

---

## 📬 Contact

**Developer:** \[Your Name]
**Email:** [your.email@example.com](yasirhussain0027@gmail.com)
**LinkedIn:** [linkedin.com/in/your-profile](https://linkedin.com/yasirhussain027)

---

## 📣 Final Note

**BusWay** isn’t just a project—it's a vision for **smarter urban mobility**. By combining computer vision with real-time analytics, this system has the potential to modernize how cities track and communicate public transport movements.

```

