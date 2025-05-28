from ultralytics import YOLO  # type: ignore
from hezar.models import Model
import cv2
import numpy as np
import re

# Initialize YOLO and OCR models once
lp_detector = YOLO(r'C:\Users\ihc\Desktop\Plate_FullStack\Plate_FullStack\Plate_Backend\Plate_Detector\lp_detector.pt')
lp_ocr = Model.load("hezarai/crnn-fa-64x256-license-plate-recognition")

def process_image(django_image_file):
    # Read image from InMemoryUploadedFile (Django)
    file_bytes = np.asarray(bytearray(django_image_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    if img is None:
        return None

    detection = lp_detector(img)[0]
    if detection.boxes.data.numel() > 0:
        try:
            plate = detection.boxes.data.tolist()[0]
            x1, y1, x2, y2, score, class_id = plate
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            plate_cropped = img[y1:y2, x1:x2]
            plate_text = lp_ocr.predict(plate_cropped)
            if isinstance(plate_text, list):
                plate_text = ''.join([output.text for output in plate_text])
            print(f"OCR Detected plate text: {plate_text}")

            # Try all common Iranian plate formats
            patterns = [
                r'(\d{2})\s*([آ-ی])\s*(\d{3})\s*ایران\s*(\d{2})',   # With "ایران"
                r'(\d{2})\s*([آ-ی])\s*(\d{3})\s*-\s*(\d{2})',        # With dash
                r'(\d{2})\s*([آ-ی])\s*(\d{3})(\d{2})',               # All together
            ]
            for pattern in patterns:
                match = re.search(pattern, plate_text)
                if match:
                    part1, persian_char, part2, city_code = match.groups()
                    formatted_plate = f"{part1} {persian_char} {part2} - {city_code}"
                    print(f"Formatted plate: {formatted_plate}")
                    return formatted_plate

            print(f"Returned raw OCR: {plate_text}")
            return plate_text
        except Exception as e:
            print(f"Error processing image: {e}")
            return None
    else:
        return None
    