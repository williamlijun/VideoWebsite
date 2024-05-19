import tornado.web
import mysql.connector
import math
from openai import OpenAI
import os
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

client = OpenAI(base_url="http://localhost:12345/v1", api_key="lm-studio")


# 设置OpenAI API密钥
# client = OpenAI(
#   api_key=os.environ.get("sk-proj-qMUypho1vpJIcGViHvyyT3BlbkFJT3UO6FyveswuC3XV1v7A"),
# )

mysql_configs = dict(
    db_host="127.0.0.1",
    db_port=3306,
    db_name="video_website",
    db_user="root",
    db_pwd="38681"
)
# 频道


class VideoPageHandler(tornado.web.RequestHandler):
    def get(self):
        # 连接数据库
        global recommended_videos, recommended_by_tag_videos
        cnx = mysql.connector.connect(
                host=mysql_configs['db_host'],
                port=mysql_configs['db_port'],
                user=mysql_configs['db_user'],
                password=mysql_configs['db_pwd'],
                database=mysql_configs['db_name']
            )
        cursor = cnx.cursor(dictionary=True)

        # 执行查询
        query = "SELECT * FROM video"
        cursor.execute(query)

        # 获取结果
        video = cursor.fetchall()

        video_id = self.get_argument('video_id', default=None)
        if video_id is None:
            video_id = 1
        else:
            video_id = int(video_id)

        # 检查是否已经存在相同的历史记录
        exists_query = "SELECT COUNT(*) AS count FROM view_history WHERE video_id = %s AND user_id = %s"
        user_id = self.get_cookie("user_id")
        cursor.execute(exists_query, (video_id, user_id))
        result = cursor.fetchone()
        if result['count'] == 0:  # 如果历史记录不存在，则插入新记录
            # 插入历史记录
            insert_query = "INSERT INTO view_history (video_id, user_id) VALUES (%s, %s)"
            user_id = self.get_cookie("user_id")
            cursor.execute(insert_query, (video_id, user_id))
            cnx.commit()  # 提交事务

        # 用户获取
        user_id = self.get_cookie("user_id")
        if user_id is None:
            user_id = 10
        query_user = "SELECT * FROM user WHERE id = %s"
        cursor.execute(query_user, (user_id,))
        user = cursor.fetchall()

        # 标签查询
        query = "SELECT * FROM video_tag WHERE video_id = %s"
        cursor.execute(query,(video_id,))
        # 获取结果
        video_tag = cursor.fetchall()



        # 查询user_tag表数据
        query = "SELECT user_id, tag FROM user_tag"
        cursor.execute(query)
        user_tag_data = cursor.fetchall()
        # 获取用户和标签列表
        users = list(set([data['user_id'] for data in user_tag_data]))
        tags = list(set([data['tag'] for data in user_tag_data]))
        # 建立用户ID到矩阵索引的映射
        user_id_to_idx = {user_id: idx for idx, user_id in enumerate(users)}
        # 构建用户-标签矩阵
        user_tag_matrix = np.zeros((len(users), len(tags)))
        # 填充矩阵
        for data in user_tag_data:
            user_idx = user_id_to_idx[data['user_id']]
            tag_idx = tags.index(data['tag'])
            user_tag_matrix[user_idx, tag_idx] += 1
        # 计算用户之间的余弦相似度
        user_sim_matrix = cosine_similarity(user_tag_matrix)
        # 假设需要找到与其最相似的用户ID为user_id
        user_id = int(self.get_cookie("user_id"))
        if user_id in user_id_to_idx:
            user_idx = user_id_to_idx[user_id]
            # 将自身与自身的相似度值设为0
            user_sim_matrix[user_idx, user_idx] = 0
            similarities = user_sim_matrix[user_idx]
            # 找到与用户最相似的用户ID
            most_similar_user_idx = np.argmax(similarities)  # 选择最相似的用户
            most_similar_user_id = users[most_similar_user_idx]

            # 根据相似用户的历史记录进行推荐
            # 查询user_tag表数据
            query = "SELECT video.* FROM view_history JOIN video ON view_history.video_id = video.id WHERE view_history.user_id = %s;"
            cursor.execute(query,(most_similar_user_id,))
            recommended_videos = cursor.fetchall()
        else:
            print("未找到用户ID为 {} 的用户信息".format(user_id))


        # 查询video_tag表数据
        query = "SELECT video_id, tag FROM video_tag"
        cursor.execute(query)
        video_tag_data = cursor.fetchall()
        # 获取video和标签列表
        videos = list(set([data['video_id'] for data in video_tag_data]))
        tags = list(set([data['tag'] for data in video_tag_data]))
        # 建立videoID到矩阵索引的映射
        video_id_to_idx = {video_id: idx for idx, video_id in enumerate(videos)}
        # 构建video-标签矩阵
        video_tag_matrix = np.zeros((len(videos), len(tags)))
        # 填充矩阵
        for data in video_tag_data:
            video_idx = video_id_to_idx[data['video_id']]
            tag_idx = tags.index(data['tag'])
            video_tag_matrix[video_idx, tag_idx] += 1
        # 计算video之间的余弦相似度
        video_sim_matrix = cosine_similarity(video_tag_matrix)
        # 假设需要找到与相似的videoID为video_id
        video_id = int(video_id)
        if video_id in video_id_to_idx:
            video_idx = video_id_to_idx[video_id]
            # 将自身与自身的相似度值设为0
            video_sim_matrix[video_idx, video_idx] = 0
            similarities = video_sim_matrix[video_idx]
            # 找到与指定视频最相似的前5个视频
            most_similar_indices = np.argsort(similarities)[::-1][1:6]  # 选择前五个最相似的视频（排除自身）
            # 构造包含前五个最相似视频ID的元组
            similar_video_ids = tuple(videos[idx] for idx in most_similar_indices)
            # 执行查询
            query = "SELECT * FROM video WHERE id IN {}".format(similar_video_ids)
            cursor.execute(query)
            # 获取结果
            recommended_by_tag_videos = cursor.fetchall()
        else:
            print("未找到视频ID为 {} 的视频信息".format(video_id))

        # 关闭连接
        cursor.close()
        cnx.close()

        # 渲染 HTML 模板并传递频道信息
        chatgpt_response = None
        self.render("VideoPage.html", videos=video, videoId=video_id, user=user, video_tags=video_tag,recommended_videos=recommended_videos, recommended_by_tag_videos=recommended_by_tag_videos)

    def post(self):
        # 连接数据库
        cnx = mysql.connector.connect(
            host=mysql_configs['db_host'],
            port=mysql_configs['db_port'],
            user=mysql_configs['db_user'],
            password=mysql_configs['db_pwd'],
            database=mysql_configs['db_name']
        )
        cursor = cnx.cursor(dictionary=True)

        video_id = self.get_body_argument("video-id", default=None)

        if video_id is None:
            video_id = 1
        else:
            video_id = int(video_id)

        # 执行查询
        query = "SELECT video_title FROM video WHERE id = %s"
        cursor.execute(query, (video_id,))

        # 获取结果
        result = cursor.fetchone()
        if result:
            if result["video_title"]:
                video_title = result["video_title"]
            else:
                video_title = "Unknown"
        else:
            video_title = "Unknown"  # 如果找不到对应视频的标题，可以给一个默认值，比如 "Unknown"


        # 关闭连接
        cursor.close()
        cnx.close()

        user_input = self.get_body_argument("user-input")  # 获取用户输入

        completion = client.chat.completions.create(
            model="Qwen/qwen1_5-7b-chat-q2_k",
            messages=[
                {"role": "system", "content": "you are a chatbot"},
                {"role": "user", "content": "我正在观看一个视频,这个视频标题是" + video_title + "，接下来请与我对话，" + user_input}
            ],
            temperature=0.7,
        )
        print(completion.choices[0].message)
        chatgpt_response = completion.choices[0].message.content
        self.write(chatgpt_response)  # 返回 ChatGPT 的回复


