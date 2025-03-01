import os
import cv2
import supervision as sv
from ultralytics import YOLO
from ultralytics import YOLO

# Set up the environment
HOME = os.path.expanduser(".")
EXAMPLE_IMAGES_DIR = os.path.join(HOME, "image_detection_examples")
IMAGE_PATH = f"{HOME}/image_detection_examples/dog-1.jpeg"

if __name__ == "__main__":
    print("Image detection environment set up.")
    image = cv2.imread(IMAGE_PATH)
    
    # Add padding to the image
    padding = 100
    image_with_padding = cv2.copyMakeBorder(
        image,
        top=padding,
        bottom=padding,
        left=padding,
        right=padding,
        borderType=cv2.BORDER_CONSTANT,
        value=[255, 255, 255]
    )

    model = YOLO("yolov8s.pt")
    result = model(image_with_padding, verbose=False)[0]
    annotated_image = image_with_padding.copy()

    detections = sv.Detections.from_ultralytics(result)
    print(len(detections))
    print(detections)
    
    box_annotator = sv.BoxAnnotator()
    label_annotator = sv.LabelAnnotator(
        text_scale=1.5,
        text_thickness=1,
        text_padding=5
    )

    annotated_image = image.copy()
    annotated_image = box_annotator.annotate(annotated_image, detections=detections)
    annotated_image = label_annotator.annotate(annotated_image, detections=detections)

    # action: render the image
    # sv.plot_image(image=annotated_image, size=(8, 8))
    
    # action: save the image to file
    cv2.imwrite("annotated_image.jpg", annotated_image)
    print("Annotated image saved successfully.")
