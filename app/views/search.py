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


class SearchHandler(tornado.web.RequestHandler):
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
        # 获取搜索框
        query = self.get_argument("query", default=None)

        # 构建查询语句
        if query:
            # 查询包含搜索词的记录总数
            cursor.execute("SELECT COUNT(*) AS total FROM video WHERE video_title LIKE %s", ('%' + query + '%',))
            total_data = cursor.fetchone()['total']
            # 计算总页数
            total_pages = math.ceil(total_data / 8)
            # 计算偏移量
            offset = (page - 1) * 8
            # 执行查询
            query_search = "SELECT * FROM video WHERE video_title LIKE %s LIMIT %s, 8"
            cursor.execute(query_search, ('%' + query + '%', offset,))
        else:
            # 查询总数据量
            cursor.execute("SELECT COUNT(*) AS total FROM video")
            total_data = cursor.fetchone()['total']
            # 计算总页数
            total_pages = math.ceil(total_data / 8)
            # 计算偏移量
            offset = (page - 1) * 8
            # 执行查询
            query_search = "SELECT * FROM video LIMIT %s, 8"
            cursor.execute(query_search, (offset,))

        # 获取结果
        videos = cursor.fetchall()

        # 频道获取
        cursor_channel = cnx.cursor(dictionary=True)
        query_channel = "SELECT * FROM channel"
        cursor_channel.execute(query_channel)
        channels = cursor_channel.fetchall()

        # 最受欢迎频道获取
        cursor_popular_channel = cnx.cursor(dictionary=True)
        query_popular_channel = "SELECT * FROM channel ORDER BY subscribe_number DESC LIMIT 4"
        cursor_popular_channel.execute(query_popular_channel)
        popular_channels = cursor_popular_channel.fetchall()

        # 用户获取
        user_id = self.get_cookie("user_id")
        query_user = "SELECT * FROM user WHERE id = %s"
        cursor.execute(query_user, (user_id,))
        user = cursor.fetchall()

        # 关闭连接
        cursor.close()
        cnx.close()

        # 渲染 HTML 模板并传递频道信息
        self.render("index.html", videos=videos, total_pages=total_pages, current_page=page, channels=channels, user=user ,popular_channels=popular_channels)