import tornado.web
import mysql.connector
import json

mysql_configs = dict(
    db_host="127.0.0.1",
    db_port=3306,
    db_name="video_website",
    db_user="root",
    db_pwd="38681"
)


class CommentsHandler(tornado.web.RequestHandler):
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

        video_id = self.get_argument('video_id', default=None)
        if video_id is None:
            video_id = 1
        else:
            video_id = int(video_id)


        query = "SELECT * FROM comment WHERE video_id = %s"
        cursor.execute(query, (video_id,))
        comments = cursor.fetchall()
        self.write(json.dumps(comments))  # 将评论数据以 JSON 格式发送到前端
    def post(self):
        # 从请求中获取评论内容
        comment_text = self.get_body_argument('comment')
        # 用户获取
        user_id = self.get_cookie("user_id")
        # 视频id
        video_id = self.get_body_argument("videoId", default=None)

        # 连接数据库
        cnx = mysql.connector.connect(
            host=mysql_configs['db_host'],
            port=mysql_configs['db_port'],
            user=mysql_configs['db_user'],
            password=mysql_configs['db_pwd'],
            database=mysql_configs['db_name']
        )
        cursor = cnx.cursor(dictionary=True)

        # 插入评论
        query = ("INSERT INTO comment "
                 "(video_id, user_id, comments) "
                 "VALUES (%s, %s, %s)")
        cursor.execute(query, (video_id, user_id, comment_text))

        cnx.commit()

        # 关闭连接
        cursor.close()
        cnx.close()

        # 返回成功的响应
        self.write("Comment submitted successfully!")
