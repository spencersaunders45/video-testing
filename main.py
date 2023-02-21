import cv2

vidcap = cv2.VideoCapture('stock_video1.mp4')
success, image = vidcap.read()
count = 1
while success:
    cv2.imwrite("video_data/image_%d.jpeg" % count, image)    
    success, image = vidcap.read()
    print('Saved image ', count)
    count += 1