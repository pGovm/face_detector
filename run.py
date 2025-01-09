from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("C:/Users/17048/face_detector/models/yolov3_DataSet_Main_mAP-0.33419_epoch-108.pt")
detector.setJsonPath("C:/Users/17048/face_detector/json/DataSet_Main_yolov3_detection_config.json")
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image="C:/Users/17048/OneDrive/Documents/CL/Python Programs/face_detector/Test_ye.jpg", output_image_path="C:/Users/17048/OneDrive/Documents/CL/Python Programs/face_detector/Ye_Res")
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])