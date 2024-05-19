import tornado.web

# 博客详情


class BlogDetailHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("BlogDetail.html")