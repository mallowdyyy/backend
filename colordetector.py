import cv2


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


while True:
   _, frame = cap.read()
   hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   height, width, _ = frame.shape


   cx = int(width / 2)
   cy = int(height / 2)


   # pick pixel value
   pixel_center = hsv_frame[cy, cx]
   hue_value = pixel_center[0]


   color = "Undefined"


   # Define ranges of hue values for colors
   red_lower = 0
   red_upper = 10
   orange_lower = 11
   orange_upper = 21
   yellow_lower = 22
   yellow_upper = 32
   green_lower = 33
   green_upper = 77
   blue_lower = 78
   blue_upper = 130
   violet_lower = 131
   violet_upper = 169
   pink_lower = 170
   pink_upper = 221


   # Classify the detected color based on the hue value
   if red_lower <= hue_value <= red_upper:
       color = "Red"
       text_color = (0, 0, 255)  # Red color
   elif orange_lower <= hue_value <= orange_upper:
       color = "Orange"
       text_color = (0, 165, 255)  # Orange color
   elif yellow_lower <= hue_value <= yellow_upper:
       color = "Yellow"
       text_color = (0, 255, 255)  # Yellow color
   elif green_lower <= hue_value <= green_upper:
       color = "Green"
       text_color = (0, 255, 0)  # Green color
   elif blue_lower <= hue_value <= blue_upper:
       color = "Blue"
       text_color = (255, 0, 0)  # Blue color
   elif violet_lower <= hue_value <= violet_upper:
       color = "Violet"
       text_color = (138, 43, 226)  # Violet color
   elif pink_lower <= hue_value <= pink_upper:
       color = "Pink"
       text_color = (255, 192, 203)  # Pink color
   else:
       color = "No color detected"
       text_color = (255, 255, 255)  # White color for undefined color


   cv2.putText(frame, color, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, text_color, 2)
   cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)


   cv2.imshow('frame', frame)
   key = cv2.waitKey(1)
   if key == 27:
       break


cap.release()
cv2.destroyAllWindows()
