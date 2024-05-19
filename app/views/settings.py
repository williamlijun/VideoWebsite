import tornado.web
import mysql.connector


mysql_configs = dict(
    db_host="127.0.0.1",
    db_port=3306,
    db_name="video_website",
    db_user="root",
    db_pwd="38681"
)


class SettingsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('settings.html', message=None)

    def post(self):
        # 信息获取
        username = self.get_argument("username")
        password = self.get_argument("password")
        phone_number = self.get_argument("phone_number")


        # 连接数据库
        cnx = mysql.connector.connect(
            host=mysql_configs['db_host'],
            port=mysql_configs['db_port'],
            user=mysql_configs['db_user'],
            password=mysql_configs['db_pwd'],
            database=mysql_configs['db_name']
        )
        cursor = cnx.cursor(dictionary=True)

        # 用户获取
        user_id = self.get_cookie("user_id")
        query_user = "UPDATE user SET username = %s, password = %s, phone_number = %s WHERE id = %s"
        cursor.execute(query_user, (username, password, phone_number, user_id))

        cnx.commit()

        # 关闭数据库连接
        cursor.close()
        cnx.close()

        message = None

        self.render('settings.html', message="successfully.")