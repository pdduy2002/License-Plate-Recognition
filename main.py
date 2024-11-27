import streamlit as st
import cv2
import numpy as np
from PIL import Image

def main():
    st.title("License Plate Recognition")

    # Create two columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Upload")
        # Upload video
        uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"]

        if uploaded_file is not None:
            # Display image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)

    with col2:
        st.subheader("Danh sách biển số xe đọc ra được")
        if uploaded_file is not None:
            # Process the image (placeholder for actual processing)
            license_plate_text = process_image(image)

            # Display recognized license plate text
            st.write(license_plate_text)
        else:
            st.write("Vui lòng tải lên ảnh để nhận diện biển số.")

def process_image(image):
    # Placeholder function for image processing
    return "ABC1234"

if __name__ == "__main__":
    main()
