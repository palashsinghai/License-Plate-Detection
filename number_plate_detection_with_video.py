import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

x = 0
y = 0
h = 0
w = 0

#function for removing noise from the cropped image of number plate to make it more accurate
def crop_image(crop):

    crop = cv2.cvtColor(crop,cv2.COLOR_BGR2GRAY)
    crop = cv2.bilateralFilter(crop,11,11,11)
    return crop

def detect_numplate(image):#function to detect number plate by removing noise and making contour of image
    # Resize the image - change width to 500
    image = cv2.resize(image, (600,500))

    # RGB to Gray scale conversion
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Noise removal with iterative bilateral filter(removes noise while preserving edges)
    gray = cv2.bilateralFilter(gray, 11, 30, 30)

    # Find Edges of the grayscale image
    edged = cv2.Canny(gray, 170, 200)

    # Find contours based on Edges
    cnts,new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Create copy of original image to draw all contours
    img1 = image.copy()
    cv2.drawContours(img1, cnts, -1, (0,255,0), 5)

    #sort contours based on their area keeping minimum required area as '30' (anything smaller than this will not be considered)
    cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:40]
    NumberPlateCnt = None #we currently have no Number plate contour

    # Top 40 Contours
    img2 = image.copy()
    cv2.drawContours(img2, cnts, -1, (0,255,0), 3)

    for c in cnts:
            global approx
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            # Select the contour with 4 corners
            if len(approx) == 4:
                NumberPlateCnt = approx #This is our approx Number Plate Contour

                # Crop those contours and store it in Cropped Images folder
                global x,y,w,h
                x, y, w, h = cv2.boundingRect(c) #This will find out co-ord for plate


                break


    # Drawing the selected contour on the original image
    cv2.drawContours(image, NumberPlateCnt, -1, (0,255,0), 3)

    Cropped = image[y:y+h,x:x+w]

    return image,Cropped,approx


video = cv2.VideoCapture(0)
a = 1

while True:
    a = a+1
    check,frame = video.read()

    img,crop,ap =detect_numplate(frame)
    cv2.imshow("image",img)
    if len(ap) == 4:
        crop = crop_image(crop)
        # using pytesseract to detect number plate, fro more accuracy Machine Learning model can be used
        text = pytesseract.image_to_string(crop)
        # checking len of number plate text to remove unecessary text
        if len(text) >=12:
            print("Number is :", text)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
