import tornado.web


class BackOfficeManagementHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("back_office_management.html")