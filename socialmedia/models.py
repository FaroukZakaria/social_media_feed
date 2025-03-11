from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, db_index=True)
    email = models.EmailField(db_index=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username + " - " + self.email


class Post(models.Model):
    user = models.ForeignKey('User', related_name="posts", on_delete=models.CASCADE, db_index=True)
    title = models.CharField(max_length=255, db_index=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " by: " + self.user.username


class Like(models.Model):
    user = models.ForeignKey('User', related_name="likes", on_delete=models.CASCADE, db_index=True)
    post = models.ForeignKey('Post', related_name="likes", on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked {self.post.title} that is by {self.post.user.username}"

class Share(models.Model):
    user = models.ForeignKey('User', related_name="shares", on_delete=models.CASCADE, db_index=True)
    post = models.ForeignKey('Post', related_name="shares", on_delete=models.CASCADE, db_index=True)
    shared_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} shared {self.post.title} that is by {self.post.user.username}"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, db_index=True)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE, db_index=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title} that is by {self.post.user.username}"