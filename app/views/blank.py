import tornado.web



class BlankHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("blank.html")