import tornado.web
import mysql.connector
import math

mysql_configs = dict(
    db_host="127.0.0.1",
    db_port=3306,
    db_name="video_website",
    db_user="root",
    db_pwd="38681"
)


class TurnChannelHandler(tornado.web.RequestHandler):
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

        # 获取频道id
        channel_id = self.get_argument("channel_id",default=None)

        # 用户获取
        if(channel_id):
            # 频道获取
            cursor_channel = cnx.cursor(dictionary=True)
            query_channel = "SELECT * FROM channel where id = %s"
            cursor_channel.execute(query_channel,[channel_id])
            channels = cursor_channel.fetchall()
            user_id = channels[0].get('CreatorID')
        else:
            # 频道获取
            channel_id = 1
            cursor_channel = cnx.cursor(dictionary=True)
            query_channel = "SELECT * FROM channel where id = %s"
            cursor_channel.execute(query_channel, [channel_id])
            channels = cursor_channel.fetchall()
            user_id = self.get_cookie("user_id")
        query_user = "SELECT * FROM user WHERE id = %s"
        cursor.execute(query_user, (user_id,))
        user = cursor.fetchall()

        # 查询总数据量
        cursor.execute("SELECT COUNT(*) AS total FROM video where channel_id = %s", (channel_id,))
        total_data = cursor.fetchone()['total']
        # 计算总页数
        total_pages = math.ceil(total_data / 8)
        # 计算偏移量
        offset = (page - 1) * 8
        # 执行查询
        query = "SELECT * FROM video where channel_id = %s LIMIT %s, 8"
        cursor.execute(query, (channel_id, offset,))
        # 获取结果
        videos = cursor.fetchall()

        # 关闭连接
        cursor.close()
        cnx.close()

        # 渲染 HTML 模板并传递频道信息
        self.render("SingleChannel.html", videos=videos, total_pages=total_pages, current_page=page, channels=channels, user=user)