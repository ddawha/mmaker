import video_processing
import object_detection
import image_classification
import product_recommendation

def main():
    video_processing.process_video('TrainingVideos/appVideo.mp4')
    detections = object_detection.detect_objects('frame0.jpg')
    for eachObject in detections:
        predictions = image_classification.classify_objects(eachObject["name"])
        for eachPrediction in predictions:
            products = product_recommendation.recommend_products(eachPrediction["label"])
            print(products)
