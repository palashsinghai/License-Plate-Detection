
# LICENSE PLATE DETECTION

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGTOyA49vzagt7Ad3lCgzz8NCQONbuTWFsZg&usqp=CAU" align="Right">

This is object detection model which takes an image/frame captured from a camera and detects the number plate from that image/frame.
This model is widely used in detecting the identity of a person who was passed by a partiuclar area.

## Prerequisites
 **Python Packages Used :**

 - [opencv-python](https://pypi.org/project/opencv-python/)
OpenCV is a huge open-source library for computer vision, machine learning, and image processing. OpenCV supports a wide variety of programming languages like Python, C++, Java, etc. It can process images and videos to identify objects, faces, or even the handwriting of a human.
 
 - [Pytesseract](https://pypi.org/project/pytesseract/)
 Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images.

Python-tesseract is a wrapper for Google’s Tesseract-OCR Engine. It is also useful as a stand-alone invocation script to tesseract, as it can read all image types supported by the Pillow and Leptonica imaging libraries, including jpeg, png, gif, bmp, tiff, and others. Additionally, if used as a script, Python-tesseract will print the recognized text instead of writing it to a file.

 **Software Packs Needed :**
 - [Tesseract Engine](https://github.com/tesseract-ocr/tesseract)
 
## How To Use

Install all the dependencies and change the path of the tsseract engine installed on your computer.
There are two file for image detection and video detection.

You can also use an external camera for video detection, all you have to do is give the path of that camera in code.

  
## Working

- **Step 1 :**
<img src="https://github.com/palashsinghai/screenshots/tree/main/license_plate_detection_model_screenshots/ss.png" width=375 height=200>
<img src="https://github.com/palashsinghai/screenshots/blob/main/public_photography_contest_website_ss/main_page.png" width=375 height=200>
Firstly the video will get captured by the model and only a frame from that video will be passed in the model.

- **Step 2 :**
Then before detecting the number plate model will pass the image from a number of filters like Bilateral, Grayscale.

- **Step 3 :**
Afterthat it will apply another filter which will find the contours from the image and find a closed contour which will our number plate.

- **Step 4 :**
After cropping out the number plate we will detect the numbers from that.

