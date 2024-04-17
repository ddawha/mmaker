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
        video_processing.process_video(video_path)

        image_directory = 'TrainingVideos/GenImages/'
        image_files = [f for f in os.listdir(image_directory) if f.endswith('.jpg')]
        for image_file in image_files:
            print(f"Image file: {image_file.title}")
            image_path = os.path.join(image_directory, image_file)
            detections = object_detection.detect_objects(image_path)
            for _ in detections:
                predictions = image_classification.classify_objects(image_path=image_path)
                for each_prediction in predictions:
                    products = product_recommendation.recommend_products(each_prediction)
                    try:
                        print(products[0]['title'], " : ", products[0]['url'])
                        print('\n')
                    except Exception as e:
                        logging.error(f"Prediction error encountered: {e}")
                        print(f"Prediction error encountered: {e}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()