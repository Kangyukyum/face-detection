import cv2
import cvlib as cv

frame_count = 0
capture_count = 0

cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret, frame = cam.read()
    frame_count += 1
    
    if ret == False:
        break
    
    face, conf = cv.detect_face(frame)
    
    for idx, pos in enumerate(face):
        (startX, startY) = pos[0], pos[1]
        (endX, endY) = pos[2], pos[3]
        
        if frame_count % 10 == 0:
            if capture_count == 85:
                break
            capture_count += 1
            image = frame[startY:endY, startX:endX, :]
            #cv2.imwrite(r'D:\Mask_dataset\Mask\maskface'+str(capture_count)+'.jpg', image)
            #cv2.imwrite(r'D:\Mask_dataset\NoMask\nomaskface'+str(capture_count)+'.jpg', image)
            cv2.imwrite(r'D:\Mask_dataset\InvalidMask\invalidmaskface'+str(425+capture_count)+'.jpg', image)
    
    cv2.imshow('capturing face image now', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()