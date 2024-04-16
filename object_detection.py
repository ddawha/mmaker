from imageai.Detection import ObjectDetection

def detect_objects(image_path):
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("yolo.h5")  # Download the YOLO model and put it in your current directory
    detector.loadModel()

    detections = detector.detectObjectsFromImage(input_image=image_path, output_image_path="detected.jpg")
    return detections
