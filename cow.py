
class Cow:
    def __init__(self, name):
        # initializes a cow object with name and image to be None
        self.name = name
        self.image = None

    def get_name(self):
        # returns the name of the cow
        return self.name

    def get_image(self):
        # returns the image used to display the cow
        return self.image

    def set_image(self, image):
        # sets image used to display the cow
        self.image = image
