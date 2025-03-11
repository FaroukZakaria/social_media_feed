import graphene
from graphene_django import DjangoObjectType
from .models import Post, User, Comment, Like, Share


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email", "created_at")


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("id", "title", "content", "created_at", "user", "likes", "comments", "shares")

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ("id", "post", "user", "text", "created_at")

class LikeType(DjangoObjectType):
    class Meta:
        model = Like
        fields = ("id", "user", "post", "created_at")

class ShareType(DjangoObjectType):
    class Meta:
        model = Share
        fields = ("id", "user", "post", "shared_at")



class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    post_by_id = graphene.Field(PostType, id=graphene.Int(required=True))

    all_users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))

    all_comments = graphene.List(CommentType)
    comment_by_id = graphene.Field(CommentType, id=graphene.Int(required=True))

    all_likes = graphene.List(LikeType)
    like_by_id = graphene.Field(LikeType, id=graphene.Int(required=True))

    all_shares = graphene.List(ShareType)
    share_by_id = graphene.Field(ShareType, id=graphene.Int(required=True))

    def resolve_all_posts(root, info):
        return Post.objects.all()

    def resolve_post_by_id(root, info, id):
        return Post.objects.get(pk=id)
    
    
    def resolve_all_users(root, info):
        return User.objects.all()
    
    def resolve_user_by_id(root, info, id):
        return User.objects.get(pk=id)
    
    def resolve_all_comments(root, info):
        return Comment.objects.all()
    
    def resolve_comment_by_id(root, info, id):
        return Comment.objects.get(pk=id)
    
    def resolve_all_likes(root, info):
        return Like.objects.all()
    
    def resolve_like_by_id(root, info, id):
        return Like.objects.get(pk=id)
    
    def resolve_all_shares(root, info):
        return Share.objects.all()
    
    def resolve_share_by_id(root, info, id):
        return Share.objects.get(pk=id)

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(root, info, username, email, password):
        user = User.objects.create(username=username, email=email, password=password)
        return CreateUser(user=user)

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        user_id = graphene.Int(required=True)

    post = graphene.Field(PostType)

    def mutate(root, info, title, content, user_id):
        user = User.objects.get(pk=user_id)
        post = Post.objects.create(title=title, content=content, user=user)
        return CreatePost(post=post)


class CreateComment(graphene.Mutation):
    class Arguments:
        post_id = graphene.Int(required=True)
        user_id = graphene.Int(required=True)
        text = graphene.String(required=True)

    comment = graphene.Field(CommentType)

    def mutate(root, info, post_id, user_id, text):
        post = Post.objects.get(pk=post_id)
        user = User.objects.get(pk=user_id)
        comment = Comment.objects.create(post=post, user=user, text=text)
        return CreateComment(comment=comment)


class CreateLike(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)
        post_id = graphene.Int(required=True)
    
    like = graphene.Field(LikeType)
    
    def mutate(root, info, user_id, post_id):
        user = User.objects.get(pk=user_id)
        post = Post.objects.get(pk=post_id)
        like = Like.objects.create(user=user, post=post)
        return CreateLike(like=like)

class CreateShare(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)
        post_id = graphene.Int(required=True)
    
    share = graphene.Field(ShareType)
    
    def mutate(root, info, user_id, post_id):
        user = User.objects.get(pk=user_id)
        post = Post.objects.get(pk=post_id)
        share = Share.objects.create(user=user, post=post)
        return CreateShare(share=share)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    create_user = CreateUser.Field()
    create_comment = CreateComment.Field()
    create_like = CreateLike.Field()
    create_share = CreateShare.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)