from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 加载训练好的模型
model = YOLO('runs/segment/yolov8seg-CBAM(0.716_0.725)/weights/best.pt')

# 读取图片
image_path = 'datasets/Pothole-seg/valid/images/pic-17-_jpg.rf.0d172b6accedf4c52a3868d9b690d48b.jpg'
image = cv2.imread(image_path)

# 对图片进行分割
results = model.predict(image)

# 检查返回的结果
if not results:
    raise ValueError("No results returned from model prediction")

# 创建一个空的 mask
mask_combined = np.zeros_like(image, dtype=np.uint8)



# 遍历所有结果并累加 mask
for result in results:
    for mask in result.masks.data:
        mask = mask.cpu().numpy()
        mask_3channel = np.stack((mask,)*3, axis=-1) * 255
        mask_3channel = mask_3channel.astype(np.uint8)
        mask_combined = cv2.add(mask_combined, mask_3channel)

# 将 mask 颜色设置为红色
mask_red = np.zeros_like(mask_combined)
mask_red[:, :, 2] = mask_combined[:, :, 2]  # 只将红色通道设为 255（分割区域）

# # 创建一个与原图相同的黑色图像，用于加权混合
# black_image = np.zeros_like(image)

# # 只在分割区域应用红色遮罩
# segmented_image = cv2.addWeighted(image, 0.7, black_image, 0.3, 0)
# segmented_image[mask_combined[:, :, 2] != 0] = cv2.addWeighted(image, 0.7, mask_red, 0.3, 0)[mask_combined[:, :, 2] != 0]

# 将 mask 叠加到原图上
segmented_image = image.copy()
segmented_image[mask_combined[:, :, 2] != 0] = [255, 0, 0]  # 只改变分割区域的颜色为蓝色

# segmented_image = cv2.addWeighted(image, 0.7, mask_combined, 0.3, 0)

# 将 BGR 转换为 RGB 以便 matplotlib 显示
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
segmented_image_rgb = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB)
mask_rgb = cv2.cvtColor(mask_combined, cv2.COLOR_BGR2RGB)


# 显示原图、mask 和分割后的图像
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].imshow(image_rgb)
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(mask_rgb)
ax[1].set_title('Segmentation Mask')
ax[1].axis('off')

ax[2].imshow(segmented_image_rgb)
ax[2].set_title('Segmented Image')
ax[2].axis('off')

plt.show()

# 保存分割结果
cv2.imwrite('save/segmented_images.jpg', segmented_image)
