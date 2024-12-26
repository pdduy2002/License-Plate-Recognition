import numpy as np
import time
import cv2

def get_plate(det_model, ocr_model, image):
    # Placeholder function for image processing
    results = det_model.predict(image, conf=0.25, iou=0.5)

    cropped_imgs = crop_objects(results)

    if cropped_imgs == []:
        return []
    
    res = []
    for img in cropped_imgs:
        crp_img = np.array(img)
        ocr_res = ocr_model.ocr(crp_img, cls=True)
        if ocr_res[0] is not None:
            extracted_plate = "".join(comp[-1][0] for comp in ocr_res[0])
            extracted_plate = "".join(filter(lambda x: x.isalpha() or x.isdigit(), extracted_plate))
            if 6 <= len(extracted_plate) <= 10 and extracted_plate.isupper() and extracted_plate not in res:
                res.append(extracted_plate) 
        
    print("===================", res)
        # cv2.imshow("test", img)
        # cv2.waitKey(0)

    return res

def crop_objects(results):
    crops = []
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Get box coordinates
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Crop the image
            crop = r.orig_img[y1:y2, x1:x2]
            crops.append(crop)
    return crops