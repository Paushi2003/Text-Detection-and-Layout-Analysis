import streamlit as st
import pytesseract
import cv2
import pdf2image
import numpy as np
import layoutparser as lp
from PIL import Image


def text_detection(img):
  res = Image.open(img)
  res = np.array(res)
  overlay = Image.open(img)
  overlay = np.array(overlay)
  with st.spinner('Processing Text Detection'):
    boxes = pytesseract.image_to_data(res)
    for i,b in enumerate(boxes.splitlines()): 
      if i!=0:
        b = b.split()
        if len(b)==12:
          x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
          cv2.rectangle(overlay,(x-5,y-5),(w+x+5,h+y+5),(185,237,221),-1) 
          #res = cv2.putText(res,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(185,237,221),2)
  new = cv2.addWeighted(overlay, 0.4, res, 1 - 0.4, 0)
  st.subheader("Text Detection")
  st.image(new)

def parserIMG(path):
  res = Image.open(path)
  with st.spinner('Processing Layout Analysis'):
    model = lp.Detectron2LayoutModel('lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config',
                                  extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.5],
                                  label_map={0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"})
    layout_result = model.detect(res)
    res=lp.draw_box(res, layout_result,  box_width=5, box_alpha=0.2, show_element_type=True)
  st.subheader("Layout Analysis")
  st.image(res)

def parserPDF(path):
  img = np.asarray(pdf2image.convert_from_bytes(path.read()))
  st.subheader("Layout Analysis")

  with st.spinner('Processing Layout Analysis'):
    model = lp.Detectron2LayoutModel('lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config',
                                  extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.5],
                                  label_map={0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"})
    for i in img:
      layout_result = model.detect(i)
      i=lp.draw_box(i, layout_result,  box_width=5, box_alpha=0.2, show_element_type=True)
      st.image(i)

#title 
st.title('Text Detection & Layout Analysis')
#uploading file
file = st.file_uploader(label='Upload your document here',type=['png','jpg','jpeg','pdf'])
button = st.button('Confirm')
if button and file is not None:
    if file.type=="image/png" or file.type=="image/jpg" or file.type=="image/jpeg":
      parserIMG(file)
      text_detection(file)
    elif file.type == "application/pdf":
      parserPDF(file)

