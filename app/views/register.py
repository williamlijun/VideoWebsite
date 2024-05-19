import tornado.web
import mysql.connector

mysql_configs = dict(
    db_host="127.0.0.1",
    db_port=3306,
    db_name="video_website",
    db_user="root",
    db_pwd="38681"
)


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        error_message = self.get_query_argument("error", default=None)
        self.render("register.html", error=error_message)

    def post(self):
        phone_number = self.get_argument("phone_number")
        password = self.get_argument("password")

        if not phone_number or not password:
            self.redirect("/register?error=Please+provide+both+username+and+password")
            return

        if self.user_exists(phone_number):
            self.redirect("/register?error=User+already+exists!")
            return

        try:
            self.insert_user(phone_number, password)
            self.write("Registered successfully!")
            self.redirect("/login")
        except mysql.connector.Error as err:
            self.write(f"Error registering user: {err}")

    def user_exists(self, phone_number):
        try:
            db = mysql.connector.connect(
                host=mysql_configs['db_host'],
                port=mysql_configs['db_port'],
                user=mysql_configs['db_user'],
                password=mysql_configs['db_pwd'],
                database=mysql_configs['db_name']
            )
            cursor = db.cursor()
            cursor.execute("SELECT * FROM user WHERE phone_number = %s", (phone_number,))
            result = cursor.fetchone()
            cursor.close()
            return result is not None
        except mysql.connector.Error as err:
            print(f"Error checking user existence: {err}")
            return False

    def insert_user(self, phone_number, password):
        db = mysql.connector.connect(
            host=mysql_configs['db_host'],
            port=mysql_configs['db_port'],
            user=mysql_configs['db_user'],
            password=mysql_configs['db_pwd'],
            database=mysql_configs['db_name']
        )
        cursor = db.cursor()
        cursor.execute("INSERT INTO user (phone_number, password) VALUES (%s, %s)", (phone_number, password))
        db.commit()
        cursor.close()
