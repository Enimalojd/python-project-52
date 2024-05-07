from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class CustomLoginRequiredMixin(LoginRequiredMixin):

    permission_denied_message = 'You are not logged in, please log in.'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR, self.permission_denied_message)
            return self.handle_no_permission()
        return super(CustomLoginRequiredMixin, self).dispatch(
            request, *args, **kwargs
        )