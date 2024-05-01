import easyocr
import cv2

def textRecognition(file_path, coordinates):
    reader = easyocr.Reader(["ru"], gpu = False)
    image = cv2.imread(file_path)
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[2]
    cropped_image = image[y1:y2, x1:x2]
    result = reader.readtext(cropped_image, detail= 0)
    return result

def main():
    file_path = "img.png"
    coordinates = ([[115, 503], [321, 503], [321, 539], [115, 539]])
    print(textRecognition(file_path=file_path, coordinates=coordinates))

if __name__ == "__main__":
    main()
