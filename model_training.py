from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
data_directory="C:/Users/17048/face_detector/DataSet_Main"
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory)
trainer.setTrainConfig(object_names_array=["Ye"], batch_size=6, num_experiments=349, train_from_pretrained_model="C:/Users/17048/face_detector/models/tiny-yolov3.pt")
try:
    trainer.trainModel()
except AssertionError as e:
    print("Error occurred:", e)
    print("Please check the input data.")
