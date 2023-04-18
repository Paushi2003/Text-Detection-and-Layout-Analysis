
# Text Detection & Layout Analysis powered on Streamlit

A Streamlit application that performs Text Detection and Layout Analysis for image/pdf documents. 
This project has been divided into 2 sub tasks. One is Text Detection and the other is Layout Analysis.
  
  Modules required for image files: tesseract-ocr, pytesseract, cv2, numpy, PIL.
  
  Modules required for pdf files: pdf2image, poppler-utils (dependency library for pdf2image), numpy.

  UI has been created using Streamlit.

  Install all the required libraries.

Firstly, import all the required library files. 


## Installation

Install the required packages

```bash
!sudo apt install tesseract-ocr poppler-utils 
!pip install pytesseract streamlit layoutparser pdf2image
!pip install 'git+https://github.com/facebookresearch/detectron2.git@v0.4#egg=detectron2'
```
You can run the consecutive cells in the notebook once these packages are installed.

To launch the streamlit application, run the below code:
```bash
!streamlit run app.py & npx localtunnel --port 8501 
```
You can specify your app name by replacing 'app.py' as 'app_name.py'. 

    
## Landing Page

![App Screenshot](https://i.ibb.co/hFHFsNH/textdetect-layoutanalysis-UI.png)


## Functions and what they do
Three functions are used here:

  text_detection: detect text areas and visualize with a bounding box.

  parserIMG: Layout Analysis for image documents.

  parserPDF: Layout Analysis for pdf documents.

  
## text_detection
The input image is converted into a numpy array. The image is then passed on to the function image_to_data from pytesseract module. This locates the text position so that we shall draw the bounding boxes. For each word, the point 
of origin/ position has been returned in the form of list. The elements at the 6th, 7th, 8th, 9th indices denotes x-coordinate, y-coordinate, width, height of the word respectively. A bounding box is drawn at those regions.
## parserIMG
This function is to perform layout analysis for image data. Detectron2Layout model is used which uses R-CNN to detect and classfiy layout objects. The results from the layout analysis is visualized using bounding box, along with
text annotation that shows the element type. The image after performing layout analysis is displayed.

## parserPDF
The document which is in the form of pdf when fed as input, it is converted into a list of images using pdf2image module. The images are converted into numpy array. Each image is passed on to the Detectron2Layout model, where each page is treated as a single image document and bounding box is drawn for the same to visualize the layout elements. Each page of the pdf is displayed after performing layout analysis.  