class BBox:
    def __init__(self, box=None):
        if box is None:
            box = {}

        # If box is already a BBox instance or has these attributes, use them
        if hasattr(box, "x1"):
            self.x1 = box.x1
        else:
            self.x1 = box.get("x1", 100)

        if hasattr(box, "y1"):
            self.y1 = box.y1
        else:
            self.y1 = box.get("y1", 100)

        if hasattr(box, "x2"):
            self.x2 = box.x2
        else:
            self.x2 = box.get("x2", 100)

        if hasattr(box, "y2"):
            self.y2 = box.y2
        else:
            self.y2 = box.get("y2", 100)

    def width(self):
        return self.x2 - self.x1

    def height(self):
        return self.y2 - self.y1

    def getSize(self):
        return {"height": self.y2 - self.y1, "width": self.x2 - self.x1}

    def merge(self, box):
        # Handle both dict and BBox object for input 'box'
        x1 = box.x1 if hasattr(box, "x1") else box.get("x1", 100)
        y1 = box.y1 if hasattr(box, "y1") else box.get("y1", 100)
        x2 = box.x2 if hasattr(box, "x2") else box.get("x2", 100)
        y2 = box.y2 if hasattr(box, "y2") else box.get("y2", 100)

        self.x1 = x1 if x1 <= self.x1 else self.x1
        self.y1 = y1 if y1 <= self.y1 else self.y1
        self.x2 = x2 if x2 >= self.x2 else self.x2
        self.y2 = y2 if y2 >= self.y2 else self.y2
        return self
