from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
data_directory="/workspace/objsmallpp/DataSet_Main"
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory)
trainer.setTrainConfig(object_names_array=["Ye"], batch_size=4, num_experiments=349, train_from_pretrained_model="/workspace/objsmallpp/DataSet_Main/models/tiny-yolov3.pt")
try:
    trainer.trainModel()
except ValueError as e:
    print("Error occurred:", e)
    print("Please check the input data.")
