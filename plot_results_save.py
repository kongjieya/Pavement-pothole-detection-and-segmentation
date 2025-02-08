import pandas as pd
import matplotlib.pyplot as plt
import os

# 训练结果列表
results_files = [
    'runs/segment/yolo8(0.688_0.689)/results.csv',
    'runs/segment/yolo11(0.688_0.684)/results.csv',
    'runs/segment/yolov8seg-EMA-MPDIoU(0.693_0.695)/results.csv',
    'runs/segment/yolov8seg-EMA(0.714_0.707)/results.csv',
    'runs/segment/yolov8seg-EMA1-MPDIoU(0.705_0.713)/results.csv',
    'runs/segment/yolov8seg-EMA1(0.711_0.694)/results.csv',
    'runs/segment/yolov8seg-CBAM-MPDIoU(0.701_0.697)/results.csv',
    'runs/segment/yolov8seg-CBAM(0.716_0.725)/results.csv',
]

# 与results_files顺序对应
custom_labels = [
    'yolov8-seg',
    'yolo11-seg',
    'yolov8seg-EMA-MPDIoU',
    'yolov8seg-EMA',
    'yolov8seg-EMA1-MPDIoU',
    'yolov8seg-EMA1',
    'yolov8seg-CBAM-MPDIoU',
    'yolov8seg-CBAM',
]

def plot_comparison(metrics, labels, custom_labels, layout=(2, 2), save_dir=None):
    fig, axes = plt.subplots(layout[0], layout[1], figsize=(15, 10))  # 创建网格布局
    axes = axes.flatten()  # 将子图对象展平，方便迭代

    for i, (metric_key, metric_label) in enumerate(zip(metrics, labels)):
        for file_path, custom_label in zip(results_files, custom_labels):
            df = pd.read_csv(file_path)

            # 清理列名中的多余空格
            df.columns = df.columns.str.strip()

            # 检查 'epoch' 列是否存在
            if 'epoch' not in df.columns:
                print(f"'epoch' column not found in {file_path}. Available columns: {df.columns}")
                continue

            # 检查目标指标列是否存在
            if metric_key not in df.columns:
                print(f"'{metric_key}' column not found in {file_path}. Available columns: {df.columns}")
                continue

            # 在对应的子图上绘制线条
            axes[i].plot(df['epoch'], df[metric_key], label=f'{custom_label}')

        axes[i].set_title(f' {metric_label}')
        axes[i].set_xlabel('Epochs')
        axes[i].set_ylabel(metric_label)
        axes[i].legend()

    plt.tight_layout()  # 自动调整子图布局，防止重叠

    if save_dir:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        save_path = os.path.join(save_dir, f'{metric_label.replace(" ", "_")}.png')
        plt.savefig(save_path)
        print(f"Saved plot to {save_path}")
    else:
        plt.show()

if __name__ == '__main__':
    # 精度指标
    metrics = [
        'metrics/precision(B)', 'metrics/recall(B)', 'metrics/mAP50(B)', 'metrics/mAP50-95(B)',
        'metrics/precision(M)', 'metrics/recall(M)', 'metrics/mAP50(M)', 'metrics/mAP50-95(M)'
    ]

    labels = [
        'Precision (B)', 'Recall (B)', 'mAP@50 (B)', 'mAP@50-95 (B)',
        'Precision (M)', 'Recall (M)', 'mAP@50 (M)', 'mAP@50-95 (M)'
    ]

    # 调用通用函数绘制精度对比图，并保存结果
    plot_comparison(metrics, labels, custom_labels, layout=(2, 4), save_dir='plots/metrics')

    # 损失指标
    loss_metrics = [
        'train/box_loss', 'train/seg_loss', 'train/cls_loss', 'train/dfl_loss',
        'val/box_loss', 'val/seg_loss', 'val/cls_loss', 'val/dfl_loss'
    ]

    loss_labels = [
        'Train Box Loss', 'Train Seg Loss', 'Train Class Loss', 'Train DFL Loss',
        'Val Box Loss', 'Val Seg Loss', 'Val Class Loss', 'Val DFL Loss'
    ]

    # 调用通用函数绘制损失对比图，并保存结果
    plot_comparison(loss_metrics, loss_labels, custom_labels, layout=(2, 4), save_dir='plots/losses')