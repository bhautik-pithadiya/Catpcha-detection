import random
from PIL import Image, ImageDraw
import typing as t

ColorTuple = t.Union[t.Tuple[int, int, int], t.Tuple[int, int, int, int]]

def random_color(
        start: int,
        end: int,
        opacity: t.Optional[int] = None) -> ColorTuple:
    red = random.randint(start, end)
    green = random.randint(start, end)
    blue = random.randint(start, end)
    if opacity is None:
        return (red, green, blue)
    return (red, green, blue, opacity)

def draw_random_lines(image_size=(400, 400), num_lines=10, max_curve_depth=50, line_width=20):
    # Create a new white image
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)

    # Iterate over the number of lines
    for _ in range(num_lines):
        # Generate random start and end points for the line
        color = random_color(10, 200, random.randint(220, 255))
        x1 = random.randint(1, image_size[0])
        y1 = random.randint(1, image_size[1])
        x2 = random.randint(1, image_size[0])
        y2 = random.randint(1, image_size[1])

        # Determine if the line should be curved or straight
        if random.random() < 0.5:
            # Draw a straight line
            random_line_width = random.randint(1,line_width)
            draw.line([(x1, y1), (x2, y2)], fill="black", width=random_line_width)
        else:
            # Draw a curved line
            random_line_width = random.randint(1,line_width)

            curve_depth = random.randint(10, max_curve_depth)
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2
            end = random.randint(160, 200)
            start = random.randint(0, 20)
            if x1>x2:
                draw.arc([x1,y1, x2, y2], start,end,fill=color, width=random_line_width)
            else:
                draw.arc([ x2, y2,x1,y1], start,end,fill=color, width=random_line_width)

    # Show or save the image
    image.show()
    # image.save("random_lines.png")  # Save the image to a file

# Example usage:
draw_random_lines()
