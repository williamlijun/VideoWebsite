import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

import cv2
import torchvision.transforms as transforms
from torchvision.models import resnet50, ResNet50_Weights
import random

random.seed(0)
torch.manual_seed(0)
torch.cuda.manual_seed_all(0)
torch.backends.cudnn.deterministic = True

# 加载预训练的 ResNet 模型
model = resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
model.fc = torch.nn.Linear(in_features=model.fc.in_features, out_features=256)

transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
])

video_data = []

for i in range(1, 34):  # 遍历33个视频文件
    cap = cv2.VideoCapture(f'C:/Users/34341\PycharmProjects/VideoWebsite/app\static/video/{i}.mp4')
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

    all_features = torch.cat(features, dim=0)  # 将当前视频的所有帧特征拼接起来形成一个张量
    mean_features = torch.mean(all_features, dim=0)  # 计算当前视频所有帧特征的平均值
    print(mean_features.tolist())
    video_data.append(mean_features.tolist())  # 将当前视频的平均特征转换为列表形式并添加到 video_data 中

aaaaa = torch.tensor(video_data).to(torch.float32)
print(aaaaa)  # 输出所有视频的特征向量列表


# 定义模型架构
class MultiLabelClassifier(nn.Module):
    def __init__(self, input_size, num_classes):
        super(MultiLabelClassifier, self).__init__()
        self.fc = nn.Linear(input_size, num_classes)

    def forward(self, x):
        return torch.sigmoid(self.fc(x))  # 使用sigmoid激活函数处理多标签分类问题


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

tag_to_index = {tag: i for i, tag in enumerate(all_tags)}

print(all_tags)

def encode_tags(tags, tag_to_index):
    encoded = [0] * len(tag_to_index)
    for tag in tags:
        encoded[tag_to_index[tag]] = 1
    return torch.tensor(encoded)


# 将列表转换为张量
X = torch.tensor(video_data).to(torch.float32)
y = []
for video_id, tags in video_tags.items():
    label = encode_tags(tags, tag_to_index)
    y.append(label)

X = X.clone().detach().to(torch.float32)
y = torch.stack(y)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = X, X, y, y  # 这里假设没有划分，实际应该根据需求划分
# 将标签转换为与模型输出相同的数据类型
y_train = y_train.type(torch.float32)
y_test = y_test.type(torch.float32)

# 创建数据加载器
train_dataset = TensorDataset(X_train, y_train)
train_loader = DataLoader(train_dataset, batch_size=1, shuffle=True)

# 初始化模型、损失函数和优化器
model = MultiLabelClassifier(256, len(all_tags))
# model.load_state_dict(torch.load('model2.pth'))  # 加载之前保存的模型参数
criterion = nn.BCELoss()  # 二元交叉熵损失
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 训练模型
num_epochs = 500
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0

    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        outputs = outputs.type(torch.float32)  # 将输出转换为Float类型
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    print(f'Epoch {epoch + 1}, Loss: {running_loss / len(train_loader)}')

# 在测试集上评估模型
model.eval()
with torch.no_grad():
    test_outputs = model(X_test)
    test_outputs = test_outputs.type(torch.float32)  # 将测试输出也转换为Float类型
    test_loss = criterion(test_outputs, y_test)
    print(f'Test Loss: {test_loss.item()}')

# 假设您已经训练好了模型 model，并且想要保存模型参数到文件 'model.pth'
torch.save(model.state_dict(), 'model.pth')

