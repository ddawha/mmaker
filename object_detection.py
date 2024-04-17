from imageai.Detection import ObjectDetection
import os

init_weights=True

def detect_objects(image_path):
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath("retinanet_resnet50_fpn_coco-eeacb38b.pth")  # Download the YOLO model and put it in your current directory
    detector.loadModel()

    # Get the base name of the input image (e.g., "input.jpg")
    base_name = os.path.basename(image_path)

    # Remove the extension of the base name (e.g., "input")
    base_name_without_ext = os.path.splitext(base_name)[0]

    # Construct the output image path
    output_image_path = os.path.join("TrainingVideos/OutImages/", base_name_without_ext + "_detected.jpg")

    detections = detector.detectObjectsFromImage(input_image=image_path, output_image_path=output_image_path)    
    print(detections)
    return detections
