from Object_detection.detector__init__ import Detector

modelURL='http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz'
#il ya des modele plus efficace que ssd mobilenet v2

classFile = 'coco.names'
imagePath = "4.jpg"
#videoPath = "data/video.mp4" # si en test real time avec webcam juste on remplace par 0
videoPath = 0 # si en test real time avec webcam juste on remplace par 0
threshould=0.5

detector = Detector()
detector.readClasses(classFile)
detector.downloadModel(modelURL)
detector.loadModel()

detector.createdetectionBox(imagePath,threshould)
