# from ultralytics import YOLO

# # Load a pretrained YOLO11n model
# # model = YOLO("yolo11n.pt")

# model = YOLO("runs/segment/train2/weights/best.pt")

# # Run inference on 'bus.jpg' with arguments
# model.predict("ultralytics-main/ultralytics/assets/1.jpg", save=True)
from ultralytics import YOLO
import cv2

# 加载训练好的模型
model = YOLO('runs/segment/yolov8seg-CBAM(0.716_0.725)/weights/best.pt')

# 读取图片
image_path = 'datasets/Pothole-seg/valid/images/pic-17-_jpg.rf.0d172b6accedf4c52a3868d9b690d48b.jpg'
image = cv2.imread(image_path)

# 对图片进行分割
results = model.predict(image)

# 可视化分割结果
for result in results:
    segmented_image = result.plot()
    # 保存分割结果
    cv2.imwrite('save/segmented_image.jpg', segmented_image)
    # 显示分割结果
    cv2.imshow('Segmented Image', segmented_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()