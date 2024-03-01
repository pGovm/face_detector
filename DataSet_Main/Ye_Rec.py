from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
data_directory="C:/Users/17048/OneDrive/Documents/CL/Python Programs/Object_Recognition/DataSet_Main"
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory)
trainer.setTrainConfig(object_names_array=["Ye"], batch_size=4, num_experiments=349, train_from_pretrained_model="C:/Users/17048/OneDrive/Documents/CL/Python Programs/Object_Recognition/DataSet_Main/models/tiny-yolov3.pt")
trainer.trainModel()