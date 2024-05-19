import tornado.web
import mysql.connector

mysql_configs = dict(
    db_host="127.0.0.1",
    db_port=3306,
    db_name="video_website",
    db_user="root",
    db_pwd="38681"
)


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        error_message = self.get_query_argument("error", default=None)
        self.render("login.html", error=error_message)

    def post(self):
        phone_number = self.get_argument("phone_number")
        password = self.get_argument("password")

        if not phone_number or not password:
            self.redirect("/login")
            return
        if not self.validate_user(phone_number, password):
            self.redirect("/login?error=Invalid+phone+number+or+password")
            return

        self.redirect("/index")

    def validate_user(self, phone_number, password):
        try:
            db = mysql.connector.connect(
                host=mysql_configs['db_host'],
                port=mysql_configs['db_port'],
                user=mysql_configs['db_user'],
                password=mysql_configs['db_pwd'],
                database=mysql_configs['db_name']
            )
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM user WHERE phone_number = %s AND password = %s", (phone_number, password))
            result = cursor.fetchone()

            if result is None:
                return False

            # 设置名为"user_id"的Cookie
            self.set_cookie("user_id", str(result['id']))
            cursor.close()
            return result is not None
        except mysql.connector.Error as err:
            print(f"Error validating user: {err}")
            return False
