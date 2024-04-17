from imageai.Classification import ImageClassification
import os

prediction = ImageClassification()
def classify_objects(image_path):
    classifier = ImageClassification()
    classifier.setModelTypeAsResNet50()
    classifier.setModelPath("resnet50-19c8e357.pth")  # Download the ResNet model and put it in your current directory
    classifier.loadModel()

    predictions, probabilities = classifier.classifyImage(image_path, result_count=5)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)
    return predictions, probabilities