import tornado.web
import mysql.connector
import math
import json


mysql_configs = dict(
    db_host="127.0.0.1",
    db_port=3306,
    db_name="video_website",
    db_user="root",
    db_pwd="38681"
)
# 频道


class ChannelsHandler(tornado.web.RequestHandler):
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

        # 获取当前页数，默认为第一页
        page = int(self.get_argument("page", default=1))

        # 查询总数据量
        cursor.execute("SELECT COUNT(*) AS total FROM channel")
        total_data = cursor.fetchone()['total']
        # 计算总页数
        total_pages = math.ceil(total_data / 8)
        # 计算偏移量
        offset = (page - 1) * 8
        # 执行查询
        query = "SELECT * FROM channel LIMIT %s, 8"
        cursor.execute(query, (offset,))

        # # 执行查询
        # query = "SELECT * FROM channel"
        # cursor.execute(query)

        # 获取结果
        channels = cursor.fetchall()

        # 用户获取
        user_id = self.get_cookie("user_id")
        if user_id is None:
            user_id = 10
        query_user = "SELECT * FROM user WHERE id = %s"
        cursor.execute(query_user, (user_id,))
        user = cursor.fetchall()

        # 关闭连接
        cursor.close()
        cnx.close()

        # 渲染 HTML 模板并传递频道信息
        self.render("channels.html", channels=channels, total_pages=total_pages, current_page=page, user=user)

    def post(self):
        # 连接数据库
        cnx = mysql.connector.connect(
            host=mysql_configs['db_host'],
            port=mysql_configs['db_port'],
            user=mysql_configs['db_user'],
            password=mysql_configs['db_pwd'],
            database=mysql_configs['db_name']
        )
        cursor = cnx.cursor(dictionary=True)

        try:
            # 解析 JSON 数据
            data = json.loads(self.request.body)
            # 获取通道ID
            channel_id = data.get("channel_id")
            if channel_id:
                # 向客户端发送响应
                self.write("订阅成功！")

                # 用户获取
                user_id = self.get_cookie("user_id")
                query_user = "SELECT * FROM user WHERE id = %s"
                cursor.execute(query_user, (user_id,))
                user = cursor.fetchall()
                username = user[0].get('username')

                query_subscribe = ("INSERT INTO subscription "
                                   "(channel_id, user_id, username) "
                                   "VALUES (%s, %s, %s)")
                cursor.execute(query_subscribe, (channel_id, user_id, username))

                cnx.commit()

                # 关闭数据库连接
                cursor.close()
                cnx.close()
            else:
                # 如果请求中没有channel_id字段，则返回错误响应
                self.set_status(400)
                self.write("错误：请求缺少channel_id字段")
                cnx.commit()

                # 关闭数据库连接
                cursor.close()
                cnx.close()
        except json.JSONDecodeError:
            # JSON 解析错误，返回错误响应
            self.set_status(400)
            self.write("错误：无法解析请求数据为JSON格式")