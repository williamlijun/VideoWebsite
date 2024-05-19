from app.views.index import IndexHandler as index
from app.views.register import RegisterHandler as register
from app.views.login import LoginHandler as login
from app.views.settings import SettingsHandler as settings
from app.views.intro import IntroHandler as intro
from app.views.upload import UploadHandler as upload
from app.views.account import AccountHandler as account
from app.views.blank import BlankHandler as blank
from app.views.blog import BlogHandler as blog
from app.views.categories import CategoriesHandler as categories
from app.views.channels import ChannelsHandler as channels
from app.views.contact import ContactHandler as contact
from app.views.error import ErrorHandler as error
from app.views.blog_detail import BlogDetailHandler as BlogDetail
from app.views.forgot_password import ForgotPasswordHandler as ForgotPassword
from app.views.history_page import HistoryPageHandler as HistoryPage
from app.views.single_channel import SingleChannelHandler as SingleChannel
from app.views.upload_video import UploadVideoHandler as UploadVideo
from app.views.video_page import VideoPageHandler as VideoPage
from app.views.video_page import VideoLikeHandler as VideoLike
from app.views.search import SearchHandler as search
from app.views.turn_channel import TurnChannelHandler as TurnChannel
from app.views.comments import CommentsHandler as comments
from app.views.image_search import ImageSearchHandler as ImageSearch

from app.views.back_office_management import BackOfficeManagementHandler as BackOfficeManagement
from app.views.channel_table_management import ChannelTableManagementHandler as ChannelTableManagement

import tornado
import os
urls = [
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "static/css")}),
    (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "static/img")}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "static/js")}),
    (r"/vendor/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "static/vendor")}),
    (r"/video/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "static/video")}),

    (r"/index(?:\?page=\d+)?", index),
    (r"/register", register),
    (r"/login", login),
    (r"/account(?:\?page=\d+)?", account),
    (r"/blank", blank),
    (r"/blog", blog),
    (r"/BlogDetail", BlogDetail),
    (r"/categories", categories),
    (r"/channels(?:\?page=\d+)?", channels),
    (r"/contact", contact),
    (r"/error", error),
    (r"/ForgotPassword", ForgotPassword),
    (r"/HistoryPage(?:\?history_page=\d+)?", HistoryPage),
    (r"/intro", intro),
    (r"/settings", settings),
    (r"/SingleChannel", SingleChannel),
    (r"/upload", upload),
    (r"/UploadVideo", UploadVideo),
    (r"/VideoPage(?:\?video_id=\d+)?", VideoPage),
    (r"/VideoLike", VideoLike),
    (r"/search", search),
    (r"/TurnChannel", TurnChannel),
    (r"/comments", comments),
    (r"/ImageSearch(?:\?results=.*)?", ImageSearch),

    (r"/BackOfficeManagement", BackOfficeManagement),
    (r"/ChannelTableManagement", ChannelTableManagement),
]