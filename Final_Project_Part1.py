import cv2
import numpy as np


# Function to preprocess the image
def blur(img):

    ##BLUR THE IMAGE
    blurred = cv2.GaussianBlur(img,(9,9),3)

    return blurred
    
# Function to get contours and filter coins
def getContours(img,original,scale_factor):
    # Implement contour detection and filtering based on area and corners
    copy_of_coins = original
    
    contours , hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(copy_of_coins,contours,-1,(255,0,0),-1,cv2.LINE_AA,hierarchy)
    cv2.imshow('Contours',copy_of_coins)
    cv2.waitKey(1)


    counter, value = countCoins(contours,scale_factor)
    
    # Display the image with the contours and value overlays
    cv2.imshow('Contours', copy_of_coins)
    cv2.waitKey(1)
    print('Total Value is ', value)
    
    
#Function to calibrate the areas of the coin



# Function to count coins and determine their value
def countCoins(contours,scaling_factor):
    # Implement coin counting and value determination
    coin_count = 0
    coin_value = "Invalid Coin"
    total_value = 0.0
    for contour in contours:
        # Calculate the area of the contour
        #area = cv2.contourArea(contour)
        #print('Coin area: ',area)
        perimeter = cv2.arcLength(contour, True)
        #print('Coin perimeter:', perimeter)
        # Set a threshold for the minimum area to consider
        
        min_peri_threshold = 200  # Adjust this value based on your requirements

        if perimeter > min_peri_threshold:
            # Increment the coin count
            coin_count += 1

            if (perimeter>=690):
                coin_value = 0.25
            elif (perimeter<=690):
                coin_value = 0.01
            # Accumulate the total value
            if coin_value != "Invalid Coin":
                total_value += float(coin_value)  # Extract the numerical value from the coin type
                
    return coin_count,total_value    
    
    ##PLACEHOLDERS

# Main function
def main():
    #The sizes of the coins listed in mm^2

    DEFAULT_CAMERA = 0
    cam = cv2.VideoCapture(DEFAULT_CAMERA) 
    
    def nothing(x):
        pass
    cv2.namedWindow("Calibrate Contour")
    cv2.createTrackbar('threshold1','Calibrate Contour',88,240,nothing)
    cv2.createTrackbar('threshold2','Calibrate Contour',108,240,nothing)
    doit = False
    while(True):
        Boolean_val, frame = cam.read() 
       
        blurred = blur(frame)
        #idea of using trackbar to change thresholding from stackoverflow.
        #https://stackoverflow.com/questions/65926998/opencv-adaptive-thresholding-trackbar-manipulation
        t1 = cv2.getTrackbarPos('threshold1','Calibrate Contour')
        t2 = cv2.getTrackbarPos('threshold2','Calibrate Contour')
        edge = cv2.Canny(blurred,t1,t2)
        #implementation idea from stackoverflow to dilate.
        ##https://stackoverflow.com/questions/70932076/remove-noises-inside-circles-with-morphological-operations
        kernel = np.ones((3,3),np.uint8)
        dilated = cv2.dilate(edge, kernel, iterations=1)
        #The closing step does dilation followed by erosion of the coin.
        closed = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)


        getContours(closed,frame,0)#used scaling_factor before.
    
        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit the loop
            break
    
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
