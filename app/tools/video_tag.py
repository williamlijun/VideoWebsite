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

query = "SELECT video_id, tag FROM video_tag"

cursor = cnx.cursor(dictionary=True)
cursor.execute(query)

video_tag_dict = {}

for row in cursor.fetchall():
    video_id = row['video_id']
    tag = row['tag']
    if video_id in video_tag_dict:
        video_tag_dict[video_id].append(tag)
    else:
        video_tag_dict[video_id] = [tag]

cursor.close()
cnx.close()

print(video_tag_dict)
