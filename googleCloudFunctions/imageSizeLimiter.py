# Google Cloud: Cloud Function

# PURPOSE
# Limit the maximum size of images that can be uploaded to the Google Cloud Storage

from PIL import Image

WIDTH_MAX_SIZE_PIXELS = 1600 # 2048
HEIGHT_MAX_SIZE_PIXELS = 1200 # 1365
INPUT_REQUEST_PREFIX = "---> Input:"

while True:
    print("Path to image that will be compressed and overwritten? [Enter blank to quit]")
    print(INPUT_REQUEST_PREFIX, end = " ")
    imagePath = input().strip()
    if not imagePath: break

    try:
        imageObj = Image.open(imagePath)
    except Exception:
        print("Failed to load image", imagePath)
        continue

    print("Current image size", imageObj.size)

    if imageObj.width <= WIDTH_MAX_SIZE_PIXELS and imageObj.height <= HEIGHT_MAX_SIZE_PIXELS:
        print("Image does not need to be compressed. Size is not exceeding limits of ({}, {})."
                .format(WIDTH_MAX_SIZE_PIXELS, HEIGHT_MAX_SIZE_PIXELS))
        continue

    if imageObj.width > WIDTH_MAX_SIZE_PIXELS:
        adjustedWidthPercentage = WIDTH_MAX_SIZE_PIXELS / imageObj.width
        adjustedHeight = int(imageObj.height * adjustedWidthPercentage)

        imageObj.resize((WIDTH_MAX_SIZE_PIXELS, adjustedHeight)).save(imagePath)
        imageObj = Image.open(imagePath)
        print("Width size exceeded limit. Resized image to ({}, {}).".format(WIDTH_MAX_SIZE_PIXELS,
                                                                            adjustedHeight))

    if imageObj.height > HEIGHT_MAX_SIZE_PIXELS:
        adjustedHeightPercentage = HEIGHT_MAX_SIZE_PIXELS / imageObj.height
        adjustedWidth = int(imageObj.width * adjustedHeightPercentage)

        imageObj.resize((adjustedWidth, HEIGHT_MAX_SIZE_PIXELS)).save(imagePath)
        imageObj = Image.open(imagePath)
        print("Height size exceeded limit. Resized image to ({}, {}).".format(adjustedWidth,
                                                                            HEIGHT_MAX_SIZE_PIXELS))

    print("Updated image size", imageObj.size)
