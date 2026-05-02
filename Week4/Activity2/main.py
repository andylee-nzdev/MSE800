from land_plot import LandPlot


def get_dimension(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Dimension must be greater than zero.")
            return value
        except ValueError as error:
            print(f"Invalid input: {error}")


if __name__ == "__main__":
    print("Rectangular Land Calculator")
    length = get_dimension("Enter the land length (meters): ")
    width = get_dimension("Enter the land width (meters): ")

    plot = LandPlot(length, width)
    print("\nCalculation Results:\n")
    print(plot.summary())
