import streamlit as st
import cv2
import numpy as np
from PIL import Image

def main():
    st.title("License Plate Recognition from Video")

    # Create two columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Upload Video")
        # Upload video
        uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

        if uploaded_file is not None:
            st.video(uploaded_file, format="video/mp4")

    with col2:
        st.subheader("Danh sách biển số xe đọc ra được")
        if uploaded_file is not None:
            # Process the video (placeholder for actual processing)
            license_plate_texts = process_video(uploaded_file)

            # Display recognized license plate text
            st.write("Biển số nhận diện được:")
            for plate in license_plate_texts:
                st.write(plate)
        else:
            st.write("Vui lòng tải lên video để nhận diện biển số.")

def process_video(video_file):
    # Load video using OpenCV
    cap = cv2.VideoCapture(video_file)
    license_plate_texts = []
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert frame to PIL Image for consistency
        frame_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
        # Placeholder function to process each frame
        plate_text = process_frame(frame_image)
        if plate_text and plate_text not in license_plate_texts:
            license_plate_texts.append(plate_text)
    
    cap.release()
    return license_plate_texts

def process_frame(frame):
    # Placeholder function for frame processing
    # Replace with actual license plate recognition logic
    return "ABC1234"  # Simulate recognizing a plate

if __name__ == "__main__":
    main()
