from django.http import HttpResponse


class GroupRequiredMixin:
    required_groups = ['writers']

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        if not request.user.is_authenticated:
            return HttpResponse('You have to be logged in!')
        if not request.user.groups:
            return HttpResponse(f'You have to be member of {self.required_groups}!')
        user_group_names = [g.name for g in request.user.groups.all()]
        result = set(user_group_names).intersection(self.required_groups)
        if self.required_groups and not result:
            return HttpResponse(f'You have to be member of {self.required_groups}!')

        return super().dispatch(request, *args, **kwargs)


