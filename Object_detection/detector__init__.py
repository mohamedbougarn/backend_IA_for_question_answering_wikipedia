import cv2
import numpy as np
import os
import tensorflow as tf
import time
import pyttsx3
from gtts import gTTS
import playsound
import win32com.client as wincl
from tensorflow.python.keras.utils.data_utils import get_file

np.random.seed(123)

engine = pyttsx3.init()

class Detector:
    def _init_(self):
        pass

    def readClasses(self,classesFilePath):
        with open(classesFilePath, 'r')as f:
            self.classesList = f.read().splitlines()

            #color list
            self.colorlist = np.random.uniform(low=0,high=255,size=(len(self.classesList), 3))

            print(len(self.classesList), len(self.colorlist))


    def downloadModel(self,modelURL):

        fileName = os.path.basename(modelURL)
        self.modelName = fileName[:fileName.index('.')]


        self.cacheDir = "./pretrained_models"#modified Object_detection/
        os.makedirs(self.cacheDir,exist_ok=True)

        get_file(fname=fileName,origin=modelURL, cache_dir=self.cacheDir, cache_subdir="checkpoint", extract=True)
        print(" file name in downloadmodel "+fileName)
        print(" model name in downloadeModel " +self.modelName)


    def loadModel(self):
        print('downloading model '+self.modelName)
        tf.keras.backend.clear_session()
        self.model = tf.saved_model.load(os.path.join(self.cacheDir, "checkpoint",self.modelName, "saved_model"))
        print("Model "+self.modelName + " loaded successfuly . . .!")

    def loadModeldowloading(self ,modelName,cacheDir):
        tf.keras.backend.clear_session()
        self.model = tf.saved_model.load(os.path.join(cacheDir, "checkpoint", modelName, "saved_model"))
        print("Model " + modelName + "loaded successfuly . . .!")



    def createBoundingBox(self, image,threshold=0.5,):
        inputTensor = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
        inputTensor = tf.convert_to_tensor(inputTensor, dtype=tf.uint8)
        inputTensor = inputTensor[tf.newaxis,...]

        detections = self.model(inputTensor)



        bboxes = detections['detection_boxes'][0].numpy()
        classIndexes = detections['detection_classes'][0].numpy().astype(np.int32)
        classScore = detections['detection_scores'][0].numpy()



        imH,imW,imC = image.shape

        #pour encadré suel les objet
        bboxIdx = tf.image.non_max_suppression(bboxes,classScore ,max_output_size=50,iou_threshold=threshold,score_threshold=threshold)
        print(bboxIdx)

        #
        # engine.say(" detect " + bboxIdx)
        # # os.system("say " + classLabelText)
        # engine.runAndWait()

        if len(bboxIdx)!=0:
            for i in bboxIdx:
                bbox = tuple(bboxes[i].tolist())
                classConfidence = round(100*classScore[i])
                classIndex = classIndexes[i]

                #classe text centent nom dobjet .upper pour le text soit maj
                classLabelText = self.classesList[classIndex].upper()
                classColor = self.colorlist[classIndex]



                # #test du voix
                # tts = gTTS(text=classLabelText, lang="en")
                # filename = "voice.mp3"



                displayText = '{} : {}%'.format(classLabelText,classConfidence)




                ymin,xmin,ymax,xmax = bbox

                xmin,xmax,ymin,ymax = (xmin * imW, xmax * imW, ymin * imH , ymax * imH)
                xmin, xmax, ymin, ymax = int(xmin), int(xmax), int(ymin), int(ymax)
                cv2.rectangle(image, (xmin,ymin), (xmax,ymax), color=classColor,thickness=1)

                #pour afficher le classe label et le confidenc %
                cv2.putText(image, displayText,(xmin,ymin -10),cv2.FONT_HERSHEY_PLAIN,1,classColor,2)

                # pour modifier les bordure et les coins du cadre
                lineWidth=min(int((xmax-xmin)*0.2),int((ymax-ymin)*0.2))

                #############

                cv2.line(image,(xmin,ymin), (xmin + lineWidth,ymin),classColor,thickness=5)
                cv2.line(image,(xmin,ymin), (xmin ,ymin + lineWidth),classColor,thickness=5)

                cv2.line(image,(xmax,ymin), (xmax - lineWidth,ymin),classColor,thickness=5)
                cv2.line(image,(xmax,ymin), (xmax ,ymin + lineWidth),classColor,thickness=5)

                #####################

                cv2.line(image, (xmin, ymax), (xmin + lineWidth, ymax), classColor, thickness=5)
                cv2.line(image, (xmin, ymax), (xmin, ymax - lineWidth), classColor, thickness=5)

                cv2.line(image, (xmax, ymax), (xmax - lineWidth, ymax), classColor, thickness=5)
                cv2.line(image, (xmax, ymax), (xmax, ymax - lineWidth), classColor, thickness=5)




        # #test
        # tts.save(filename)
        # playsound.playsound(filename)




        return image








    def predictImage(self,imagePath,threshold=0.5):
        image = cv2.imread(imagePath)
        bboxImage = self.createBoundingBox(image,threshold)

        cv2.imwrite(self.modelName +".jpg",bboxImage)
        cv2.imshow("result",bboxImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

#si on veut en real life il faut modifier les lignes 132==>??
    def predictVideo(self,videoPath , threshold = 0.5):
        cap = cv2.VideoCapture(videoPath)

        if(cap.isOpened()== False):
            print("Error video ")
            return
        (success,image) = cap.read()

        starttime =0

        while success:
            currentTime = time.time()
            fps = 1/(currentTime - starttime)
            starttime = currentTime
            bboxImage = self.createBoundingBox(image,threshold)

            cv2.putText(bboxImage , "FPS: " +str(int(fps)),(20,70),cv2.FONT_HERSHEY_PLAIN , 2 ,(0,255,0),2)
            cv2.imshow("RESULT ",bboxImage)



            key=cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

            (success,image)=cap.read()
        cv2.destroyAllWindows()




    #todo define : function that returns JSON with classes found in images
    def get_detections(images):
        raw_images = []
        # images = request.files.getlist("images")
        image_names = []
        for image in images:
            image_name = image.filename
            image_names.append(image_name)
            image.save(os.path.join(os.getcwd(), image_name))
            img_raw = tf.image.decode_image(
                open(image_name, 'rb').read(), channels=3)
            raw_images.append(img_raw)

        num = 0

        # create list for final response
        response = []

        for j in range(len(raw_images)):
            # create list of responses for current image
            responses = []
            raw_img = raw_images[j]
            num += 1
            img = tf.expand_dims(raw_img, 0)
            img = transform_images(img, size)

            t1 = time.time()
            boxes, scores, classes, nums = yolo(img)
            t2 = time.time()
            print('time: {}'.format(t2 - t1))

            print('detections:')
            for i in range(nums[0]):
                print('\t{}, {}, {}'.format(class_names[int(classes[0][i])],
                                            np.array(scores[0][i]),
                                            np.array(boxes[0][i])))
                responses.append({
                    "class": class_names[int(classes[0][i])],
                    "confidence": float("{0:.2f}".format(np.array(scores[0][i]) * 100))
                })
            response.append({
                "image": image_names[j],
                "detections": responses
            })
            img = cv2.cvtColor(raw_img.numpy(), cv2.COLOR_RGB2BGR)
            img = draw_outputs(img, (boxes, scores, classes, nums), class_names)
            cv2.imwrite(output_path + 'detection' + str(num) + '.jpg', img)
            print('output saved to: {}'.format(output_path + 'detection' + str(num) + '.jpg'))

        # remove temporary images
        for name in image_names:
            os.remove(name)
        try:
            return jsonify({"response": response}), 200
        except FileNotFoundError:
            abort(404)






    def createdetectionBox(self, image,threshold=0.5):
        # create list of responses for current image
        responses = []
        #
        #img = cv2.imread(image)
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #
        inputTensor = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
        inputTensor = tf.convert_to_tensor(inputTensor, dtype=tf.uint8)
        inputTensor = inputTensor[tf.newaxis,...]

        detections = self.model(inputTensor)



        bboxes = detections['detection_boxes'][0].numpy()
        classIndexes = detections['detection_classes'][0].numpy().astype(np.int32)
        classScore = detections['detection_scores'][0].numpy()



        # imH,imW,imC = image.shape

        #pour encadré seul les objet
        bboxIdx = tf.image.non_max_suppression(bboxes,classScore ,max_output_size=50,iou_threshold=threshold,score_threshold=threshold)
        print(bboxIdx)

        #
        # engine.say(" detect " + bboxIdx)
        # # os.system("say " + classLabelText)
        # engine.runAndWait()

        if len(bboxIdx) != 0:
            for i in bboxIdx:
                bbox = tuple(bboxes[i].tolist())
                classConfidence =  float("{0:.2f}".format(100*classScore[i]))
                classIndex = classIndexes[i]

                #classe text centent nom dobjet .upper pour le text soit maj
                classLabelText = self.classesList[classIndex].upper()
                classColor = self.colorlist[classIndex]

                responses.append({
                    "class": classLabelText,
                    "confidence": classConfidence
                })



                # #test du voix
                # tts = gTTS(text=classLabelText, lang="en")
                # filename = "voice.mp3"



                displayText = '{} : {}%'.format(classLabelText,classConfidence)

        print (responses)
        return responses

