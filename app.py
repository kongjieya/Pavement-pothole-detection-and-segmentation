import streamlit as st
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from plot_results_save import plot_comparison, custom_labels  # 导入 custom_labels
import subprocess
import os
import tempfile
from ultralytics import YOLO
import time  # 导入 time 模块用于添加延迟
import base64

# 设置页面配置
st.set_page_config(page_title="基于 YOLO 的路面坑洞检测与分割系统", page_icon=":road:", layout="wide")

# 初始化会话状态
if 'page' not in st.session_state:
    st.session_state.page = 'main'

if 'stop_camera_detection' not in st.session_state:
    st.session_state.stop_camera_detection = False

if 'custom_background' not in st.session_state:
    st.session_state.custom_background = None
if 'use_custom_background' not in st.session_state:
    st.session_state.use_custom_background = False

# 默认背景设为 None，表示使用 Streamlit 默认背
default_background = None
def set_background(main_bg):
    if main_bg is None:
        return
    main_bg_ext = "png"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
# 每次页面渲染时检查并设置背景
if st.session_state.use_custom_background and st.session_state.custom_background:
    set_background(st.session_state.custom_background)
else:
    set_background(default_background)




# 获取 runs 目录下的所有模型文件
models_dir = "runs/segment"
models = {}  # 使用字典来存储模型名和对应的 best.pt 文件路径
for root, dirs, files in os.walk(models_dir):
    if "weights" in root and "best.pt" in files:
        model_name = os.path.basename(os.path.dirname(root))
        model_path = os.path.join(root, "best.pt")
        models[model_name] = model_path

# 主页面
if st.session_state.page == 'main':

    # 显示 Logo 和标语
    logo = Image.open("logo.png")  # 请替换为实际的 Logo 图片路径
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(logo, width=150)
    with col2:
        st.title("基于 YOLO 的路面坑洞检测与分割系统")
        st.subheader("精准检测，高效分割，助力道路安全！")

    # 用卡片式布局展示功能
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("系统功能概览")

    # 创建一个4列布局，模拟原始卡片布局
    col1, col2, col3, col4 = st.columns(4)

    # 模拟卡片样式，包裹按钮和描述文字
    with col1:
        with st.container():
            st.markdown("""
                <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                    <button style="width: 100%; background-color: #007bff; color: white; border: none; padding: 10px 0; font-size: 16px; border-radius: 8px;">模型性能分析</button>
                    <p style="text-align: center;">深入了解模型的各项性能指标。</p>
                </div>
            """, unsafe_allow_html=True)

    with col2:
        with st.container():
            st.markdown("""
                <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                    <button style="width: 100%; background-color: #007bff; color: white; border: none; padding: 10px 0; font-size: 16px; border-radius: 8px;">图片检测</button>
                    <p style="text-align: center;">上传图片，快速检测路面坑洞。</p>
                </div>
            """, unsafe_allow_html=True)

    with col3:
        with st.container():
            st.markdown("""
                <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                    <button style="width: 100%; background-color: #007bff; color: white; border: none; padding: 10px 0; font-size: 16px; border-radius: 8px;">视频检测</button>
                    <p style="text-align: center;">支持视频和摄像头实时检测。</p>
                </div>
            """, unsafe_allow_html=True)

    with col4:
        with st.container():
            st.markdown("""
                <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                    <button style="width: 100%; background-color: #007bff; color: white; border: none; padding: 10px 0; font-size: 16px; border-radius: 8px;">设置</button>
                    <p style="text-align: center;">个性化定制系统界面。</p>
                </div>
            """, unsafe_allow_html=True)

    # 添加间距
    st.markdown("<br>", unsafe_allow_html=True)  # 添加额外的间距

    # 使用 Streamlit 列布局让按钮居中
    _, _, center_col, _ = st.columns([1, 1, 1, 1])
    with center_col:
        if st.button("进入系统", key="main_enter_button"):
            st.balloons()
            st.toast('欢迎进入系统！', icon='🎉')
            time.sleep(.5)
            st.toast('正在加载功能模块...', icon='💫')
            time.sleep(.5)
            st.toast('即将为您展示功能选择页面。', icon='😍')
            time.sleep(1)
            st.session_state.page = 'function_selection'
            st.rerun()


    # # 进入系统按钮
    # if st.button("进入系统", key="main_enter_button"):
    #     st.session_state.page = 'function_selection'
    #     st.rerun()



