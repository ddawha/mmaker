from imageai.Classification import ImageClassification

def classify_objects(image_path):
    classifier = ImageClassification()
    classifier.setModelTypeAsResNet50()
    classifier.setModelPath("resnet50_imagenet_tf.2.0.h5")  # Download the ResNet model and put it in your current directory
    classifier.loadModel()

    predictions = classifier.classifyImage(image_path, result_count=5)
    return predictions
