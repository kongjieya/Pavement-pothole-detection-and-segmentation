from ultralytics import YOLO
import cv2

# 加载训练好的模型
model = YOLO('runs/segment/yolov8seg-CBAM(0.716_0.725)/weights/best.pt')

# 读取视频
video_path = 'datasets/Pothole-seg/sample_video.mp4'
cap = cv2.VideoCapture(video_path)

# 获取视频的宽度、高度和帧率
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 定义视频编解码器并创建 VideoWriter 对象
out = cv2.VideoWriter('save/segmented_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 对每一帧进行分割
    results = model.predict(frame)
    
    # 可视化分割结果
    for result in results:
        segmented_frame = result.plot()
        # 写入处理后的帧到视频文件
        out.write(segmented_frame)
    
    # 显示分割结果（可选）
    cv2.imshow('Segmented Frame', segmented_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放视频捕获和写入对象
cap.release()
out.release()
cv2.destroyAllWindows()