import tornado.web
import mysql.connector


mysql_configs = dict(
    db_host="127.0.0.1",
    db_port=3306,
    db_name="video_website",
    db_user="root",
    db_pwd="38681"
)


class ChannelTableManagementHandler(tornado.web.RequestHandler):
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

        query = "SELECT * FROM channel"
        cursor.execute(query)
        channels = cursor.fetchall()

        # 关闭连接
        cursor.close()
        cnx.close()

        self.render("channel_table_management.html", channels=channels)