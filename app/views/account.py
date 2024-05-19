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
class AccountHandler(tornado.web.RequestHandler):
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


        # 用户获取
        user_id = self.get_cookie("user_id")
        query_user = "SELECT * FROM user WHERE id = %s"
        cursor.execute(query_user, (user_id,))
        user = cursor.fetchall()

        # 查询总数据量
        cursor.execute("SELECT COUNT(*) AS total FROM video where video_blong_to = %s",(user[0].get('username'),))
        total_data = cursor.fetchone()['total']
        # 计算总页数
        total_pages = math.ceil(total_data / 8)
        # 计算偏移量
        offset = (page - 1) * 8
        # 执行查询
        query = "SELECT * FROM video where video_blong_to = %s LIMIT %s, 8"
        cursor.execute(query, (user[0].get('username'),offset,))
        # 获取结果
        videos = cursor.fetchall()

        # 频道获取
        cursor_channel = cnx.cursor(dictionary=True)
        query_channel = "SELECT c.* FROM channel c INNER JOIN subscription s ON c.id = s.channel_id WHERE s.user_id = %s"
        cursor_channel.execute(query_channel,(user_id,))
        channels = cursor_channel.fetchall()

        cnx.commit()

        # 关闭连接
        cursor.close()
        cnx.close()

        # 渲染 HTML 模板并传递频道信息
        self.render("account.html", videos=videos, total_pages=total_pages, current_page=page, channels=channels,user=user,)
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
                self.write("取消订阅成功！")

                # 用户获取
                user_id = self.get_cookie("user_id")

                query_subscribe = ("DELETE FROM subscription WHERE user_id = %s and channel_id = %s")
                cursor.execute(query_subscribe, (user_id, channel_id))

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