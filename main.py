import easyocr
import cv2


file_path_udastak = "images/udastak.png"
file_path_prava = "images/prava.png"
def textRecognition(file_path):
    reader = easyocr.Reader(["en"], gpu = True , verbose = False)
    image = cv2.imread(file_path)
    result = reader.readtext(image, detail= 0)
    return result

def udastakBirthdayRecognition():
    for info in textRecognition(file_path_udastak):
        if "." in info:
            return info

def pravaBirthdayRecognition():
    for info in textRecognition(file_path_prava):
        if "3." in info:
            info = info[3:13]#тут [3:13] и 3. потому что считывает вот так: <<3.18.03.2005.г.Астана>>
            return info

def udastakIinRecognition():
    for info in textRecognition(file_path_udastak):
        if info.isdigit() and len(info) == 12:
            return info

def pravaIinRecognition():
    for info in textRecognition(file_path_prava):
        if len(info) == 25:
            iin = ""
            for char in info:
                if char.isdigit():
                    iin += char
            iin = iin[1:] #тут с правами чуть чуть по другому потому что там сканируется вся строка: тоесть <<4) ИИН 051803...>> вот так
            return iin

def compareIIN():
    if udastakIinRecognition() == pravaIinRecognition():
        return True
    else:
        return False

def compareBirthday():
    if udastakBirthdayRecognition() == pravaBirthdayRecognition():
        return True
    else:
        return False

def checkApprove():
    if compareBirthday() and compareIIN():
        return True
    else:
        return False

def main():
    print(pravaIinRecognition())
    print(udastakIinRecognition())
    print(pravaBirthdayRecognition())
    print(udastakBirthdayRecognition())
    print(compareIIN())
    print(compareBirthday())
    print(checkApprove())

if __name__ == "__main__":
    main()
