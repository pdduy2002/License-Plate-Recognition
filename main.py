import streamlit as st
import cv2
import numpy as np

def main():
    st.title("License Plate Recognition")

    # Create two columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Upload")
        # Upload video
        uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

        if uploaded_file is not None:
            # Display video
            st.video(uploaded_file)

    with col2:
        st.subheader("Danh sách biển số xe đọc ra được")
        if uploaded_file is not None:
            # Process the video (placeholder for actual processing)
            license_plate_text = process_video(uploaded_file)

            # Display recognized license plate text
            st.write(license_plate_text)
        else:
            st.write("Vui lòng tải lên video để nhận diện biển số.")

def process_video(uploaded_file):
    # Placeholder function for video processing
    return "ABC1234\nDEF5678\nGHI9012"

if __name__ == "__main__":
    main()