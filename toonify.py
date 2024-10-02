import cv2
import PIL.Image as Image
import numpy as np

def to_img(uploaded_file):
        pil_image = Image.open(uploaded_file)
        image = np.array(pil_image)
        return image
    
def read_img(file_path):
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def edge_detection(img, line_width, blur_amount):
    gray_scale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    gray_scale_img_blur = cv2.medianBlur(gray_scale_img, blur_amount)

    img_edges = cv2.adaptiveThreshold(gray_scale_img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_width, blur_amount)

    return img_edges

def color_segmentation(img, k_value, epochs, accuracy):     
    data = np.float32(img)
    data = data.reshape((-1, 3))
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, epochs, accuracy)

    compactness, labels, centers = cv2.kmeans(data, k_value, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    centers = np.uint8(centers)

    result = centers[labels.flatten()]

    result = result.reshape(img.shape)

    return result

def generate(image, TOTAL_COLORS=4,LINE_WIDTH=7,BLUR_VALUE=5):
    
    EPOCHS = 50
    ACCURACY = 0.01
 
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    edgeImg = edge_detection(image, LINE_WIDTH, BLUR_VALUE)
    segmented_img = color_segmentation(image, TOTAL_COLORS, EPOCHS, ACCURACY)
    
    blurred_img = cv2.bilateralFilter(segmented_img, d=7, sigmaColor=200, sigmaSpace=200)    
    cartoonized_img = cv2.bitwise_and(blurred_img, blurred_img, mask = edgeImg)    
    
    return cartoonized_img