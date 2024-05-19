import tornado.web

# 博客


class BlogHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("blog.html")