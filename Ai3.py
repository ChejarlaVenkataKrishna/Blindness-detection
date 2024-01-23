import cv2
import numpy as np


def detect_eye_disease(image_path):
    # Load the image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply image processing techniques (this is a simple example)
    # You might need more sophisticated methods for specific diseases
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Assess the presence of abnormalities in the image (example)
    abnormality_detected = len(contours) > 0

    if abnormality_detected:
        print("Abnormality detected. Consult an eye care professional.")
    else:
        print("No abnormality detected. Continue regular eye check-ups.")

    # Display the image with detected contours (for illustration purposes)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    cv2.imshow('Detected Abnormality', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Replace 'path/to/your/image.jpg' with the path to the image you want to analyze
image_path = 'My photo.jpg'
detect_eye_disease(image_path)
