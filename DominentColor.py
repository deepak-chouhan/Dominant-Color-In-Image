from PIL import Image
import colorsys

def getDominentColor(image_file):
    """
    Return the Dominent Hue in Image
    """
    image = Image.open(image_file)
    
    # Find dominant colors
    paletted = image.convert('P', palette=Image.Palette.ADAPTIVE, colors=10)
    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)
    colors = list()
    for i in range(10):
        palette_index = color_counts[i][1]
        dominant_color = palette[palette_index*3:palette_index*3+3]
        colors.append(tuple(dominant_color))
    
    # Convert RGB to HSV
    for i in range(len(colors)):
        color = colors[i]
        colors[i] = colorsys.rgb_to_hsv(color[0], color[1], color[2])
    
    # return color with max saturation
    max_index = 0
    max_saturation = colors[0][1]
    for i in range(len(colors)):
        if colors[i][1] > max_saturation:
            max_saturation = colors[i][1]
            max_index = i
    
    dominent_color = colors[max_index]
    dominent_hue = round(dominent_color[0] * 360)
    
    return dominent_hue


if __name__ == "__main__":
    print("Dominant Hue:", getDominentColor("./image_1.png"))
    print("Dominant Hue:", getDominentColor("./image_2.png"))
    print("Dominant Hue:", getDominentColor("./image_3.png"))