from sisis_auth.models import SisisUser


def get_author_name(author):
    name = None
    author = SisisUser.objects.filter(email=author).first()
    if author.profile.name:
        name = author.profile.name
    else:
        idx = [c for c in author.email].index('@')
        name = author.email[:idx]
    return name


def get_author_bio(author):
    author = SisisUser.objects.filter(email=author).first()
    bio = author.profile.bio
    return bio
