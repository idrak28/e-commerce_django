from PIL import Image, ImageDraw, ImageFont


def generate_pictures_with_names(names, output_folder="output_images"):
    import os

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Create an image for each name
    for name in names:
        # Create an image with a white background
        image_width, image_height = 300, 300
        background_color = (255, 255, 255)  # White
        image = Image.new("RGB", (image_width, image_height), background_color)

        # Initialize drawing context
        draw = ImageDraw.Draw(image)

        # Load a font
        try:
            font = ImageFont.truetype(
                "arial.ttf", size=500
            )  # Change font path if needed
        except IOError:
            font = (
                ImageFont.load_default()
            )  # Use default font if TrueType font is unavailable

        # Calculate text size and position
        text_bbox = draw.textbbox((0, 0), name, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = (image_width - text_width) // 2
        text_y = (image_height - text_height) // 2

        # Write the name on the image
        text_color = (0, 0, 0)  # Black
        draw.text((text_x, text_y), name, fill=text_color, font=font)

        # Save the image
        output_file = os.path.join(output_folder, f"{name.replace(' ', '_')}.png")
        image.save(output_file)
        print(f"Image with name '{name}' saved as '{output_file}'")


# Example usage
names_list = [
    "book1",
    "book2",
    "book3",
    "book4",
    "book11",
    "book22",
    "book33",
    "book44",
]
generate_pictures_with_names(names_list)
