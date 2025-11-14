import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
score = 0 


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # change frame it is fliped 
    frame = cv.flip(frame, 1)

    # display score 
    text = "player score:" + str(score)
    org = (50, 250)  # Bottom-left corner of the text (x, y)
    font = cv.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    color = (0, 255, 0)  # BGR color (Green in this case)
    thickness = 2
    line_type = cv.LINE_AA # For anti-aliased lines

    # Write the text on the image
    cv.putText(frame, text, org, font, font_scale, color, thickness, line_type)

    
    # Get the original dimensions
    height, width = frame.shape[:2]

    # Resize the frame to half its size
    frame_half = cv.resize(frame, (width // 2, height // 2), interpolation=cv.INTER_AREA)

    # Our operations on the frame come here
    gray = cv.cvtColor(frame_half, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    #cv.imshow('frame', gray)
    cv.imshow('frame', frame_half)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
