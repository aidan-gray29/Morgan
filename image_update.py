from PIL import Image, ImageSequence
import sys

# imports the Reaction GIFs folder to be used in the directory
def file_get(emotion):
    switch= {
        'angry': './ReactionGIFs/dino_angry.gif',
        'happy': './ReactionGIFs/dino_happy.gif',
        'bored': './ReactionGIFs/dino_bored.gif',
        'sad': './ReactionGIFs/dino_sad.gif',
        'confused': './ReactionGIFs/dino_confused.gif'
    }
    return switch.get(emotion, "Invalid")

# Changes a file from a GIF to PNGs
def processImage(infile):
    img = Image.open(infile)
    pal = img.getpalette()
    prev = img.convert('RGBA')
    prev_dispose = True
    for i, frame in enumerate(ImageSequence.Iterator(img)):
        dispose = frame.dispose

        if frame.tile:
            x0, y0, x1, y1 = frame.tile[0][1]
            if not frame.palette.dirty:
                frame.putpalette(pal)
            frame = frame.crop((x0, y0, x1, y1))
            bbox = (x0, y0, x1, y1)
        else:
            bbox = None

        if dispose is None:
            prev.paste(frame, bbox, frame.convert('RGBA'))
            prev.save('foo%02d.png' % i)
            prev_dispose = False
        else:
            if prev_dispose:
                prev = Image.new('RGBA', img.size, (0, 0, 0, 0))
            out = prev.copy()
            out.paste(frame, bbox, frame.convert('RGBA'))
            out.save('foo%02d.png' % i)

# Accepts an image and changes its color to either red, green, or blue
def colorChange(file_name):
    img = Image.open(file_name)
    img = img.convert('RGB')

    width = img.size[0] 
    height = img.size[1] 
    for i in range(0,width):# process all pixels
        for j in range(0,height):
            data = img.getpixel((i,j))
            #print(data) #(255, 255, 255)
            if (data[0]==0 and data[1]==0 and data[2]==0):
                img.putpixel((i,j),(255, 0, 0))
    # d = image.getdata()

    # new_image = []
    # for item in d:
    #     if item[0] in list(range(0,1)):
    #         new_image.append((255,0,0))
    #     else:
    #         new_image.append(item)
    
    # image.putdata(new_image)
    # image.save("altered_red.png")

    # red = RGBTransform().mix_with((255, 0, 0),factor=.30).applied_to(image)
    # green = RGBTransform().mix_with((0, 255, 0),factor=.30).applied_to(image)
    # blue = RGBTransform().mix_with((0, 0, 255),factor=.30).applied_to(image)


if __name__ == "__main__":
    processImage(file_get('angry'))
    # colorChange("foo00.png")