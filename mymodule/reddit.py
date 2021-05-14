class Post:
    def __init__(self, body, user, up_votes, down_votes):
        self.body = body
        self.user = user
        self.up_votes = up_votes
        self.down_votes = down_votes


class User:
    def __init__(self, name, reputation, is_moderator):
        self.name = name
        self.reputation = reputation
        self.is_moderator = is_moderator
        self.topics = []
        self.comments = []

    def post_topic(self, title, body):
        topic = Topic(title=title, body=body, user=self)
        self.topics.append(topic)
        return topic

    def post_comment(self, topic, body):
        comment = Comment(topic=topic, body=body, user=self)
        self.comments.append(comment)
        topic.comments.append(comment)
        return comment

    def up_vote(self, post:Post):
        post.up_votes += 1

class Topic(Post):
    def __init__(self, title, body, user, up_votes=0, down_votes=0):
        self.title = title
        self.comments = []
        self.comments.append(Comment(topic=self, body="OG Comment", user=user))
        super().__init__(
            body = body,
            user = user,
            up_votes = up_votes,
            down_votes = down_votes
        )


class Comment(Post):
    def __init__(self, topic, body,  user, up_votes=0, down_votes=0):
        self.topic = topic
        super().__init__(
            body = body,
            user = user,
            up_votes = up_votes,
            down_votes = down_votes
        )

