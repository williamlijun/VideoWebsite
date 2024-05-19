import tornado.web


class ForgotPasswordHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("ForgotPassword.html")