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


class HistoryPageHandler(tornado.web.RequestHandler):
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

        # 获取历史观看页数，默认为第一页
        history_page = int(self.get_argument("history_page", default=1))

        # 用户获取
        user_id = self.get_cookie("user_id")
        query_user = "SELECT * FROM user WHERE id = %s"
        cursor.execute(query_user, (user_id,))
        user = cursor.fetchall()

        # 观看历史
        # 查询总数据量
        cursor.execute(
            "SELECT COUNT(*) AS total FROM video JOIN view_history ON video.id = view_history.video_id JOIN user ON view_history.user_id = user.id WHERE user.id = %s",
            (user_id,))
        history_total_data = cursor.fetchone()['total']
        # 计算总页数
        history_total_pages = math.ceil(history_total_data / 8)
        # 计算偏移量
        history_offset = (history_page - 1) * 8
        # 执行查询
        query = "SELECT video.* FROM video JOIN view_history ON video.id = view_history.video_id JOIN user ON view_history.user_id = user.id WHERE user.id = %s LIMIT %s, 8"
        cursor.execute(query, (user_id, history_offset,))
        # 获取结果
        history_videos = cursor.fetchall()

        # 关闭连接
        cursor.close()
        cnx.close()

        # 渲染 HTML 模板并传递频道信息
        self.render("HistoryPage.html", user=user, history_current_page=history_page, history_total_pages=history_total_pages, history_videos=history_videos)