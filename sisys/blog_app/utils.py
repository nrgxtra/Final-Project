from sisys.sisis_auth.models import SisisUser


def get_author_name(author):
    author = SisisUser.objects.filter(email=author).first()
    idx = [c for c in author.email].index('@')
    name = author.email[:idx]
    return name