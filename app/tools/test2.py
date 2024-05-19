import torch.nn as nn
import cv2
import torchvision.transforms as transforms
from torchvision.models import resnet50, ResNet50_Weights
# 设置随机种子
import random
import torch

random.seed(0)
torch.manual_seed(0)
torch.cuda.manual_seed_all(0)
torch.backends.cudnn.deterministic = True

# 加载预训练的 ResNet 模型
model = resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
model.fc = torch.nn.Linear(in_features=model.fc.in_features, out_features=256)

# 读取视频
cap = cv2.VideoCapture('C:/Users/34341\PycharmProjects/VideoWebsite/app\static/video/test.mp4')

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
model.load_state_dict(torch.load('model.pth'))  # 加载模型参数
model.eval()  # 设置为评估模式

# 准备新视频数据特征向量进行预测
new_video_features = new_video_features  # 假设这是新视频的特征向量
new_video_features = torch.tensor(new_video_features, dtype=torch.float32).unsqueeze(0)  # 添加批次维度

# 使用模型进行预测
with torch.no_grad():
    output = model(new_video_features)
    print(output)
    predicted_labels = (output > 0.5).int()  # 根据输出概率是否大于0.5进行阈值判断，得到预测的标签


print(all_tags)
# 输出预测结果
predicted_tags = [all_tags[i] for i in range(len(predicted_labels[0])) if predicted_labels[0][i] == 1]
print("预测的标签为：", predicted_tags)
