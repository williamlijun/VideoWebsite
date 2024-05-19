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

# 查询video_tag表和view_history表，获取user_id和tag
query = """
SELECT vh.user_id, vt.tag
FROM view_history vh
JOIN video_tag vt ON vh.video_id = vt.video_id
"""

cursor.execute(query)
results = cursor.fetchall()

# 插入数据到user_tag表
for row in results:
    user_id = row['user_id']
    tag = row['tag']

    insert_query = "INSERT INTO user_tag (user_id, tag) VALUES (%s, %s)"
    insert_data = (user_id, tag)
    cursor.execute(insert_query, insert_data)

# 提交事务并关闭连接
cnx.commit()
cursor.close()
cnx.close()