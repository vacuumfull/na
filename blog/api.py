"""Blog api."""
from blog.models import Blog, Comment, Rating


def get_rating(blog_id: int, user: object) -> dict:
    """Get blog rating."""
    result = Rating.objects.average(blog_id, user)
    return result


def vote_rating(blog_id: int, user: object, vote: int) -> dict:
    """Vote for blog post."""
    try:
        blog = Blog.objects.get(pk=blog_id)
        Rating.objects.update_or_create(
            blog=blog, user=user,
            defaults={'value': vote})
    except Blog.DoesNotExist:
        pass


def get_comment(blog_id: int, offset: int) -> dict:
    """Get blog rating."""
    result = Comment.objects.get_last_comments(blog_id, int(offset))
    return result
