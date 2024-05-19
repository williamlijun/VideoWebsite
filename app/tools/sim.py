import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import mysql.connector

mysql_configs = dict(
    db_host="127.0.0.1",
    db_port=3306,
    db_name="video_website",
    db_user="root",
    db_pwd="38681"
)

# 连接数据库
cnx = mysql.connector.connect(
    host=mysql_configs['db_host'],
    port=mysql_configs['db_port'],
    user=mysql_configs['db_user'],
    password=mysql_configs['db_pwd'],
    database=mysql_configs['db_name']
)
cursor = cnx.cursor(dictionary=True)

# 查询user_tag表数据
query = "SELECT user_id, tag FROM user_tag"
cursor.execute(query)
user_tag_data = cursor.fetchall()

# 获取用户和标签列表
users = list(set([data['user_id'] for data in user_tag_data]))
tags = list(set([data['tag'] for data in user_tag_data]))

# 构建用户-标签矩阵
user_tag_matrix = np.zeros((len(users), len(tags)))


# 填充矩阵
for data in user_tag_data:
    user_idx = users.index(data['user_id'])
    tag_idx = tags.index(data['tag'])
    user_tag_matrix[user_idx, tag_idx] += 1

print("用户-标签矩阵：")
print(user_tag_matrix)

# 关闭连接
cursor.close()
cnx.close()


# 计算用户之间的余弦相似度
user_sim_matrix = cosine_similarity(user_tag_matrix)

print("用户之间的余弦相似度矩阵：")
print(user_sim_matrix)