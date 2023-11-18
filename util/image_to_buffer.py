def image_to_buffer(image):
    binary_data = None
    try:
        with open(image, 'rb') as file:
            binary_data = file.read()
        return binary_data
    except Exception as e:
        print(f"Error: {e}")