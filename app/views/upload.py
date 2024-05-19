import tornado.web

class UploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("upload.html")