def detect_objects(image_path):
    """
    Detect objects in the given image using the supervision library.

    Args:
        image_path (str): The path to the image file.

    Returns:
        list: A list of detected objects with their bounding boxes.
    """
    # Import necessary libraries
    from supervision import ObjectDetector

    # Initialize the object detector
    detector = ObjectDetector()

    # Load the image
    image = detector.load_image(image_path)

    # Perform detection
    detections = detector.detect(image)

    return detections


def process_image(image_path):
    """
    Process the image for detection.

    Args:
        image_path (str): The path to the image file.

    Returns:
        None
    """
    detections = detect_objects(image_path)
    # Further processing can be done here, such as displaying results or saving output
    print(f"Detections for {image_path}: {detections}")