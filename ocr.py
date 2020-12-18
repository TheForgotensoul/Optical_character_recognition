import cv2
from pathlib import Path
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"tesseract/tesseract.exe"
img = Path(input("Enter the location of the file > "))
img = cv2.imread(f"{img}")
img = cv2.resize(img, (800, 600))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cong = r'--oem 3 --psm 6'
bounds = pytesseract.image_to_data(img, config=cong)
text = pytesseract.image_to_string(img, config=cong)

for x, bound in enumerate(bounds.splitlines()):

    if x != 0:
        box = bound.split()
        if len(box) == 12:
            x, y, w, h, = int(box[6]), int(box[7]), int(box[8]), int(box[9])
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 1)
            cv2.putText(img, box[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 255, 0), 1)

with open("ocr.txt", "w+") as f:
    f.write(text)

cv2.imshow("img", img)
cv2.waitKey(0)
