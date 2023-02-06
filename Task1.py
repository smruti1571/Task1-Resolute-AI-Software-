# Need to install opencv and pytesseract
import cv2                   # Import OpenCV
import pytesseract           # Import Pytesseract

# Path for the Tessseract-OCR in system files
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract'

#Image path
# Within " " you have to specift the path for the image to be read
# For my system refernce path is "C:\Users\Smruti\OneDrive\Desktop\Task\Data\Task1\1.jpg"
imagePath=r"C:\Users\Smruti\OneDrive\Desktop\Task\Data\Task1\1.jpg"                     

# Load the image
image = cv2.imread(imagePath)

# Pre-processing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)        # Convert imgae to gray scale image
gray = cv2.medianBlur(gray, 3)                        # Blur the image

# Pass the image to Py-tesseract
text = pytesseract.image_to_string(gray)


print(text)