# 功能选择页面
elif st.session_state.page == 'function_selection':
    def m_exit():
        msg = st.toast('感谢你的使用！', icon="🥰")
        time.sleep(2)
        msg.toast('欢迎下次再来哦！', icon = "💖")
    if st.button("退出系统", key="function_exit_button"):
        st.snow()
        m_exit()
        time.sleep(1)
        st.session_state.page = 'main'
        st.rerun()

    # 定义侧边栏
    with st.sidebar:
        st.title("功能选择")
        selected_function = st.radio("请选择功能", ["模型性能分析", "图片检测", "视频检测", "设置"])

    # # 模型列表
    # models = ["YOLOv5", "YOLOv6", "YOLOv7"]

    

    # 模型性能分析界面
    if selected_function == "模型性能分析":     
        st.title("模型性能分析")
        st.write("这里将展示模型的性能分析结果，如准确率、召回率等。")

        # 精度指标
        metrics = [
            'metrics/precision(B)', 'metrics/recall(B)', 'metrics/mAP50(B)', 'metrics/mAP50-95(B)',
            'metrics/precision(M)', 'metrics/recall(M)', 'metrics/mAP50(M)', 'metrics/mAP50-95(M)'
        ]

        labels = [
            'Precision (B)', 'Recall (B)', 'mAP@50 (B)', 'mAP@50-95 (B)',
            'Precision (M)', 'Recall (M)', 'mAP@50 (M)', 'mAP@50-95 (M)'
        ]

        # 调用通用函数绘制精度对比图
        st.subheader("Metrics")
        fig_num_before = plt.get_fignums()
        plot_comparison(metrics, labels, custom_labels, layout=(2, 4), save_dir=None)
        fig_num_after = plt.get_fignums()
        new_fig_num = [num for num in fig_num_after if num not in fig_num_before][0]
        fig_metrics = plt.figure(new_fig_num)
        st.pyplot(fig_metrics)

        # 损失指标
        loss_metrics = [
            'train/box_loss', 'train/seg_loss', 'train/cls_loss', 'train/dfl_loss',
            'val/box_loss', 'val/seg_loss', 'val/cls_loss', 'val/dfl_loss'
        ]

        loss_labels = [
            'Train Box Loss', 'Train Seg Loss', 'Train Class Loss', 'Train DFL Loss',
            'Val Box Loss', 'Val Seg Loss', 'Val Class Loss', 'Val DFL Loss'
        ]

        # 调用通用函数绘制损失对比图
        st.subheader("Losses")
        fig_num_before = plt.get_fignums()
        plot_comparison(loss_metrics, loss_labels, custom_labels, layout=(2, 4), save_dir=None)
        fig_num_after = plt.get_fignums()
        new_fig_num = [num for num in fig_num_after if num not in fig_num_before][0]
        fig_losses = plt.figure(new_fig_num)
        st.pyplot(fig_losses)

        


    # 图片检测界面
    elif selected_function == "图片检测":
        st.title("图片检测")
        # 选择模型
        selected_model_name = st.selectbox("选择模型", list(models.keys()))
        selected_model = models[selected_model_name]  # 获取对应的 best.pt 文件路径

        # 上传图片
        uploaded_file = st.file_uploader("上传图片", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            st.success("图片上传成功！")
            # 读取图片
            image = Image.open(uploaded_file)
            image_path = "temp_image.jpg"
            image.save(image_path)  # 保存上传的图片到临时文件

            #  # 调用 predict_seg.py 进行检测
            # command = f"python predict_seg.py --model {selected_model} --image {image_path}"
            # subprocess.run(command, shell=True)

            # # 读取 predict_seg.py 保存的结果图片
            # original_image = cv2.imread(image_path)
            # segmented_image = cv2.imread('save/segmented_image.jpg')

            # 调用 seg_mask.py 进行检测
            command = f"python seg_mask.py --model {selected_model} --image {image_path}"
            subprocess.run(command, shell=True)

            # 读取 seg_mask.py 保存的结果图片
            original_image = cv2.imread(image_path)
            # segmented_image = cv2.imread('save/segmented_images.jpg')

           

            # 重新运行 seg_mask.py 中的部分代码来生成 mask 图像
            # from ultralytics import YOLO
            model = YOLO(selected_model)
            results = model.predict(original_image)
            mask_combined = np.zeros_like(original_image, dtype=np.uint8)
            for result in results:
                predicted_image = result.plot()
                for mask in result.masks.data:
                    mask = mask.cpu().numpy()
                    mask_3channel = np.stack((mask,) * 3, axis=-1) * 255
                    mask_3channel = mask_3channel.astype(np.uint8)
                    mask_combined = cv2.add(mask_combined, mask_3channel)
            mask_rgb = cv2.cvtColor(mask_combined, cv2.COLOR_BGR2RGB)

            segmented_image = original_image.copy()
            segmented_image[mask_combined[:, :, 2] != 0] = [255, 0, 0]

            # 将 BGR 转换为 RGB 以便 streamlit 显示
            original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
            segmented_image_rgb = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB)

            # 读取预测图片
            # predicted_image = cv2.imread('save/segmented_image.jpg')
            predicted_image_rgb = cv2.cvtColor(predicted_image, cv2.COLOR_BGR2RGB)

            # 显示原图、mask 和分割后的图像和预测图片
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.image(original_image_rgb, caption="原图", use_container_width=True)
            with col2:
                st.image(mask_rgb, caption="分割掩码", use_container_width=True)
            with col3:
                st.image(segmented_image_rgb, caption="分割后的图像", use_container_width=True)
            with col4:
                st.image(predicted_image_rgb, caption="预测图片", use_container_width=True)

            # # 单独展示预测图片
            # st.image(predicted_image_rgb, caption="预测图片", use_container_width=True)

            # 删除临时文件
            os.remove(image_path)

    # 视频检测界面
    elif selected_function == "视频检测":
        st.title("视频检测")
        # 选择模型
        selected_model_name = st.selectbox("选择模型", list(models.keys()))
        selected_model = models[selected_model_name]  # 获取对应的 best.pt 文件路径

        # 选择上传视频还是打开摄像头
        source = st.radio("选择视频源", ["上传视频", "打开摄像头"])

        if source == "上传视频":
            uploaded_video = st.file_uploader("上传视频", type=["mp4", "avi"])
            if uploaded_video is not None:
                st.success("视频上传成功！")
                # 保存视频到临时文件
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as f:
                    f.write(uploaded_video.read())
                    temp_video_path = f.name

                # 获取视频的总帧数
                cap = cv2.VideoCapture(temp_video_path)
                total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                cap.release()

                # 创建进度条
                progress_bar = st.progress(0)

                # 调用 predict_seg_video.py 进行视频检测
                output_video_path = "save/segmented_video.mp4"
                if os.path.exists(output_video_path):
                    os.remove(output_video_path)

                model = YOLO(selected_model)
                cap = cv2.VideoCapture(temp_video_path)
                frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                fps = int(cap.get(cv2.CAP_PROP_FPS))
                out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

                frame_count = 0
                frame_placeholder = st.empty()

                # 创建结束检测按钮
                stop_button = st.button("结束视频检测", key="stop_video_detection")

                while cap.isOpened() and not stop_button:
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

                    # 更新进度条
                    frame_count += 1
                    progress_percent = frame_count / total_frames
                    progress_bar.progress(progress_percent)

                    # 显示分割结果（可选）
                    frame_placeholder.image(segmented_frame, channels="BGR", use_container_width=True)

                    # 更新按钮状态
                    stop_button = st.session_state.get("stop_video_detection", False)

                # 释放视频捕获和写入对象
                cap.release()
                out.release()
                # 移除 cv2.destroyAllWindows() 这行代码
                # cv2.destroyAllWindows()
                time.sleep(1)  # 释放后等待 1 秒

                # 显示处理后的视频
                if os.path.exists(output_video_path):
                    st.video(output_video_path)

        elif source == "打开摄像头":
            st.write("即将打开摄像头进行实时检测...")
            cap = cv2.VideoCapture(0)  # 打开摄像头
            frame_placeholder = st.empty()
            model = YOLO(selected_model)

            # 创建结束检测按钮
            if st.button("结束检测", key="start_stop_button"):
                st.session_state.stop_camera_detection = True

            while cap.isOpened() and not st.session_state.stop_camera_detection:
                ret, frame = cap.read()
                if not ret:
                    break

                # 对每一帧进行分割
                results = model.predict(frame)

                # 可视化分割结果
                for result in results:
                    segmented_frame = result.plot()

                # 显示分割结果
                frame_placeholder.image(segmented_frame, channels="BGR", use_container_width=True)

            # 释放摄像头
            cap.release()

            # 重置会话状态
            st.session_state.stop_camera_detection = False

    # 设置界面
    elif selected_function == "设置":
        st.title("设置")
        # 设置背景
        background_image = st.file_uploader("上传背景图片", type=["jpg", "jpeg", "png"])
        if background_image is not None:
            # 保存上传的图片到本地临时文件
            import tempfile
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
            temp_file.write(background_image.read())
            temp_file.close()
            st.session_state.custom_background = temp_file.name
            st.session_state.use_custom_background = True
            st.write("背景图片设置成功！")

        # 切换背景按钮
        if st.button("切换背景"):
            st.session_state.use_custom_background = not st.session_state.use_custom_background
            st.write("切换成功")

        # 恢复默认背景按钮
        if st.button("恢复默认背景"):
            st.session_state.use_custom_background = False
            st.session_state.custom_background = None
            st.write("已恢复默认背景")

            
