import cv2

# Load the image (replace 'your_image.jpg' with your image file)
image = cv2.imread('a.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to get a binary image
ret, thresh = cv2.threshold(gray, 127, 255, 0)

# Find contours in the binary image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    if len(approx) == 4:
        x, y, width, height = cv2.boundingRect(approx)
        aspect_ratio = float(width) / height
        ideal_aspect_ratio_range = (1.2, 2.5)
        
        if ideal_aspect_ratio_range[0] <= aspect_ratio <= ideal_aspect_ratio_range[1]:
            # This plate is close to ideal
            pass
        else:
            # This plate is not ideal, mark it!
            message = "NOT IDEAL"
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            color = (0, 0, 255)  # Red color
            text_size = cv2.getTextSize(message, font, font_scale, 1)[0]
            text_x = int((x + width - text_size[0]) / 2)
            text_y = int(y + height + text_size[1] + 10)
            
            cv2.putText(image, message, (text_x, text_y), font, font_scale, color, 2)

# Display the annotated image
cv2.imshow('Annotated Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
