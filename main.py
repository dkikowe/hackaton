import easyocr
import cv2


file_path = "img_3.png"
def textRecognition(file_path):
    reader = easyocr.Reader(["ru"], gpu = True , verbose = False)
    image = cv2.imread(file_path)
    result = reader.readtext(image, detail= 0)
    return result

def birthdayRecognition():
    for info in textRecognition(file_path):
        if "." in info:
            return info

def iinRecognition():
    for info in textRecognition(file_path):
        if info.isdigit() and len(info) == 12:
            return info

def main():
    print(iinRecognition(), birthdayRecognition())

if __name__ == "__main__":
    main()
