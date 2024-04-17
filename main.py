import os
import logging
import video_processing
import object_detection
import image_classification
import product_recommendation

# Configure logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def main():
    try:
        video_path = 'TrainingVideos/appVideo.mp4'
        print(f"Current directory: {os.getcwd()}")
        print(f"Absolute path to video file: {os.path.abspath(video_path)}")
        video_processing.process_video(video_path)

        image_directory = 'TrainingVideos/GenImages/'
        print(f"Current directory: {os.getcwd()}")
        print(f"Image directory: {os.path.abspath(image_directory)}")
        image_files = [f for f in os.listdir(image_directory) if f.endswith('.jpg')]
        for image_file in image_files:
            print(f"Image file: {image_file.title}")
            image_path = os.path.join(image_directory, image_file)
            detections = object_detection.detect_objects(image_path)
            for each_object in detections:
                predictions = image_classification.classify_objects(image_path=image_path)
                for each_prediction in predictions:
                    products = product_recommendation.recommend_products(each_prediction)
                    print(products)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()