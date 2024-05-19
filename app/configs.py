import os

root_path = os.path.dirname(__file__)

configs = dict(
    debug = True,
    template_path = os.path.join(root_path, "templates"),
    static_path = os.path.join(root_path, "static"),
)

mysql_configs = dict(
    db_host="127.0.0.1",
    db_port=3306,
    db_name="video_website",
    db_user="root",
    db_pwd="38681"
)
link = "mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}".format(
    **mysql_configs
)