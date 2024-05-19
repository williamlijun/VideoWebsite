import tornado.web
import mysql.connector
import os
import torch.nn as nn
import cv2
import torchvision.transforms as transforms
from torchvision.models import resnet50, ResNet50_Weights
# 设置随机种子
import random
import torch

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

mysql_configs = dict(
    db_host="127.0.0.1",
    db_port=3306,
    db_name="video_website",
    db_user="root",
    db_pwd="38681"
)

UPLOAD_DIRECTORY = "C:/Users/34341/PycharmProjects/VideoWebsite/app/static/video"


class UploadVideoHandler(tornado.web.RequestHandler):
    def get(self):
        # 连接数据库
        cnx = mysql.connector.connect(
            host=mysql_configs['db_host'],
            port=mysql_configs['db_port'],
            user=mysql_configs['db_user'],
            password=mysql_configs['db_pwd'],
            database=mysql_configs['db_name']
        )
        cursor = cnx.cursor(dictionary=True)
        # 用户获取
        user_id = self.get_cookie("user_id")
        if user_id is None:
            user_id = 10
        query_user = "SELECT * FROM user WHERE id = %s"
        cursor.execute(query_user, (user_id,))
        user = cursor.fetchall()

        query_user = "SELECT * FROM channel WHERE CreatorID = %s"
        cursor.execute(query_user, (user_id,))
        channels = cursor.fetchall()

        # 关闭数据库连接
        cursor.close()
        cnx.close()

        self.render("UploadVideo.html", message=None, user=user, channels=channels)


    def post(self):
        # 信息获取
        video_title = self.get_argument("videoTitle")
        privacy = self.get_argument("privacy")
        channel = self.get_argument("channel")
        description = self.get_argument("describe")
        video_file = self.request.files["videoFile"][0]


        # 连接数据库
        cnx = mysql.connector.connect(
            host=mysql_configs['db_host'],
            port=mysql_configs['db_port'],
            user=mysql_configs['db_user'],
            password=mysql_configs['db_pwd'],
            database=mysql_configs['db_name']
        )
        cursor = cnx.cursor(dictionary=True)

        # 用户获取
        user_id = self.get_cookie("user_id")
        query_user = "SELECT * FROM user WHERE id = %s"
        cursor.execute(query_user, (user_id,))
        user = cursor.fetchall()


        # 将上传的视频文件保存到服务器上的指定目录
        file_path = os.path.join(UPLOAD_DIRECTORY, video_file["filename"])
        with open(file_path, "wb") as f:
            f.write(video_file["body"])

        # 插入视频信息到数据库
        insert_query = ("INSERT INTO video "
                        "(video_title, video_url, Privacy, video_description, video_blong_to, channel_id) "
                        "VALUES (%s, %s, %s, %s, %s, %s)")
        video_url = 'video/' + video_file["filename"]
        video_data = (video_title, video_url, privacy, description, user[0]['username'], channel)
        cursor.execute(insert_query, video_data)
        cnx.commit()

        random.seed(0)
        torch.manual_seed(0)
        torch.cuda.manual_seed_all(0)
        torch.backends.cudnn.deterministic = True

        # 加载预训练的 ResNet 模型
        model = resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
        model.fc = torch.nn.Linear(in_features=model.fc.in_features, out_features=256)

        # 读取视频
        cap = cv2.VideoCapture(f'C:/Users/34341\PycharmProjects/VideoWebsite/app\static/video/{video_file["filename"]}')

        transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
        ])

        features = []

        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            input_tensor = transform(frame).unsqueeze(0)

            with torch.no_grad():
                output = model(input_tensor)
                features.append(output)

        cap.release()

        all_features = torch.cat(features, dim=0)  # 将所有视频特征拼接起来形成一个张量

        new_video_features = torch.mean(all_features, dim=0)  # 计算所有视频特征的平均值
        new_video_features = new_video_features.tolist()  # 转换为 Python 列表格式

        # 定义模型架构
        class MultiLabelClassifier(nn.Module):
            def __init__(self, input_size, num_classes):
                super(MultiLabelClassifier, self).__init__()
                self.fc = nn.Linear(input_size, num_classes)

            def forward(self, x):
                return torch.sigmoid(self.fc(x))

        # 加载数据
        video_tags = {
            1: ['动漫'],
            2: ['电影片段', '剪辑', '悲伤'],
            3: ['动漫', '唯美'],
            4: ['动漫', '唯美'],
            5: ['海盗', '海盗'],
            6: ['励志', '剪辑'],
            7: ['唯美', '剪辑'],
            8: ['战争'],
            9: ['战争', '感动'],
            10: ['战争', '感动'],
            11: ['科幻', '搞笑'],
            12: ['唯美', '剪辑'],
            13: ['动漫', '音乐'],
            14: ['动漫', '感动'],
            15: ['动漫', '动作'],
            16: ['动漫', '动作'],
            17: ['动漫', '唯美'],
            18: ['动漫', '动作'],
            19: ['搞笑', '剪辑'],
            20: ['搞笑', '动漫'],
            21: ['动漫', '动作'],
            22: ['动漫', '动作'],
            23: ['奥特曼', '阴暗'],
            24: ['剪辑', '搞笑'],
            25: ['剪辑', '搞笑'],
            26: ['励志', '剪辑'],
            27: ['励志', '剪辑'],
            28: ['励志', '电影片段'],
            29: ['剪辑', '黑社会'],
            30: ['治愈', '唯美'],
            31: ['唯美', '美丽'],
            32: ['剪辑', '电影片段'],
            33: ['电影解说', '科幻']
        }

        # 从 video_tags 中获取所有标签，并按照特定顺序构建 all_tags 列表
        all_tags = []
        seen_tags = set()

        for tags in video_tags.values():
            for tag in tags:
                if tag not in seen_tags:
                    all_tags.append(tag)
                    seen_tags.add(tag)

        # 加载训练好的模型
        model = MultiLabelClassifier(256, len(all_tags))  # 假设已定义了模型结构
        model_path = os.path.join(current_dir, 'model.pth')
        model.load_state_dict(torch.load(model_path))  # 加载模型参数
        model.eval()  # 设置为评估模式

        # 准备新视频数据特征向量进行预测
        new_video_features = new_video_features  # 假设这是新视频的特征向量
        new_video_features = torch.tensor(new_video_features, dtype=torch.float32).unsqueeze(0)  # 添加批次维度

        # 使用模型进行预测
        with torch.no_grad():
            output = model(new_video_features)
            print(output)
            predicted_labels = (output > 0.3).int()  # 根据输出概率是否大于0.3进行阈值判断，得到预测的标签

        print(all_tags)
        # 输出预测结果
        predicted_tags = [all_tags[i] for i in range(len(predicted_labels[0])) if predicted_labels[0][i] == 1]
        print("预测的标签为：", predicted_tags)

        for i in range(len(predicted_tags)):
            query = "SELECT id FROM video ORDER BY id DESC LIMIT 1"
            cursor.execute(query)
            video = cursor.fetchall()
            video_id = video[0]['id']

            insert_query = ("INSERT INTO video_tag "
                            "(video_id, tag) "
                            "VALUES (%s, %s)")
            video_data = (video_id, predicted_tags[i])
            cursor.execute(insert_query, video_data)
            cnx.commit()


        query_user = "SELECT * FROM channel WHERE CreatorID = %s"
        cursor.execute(query_user, (user_id,))
        channels = cursor.fetchall()

        # 关闭数据库连接
        cursor.close()
        cnx.close()

        message = None

        self.render('UploadVideo.html', message="Video uploaded successfully.",user=user, channels=channels)