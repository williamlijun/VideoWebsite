import tornado.web

class IntroHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("intro.html")