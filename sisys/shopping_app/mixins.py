from django.http import HttpResponse


def required_group(groups=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            group = None
            if not user.is_authenticated:
                return HttpResponse('You have to be logged in!')
            if user.is_superuser:
                return view_func(request, *args, **kwargs)
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in groups:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse(f'You have to be member of {groups}!')

        return wrapper

    return decorator
