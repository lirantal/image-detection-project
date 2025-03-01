import os

def get_file_path(filename):
    """Returns the full path for a given filename in the project directory."""
    return os.path.join(os.path.dirname(__file__), filename)

def load_image(image_path):
    """Loads an image from the specified path."""
    # Implementation for loading an image goes here
    pass

def save_image(image, save_path):
    """Saves the given image to the specified path."""
    # Implementation for saving an image goes here
    pass