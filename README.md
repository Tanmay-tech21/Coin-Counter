Coin Detection and Counting Readme

This Python script utilizes the OpenCV library to detect and count quarters (25 cents) and pennies (1 cent) in a live video stream. The script applies image blurring, contour detection, and coin counting based on predefined criteria.

Prerequisites

Python 3.x
OpenCV (cv2) library
NumPy library
Install the required libraries using the following command:

pip install opencv-python numpy

Usage

Run the script using the command:

python Final_Project_Part1.py
The script captures video from the default camera, applies image processing, and displays real-time results.
The script is calibrated to detect and count quarters and pennies. It utilizes contour detection and predefined perimeter thresholds for these specific coin types.
Customization

The script is designed to work with quarters and pennies. Modify the code in the countCoins function to accommodate additional coin types or adjust detection criteria.
Ensure that your camera is connected and accessible. Press 'Esc' to exit the script.
