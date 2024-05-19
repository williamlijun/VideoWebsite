import tornado.web

# 类别


class CategoriesHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("categories.html")