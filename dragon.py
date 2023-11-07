
class Dragon:
    def __init__(self, name, image):
        # constructor
        # creates a new dragon object with given name and image
        self.name = name
        self.image = image

    def get_name(self):
        # returns the name of the dragon
        return self.name

    def get_image(self):
        # returns the image used to display the dragon
        return self.image

    def can_breathe_fire(self):
        # should exist in every Dragon class
        # for default dragon should return True
        return True
