# Location class
class Directory:

    def __init__(self, name, x, y, distance_to=None):
        """
        Stores City objects. Upon initiation, automatically appends itself to list_of_cities
        self.x: x-coord
        self.y: y-coord
        self.graph_x: x-coord for graphic representation
        self.graph_y: y-coord for graphic representation
        self.name: human readable name.
        """
        self.name = name
        self.x = float(x)
        self.y = float(y)
        self.distance_to = {self.name: 0.0}
        if distance_to:
            self.distance_to = distance_to

