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

def plot_metric_comparison(metric_key, metric_label, custom_labels, save_path=None):
    plt.figure(figsize=(10, 6))

    for file_path, custom_label in zip(results_files, custom_labels):
        exp_name = os.path.basename(os.path.dirname(file_path))
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

        # 绘制没有圆点的线条
        plt.plot(df['epoch'], df[metric_key], label=f'{custom_label}')

    plt.title(f'{metric_label}')
    plt.xlabel('Epochs')
    plt.ylabel(metric_label)
    plt.legend()

    if save_path:
        plt.savefig(save_path)
        print(f"Saved plot to {save_path}")
    else:
        plt.show()

if __name__ == '__main__':
    metrics = [
        ('metrics/precision(B)', 'Precision (B)'),
        ('metrics/recall(B)', 'Recall (B)'),
        ('metrics/mAP50(B)', 'mAP@50 (B)'),
        ('metrics/mAP50-95(B)', 'mAP@50-95 (B)'),
        ('metrics/precision(M)', 'Precision (M)'),
        ('metrics/recall(M)', 'Recall (M)'),
        ('metrics/mAP50(M)', 'mAP@50 (M)'),
        ('metrics/mAP50-95(M)', 'mAP@50-95 (M)')
    ]

    for metric, label in metrics:
        plot_metric_comparison(metric, label, custom_labels, save_path=f'plot/{label}.png')

    loss_metrics = [
        ('train/box_loss', 'Train Box Loss'),
        ('train/seg_loss', 'Train Seg Loss'),
        ('train/cls_loss', 'Train Class Loss'),
        ('train/dfl_loss', 'Train DFL Loss'),
        ('val/box_loss', 'Val Box Loss'),
        ('val/seg_loss', 'Val Seg Loss'),
        ('val/cls_loss', 'Val Class Loss'),
        ('val/dfl_loss', 'Val DFL Loss')
    ]

    for metric, label in loss_metrics:
        plot_metric_comparison(metric, label, custom_labels, save_path=f'plot/{label}.png')