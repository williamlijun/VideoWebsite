import tornado.web


class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("404.html")