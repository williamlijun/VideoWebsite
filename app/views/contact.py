import tornado.web


class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("contact.html")