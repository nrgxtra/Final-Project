from django.shortcuts import redirect


class RedirectAfterRegistration:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile details')

        return super().dispatch(request, *args, **kwargs)
