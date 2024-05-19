import hashlib
import os
import tornado.web
import requests
import json

UPLOAD_PATH = r'C:\Users\34341\PycharmProjects\VideoWebsite\app\static\search_img'


class ImageSearchHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("ImageSearch.html")

    def post(self):
        global img_path
        fileinfo = self.request.files.get('image')
        if fileinfo:
            filename = fileinfo[0]['filename']
            image = fileinfo[0]['body']

            # 生成唯一的文件名，可以使用哈希值
            file_hash = hashlib.md5(image).hexdigest()
            filepath = os.path.join(UPLOAD_PATH, file_hash + '_' + filename)

            # 保存文件到指定位置
            with open(filepath, 'wb') as f:
                f.write(image)
            img_path = 'search_img/' + file_hash + '_' + filename

            # 调用外部API进行图片识别
            response = requests.post("https://api.trace.moe/search", files={"image": (filename, image)})
            if response.status_code == 200:
                results = response.json()
                result_list = results['result']
                result_json = json.dumps(result_list)
                self.write(result_json)
            else:
                self.set_status(response.status_code)
                self.write(response.text)
        else:
            self.set_status(400)
            self.write("未上传任何图片")