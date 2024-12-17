import streamlit as st
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO
from utils import *
from paddleocr import PaddleOCR, draw_ocr
import time

def main():
    if "det_model" not in st.session_state:
        print("=========Initializing yolo========")
        st.session_state.det_model = YOLO("model/yolov8_weight.pt")
    
    if "ocr_model" not in st.session_state:
        print("=========Initializing ocr========")
        st.session_state.ocr_model = PaddleOCR(use_angle_cls=True, lang="en")

    if "plates" not in st.session_state:
        st.session_state.plates = []
    
    if "current_file_name" not in st.session_state:
        st.session_state.current_file_name = ""

    if "prev_file_name" not in st.session_state:
        st.session_state.prev_file_name = ""

    st.title("License Plate Recognition")

    # Create two columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Upload Video")
        # Upload video
        uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

        if uploaded_file:
            if uploaded_file.name != st.session_state.current_file_name:
                st.session_state.plates = []

            st.session_state.current_file_name = uploaded_file.name
            count = 0
            st.video(uploaded_file, format="video/mp4")

            vid_file = "data/uploaded_data/upload." + uploaded_file.name.split('.')[-1]
            with open(vid_file, 'wb') as out:
                out.write(uploaded_file.read())

            cap = cv2.VideoCapture(vid_file)
            start = time.time()
            while True:
                ret, frame = cap.read()

                if not ret:
                    cap.release()
                    break

                if count % 15 == 0: 
                    st.session_state.plates += get_plate(st.session_state["det_model"], st.session_state["ocr_model"], frame)

                count += 1
            
    with col2:
        st.subheader("Danh sách biển số xe đọc ra được")
        if st.session_state.plates != []:
            # Display recognized license plate text
            st.session_state.plates.sort()
            for p in set(st.session_state.plates):
                st.write(p)
        else:
            st.write("Vui lòng tải lên ảnh để nhận diện biển số.")

if __name__ == "__main__":
    main()