class VideoLikeHandler(tornado.web.RequestHandler):
    def post(self):
        # 连接数据库
        global query
        cnx = mysql.connector.connect(
            host=mysql_configs['db_host'],
            port=mysql_configs['db_port'],
            user=mysql_configs['db_user'],
            password=mysql_configs['db_pwd'],
            database=mysql_configs['db_name']
        )
        cursor = cnx.cursor(dictionary=True)

        try:
            # 从前端页面获取视频 ID 和点赞类型
            video_id = self.get_body_argument("video-id")
            like_type = self.get_argument('type')
            user_id = self.get_cookie("user_id")

            if like_type == 'favorite':
                # 查询用户是否已收藏该视频
                query = "SELECT * FROM favorite_video WHERE video_id = %s AND user_id = %s"
                cursor.execute(query, (video_id, user_id))
                existing_favorite = cursor.fetchone()

                if existing_favorite:
                    # 如果已收藏，则取消收藏
                    delete_query = "DELETE FROM favorite_video WHERE video_id = %s AND user_id = %s"
                    cursor.execute(delete_query, (video_id, user_id))
                    cnx.commit()
                    self.write(json.dumps({"favorite": "not favorited"}))
                else:
                    # 如果未收藏，则执行收藏操作
                    insert_query = "INSERT INTO favorite_video (video_id, user_id, is_favorite) VALUES (%s, %s, %s)"
                    cursor.execute(insert_query, (video_id, user_id, 1))
                    cnx.commit()
                    self.write(json.dumps({"favorite": "collected"}))
            else:
                # 查询用户是否已对该视频进行过点赞操作
                query = "SELECT * FROM like_table WHERE video_id = %s AND user_id = %s"
                cursor.execute(query, (video_id, user_id))
                existing_like = cursor.fetchone()

                if existing_like:
                    # 表示取消操作
                    if like_type == 'like' and existing_like['is_like'] == 1:
                        # 用户取消点赞
                        delete_query = "DELETE FROM like_table WHERE video_id = %s AND user_id = %s"
                        cursor.execute(delete_query, (video_id, user_id))
                        cnx.commit()
                    elif like_type == 'dislike' and existing_like['is_like'] == 0:
                        # 用户取消踩
                        delete_query = "DELETE FROM like_table WHERE video_id = %s AND user_id = %s"
                        cursor.execute(delete_query, (video_id, user_id))
                        cnx.commit()
                    # 删除点赞/踩后，更新视频表中的点赞和踩数量
                    update_likes_query = "UPDATE video SET likes = (SELECT COUNT(*) FROM like_table WHERE video_id = %s AND is_like = 1), dislike = (SELECT COUNT(*) FROM like_table WHERE video_id = %s AND is_like = 0) WHERE id = %s"
                    cursor.execute(update_likes_query, (video_id, video_id, video_id))
                    cnx.commit()
                else:
                    # 插入新的点赞记录
                    if like_type == 'like':
                        like_value = 1
                    elif like_type == 'dislike':
                        like_value = 0

                    insert_query = "INSERT INTO like_table (video_id, user_id, is_like) VALUES (%s, %s, %s)"
                    cursor.execute(insert_query, (video_id, user_id, like_value))
                    cnx.commit()

                    # 更新视频表中的点赞数量
                    update_query = "UPDATE video SET likes = (SELECT COUNT(*) FROM like_table WHERE video_id = %s AND is_like = 1), dislike = (SELECT COUNT(*) FROM like_table WHERE video_id = %s AND is_like = 0) WHERE id = %s"
                    cursor.execute(update_query, (video_id, video_id, video_id))
                    cnx.commit()

                # 获取更新后的视频信息
                select_query = "SELECT * FROM video WHERE id = %s"
                cursor.execute(select_query, (video_id,))
                result = cursor.fetchone()

                self.write(json.dumps(result))

        except Exception as e:
            self.set_status(500)
            self.write(json.dumps({"error": str(e)}))

        finally:
            # 关闭连接
            cursor.close()
            cnx.close()