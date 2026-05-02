class LandPlot:
    """Represents a rectangular plot of land."""

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        """Return the land area."""
        return self.length * self.width

    def perimeter(self) -> float:
        """Return the land perimeter."""
        return 2 * (self.length + self.width)

    def summary(self) -> str:
        """Return a formatted summary of the land measurements."""
        return (
            f"Land dimensions: {self.length:.2f} x {self.width:.2f}\n"
            f"Area: {self.area():.2f}\n"
            f"Perimeter: {self.perimeter():.2f}"
        )
