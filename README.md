
# Text Detection & Layout Analysis powered on Streamlit

A Streamlit application that performs Text Detection and Layout Analysis for image/pdf documents. This project has been divided into 2 sub tasks. One is Text Detection and the other is Layout Analysis.

## Installation
Before installing ensure Microsoft visual studio  is up to date, else use the link to install:
https://aka.ms/vs/17/release/vc_redist.x64.exe

Also check for and install :
Microsoft C++ Build Tools - Visual Studio

![App Screenshot](https://i.ibb.co/hsp9kMh/c.png)

Install all the required library files from requirements.txt

Step 1: Install Detectron2LayoutModel
```bash
git clone https://github.com/facebookresearch/detectron2.git
python -m pip install -e detectron2
```
Step 2: Download and install pytesseract using the link https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v4.0.0.20181030.exe

Step 3: Add the path of tesseract.exe file in the environment.




    


![App Screenshot](https://i.ibb.co/NLTTrvr/path.png)


Step 4: Install poppler-utils using the link https://blog.alivate.com.au/wp-content/uploads/2018/10/poppler-0.68.0_x86.7z

Step 5: Add poppler to the environment path same as tesseract


![App Screenshot](https://i.ibb.co/ZLYv1Rq/path-poppler.png)

Step 6: Download config.yml file and provide the address in the 29th and 42nd line of the app.py file. Download Link: https://www.dropbox.com/s/u9wbsfwz4y0ziki/config.yml?dl=1

Step 7: Open config.yaml file
Scroll down to WEIGHTS: https://www.dropbox.com/s/h7th27jfv19rxiy/model_final.pth?dl=1 (It will be present around 265th line)
![App Screenshot](https://i.ibb.co/kKhGx4j/config.png)

Copy that link and paste it in your browser, a 'model_final.pth' will be downloaded. 

Now replace the path to WEIGHTS: your_desired_folder/model_final.pth
![App Screenshot](https://i.ibb.co/276dW83/config1.png)

Once, the installation is completed, we are ready to launch the Streamlit application. Open app.py in any of the editors and in the terminal run following code: 
```bash
streamlit run app.py
```
Your streamlit application will be opened in your default web browser.

![App Screenshot](https://i.ibb.co/xqsLFwM/Capture.png)





## Functions and what they do
Three functions are used here:

text_detection: detect text areas and visualize with a bounding box.

parserIMG: Layout Analysis for image documents.

parserPDF: Layout Analysis for pdf documents.
## text_detection
The input image is converted into a numpy array. The image is then passed on to the function image_to_data from pytesseract module. This locates the text position so that we shall draw the bounding boxes. For each word, the point of origin/ position has been returned in the form of list. The elements at the 6th, 7th, 8th, 9th indices denotes x-coordinate, y-coordinate, width, height of the word respectively. A bounding box is drawn at those regions.

## parserIMG
This function is to perform layout analysis for image data. Detectron2Layout model is used which uses R-CNN to detect and classfiy layout objects. The results from the layout analysis is visualized using bounding box, along with text annotation that shows the element type. The image after performing layout analysis is displayed.
## parserPDF
The document which is in the form of pdf when fed as input, it is converted into a list of images using pdf2image module. The images are converted into numpy array. Each image is passed on to the Detectron2Layout model, where each page is treated as a single image document and bounding box is drawn for the same to visualize the layout elements. Each page of the pdf is displayed after performing layout analysis.
