from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic.edit import DeleteView
from django.db.models.deletion import ProtectedError


class CustomLoginRequiredMixin(LoginRequiredMixin):

    permission_denied_message = "You are not logged in, please log in."

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if not request.user.is_authenticated:
            messages.add_message(
                request, messages.ERROR, self.permission_denied_message
            )
            return self.handle_no_permission()
        return super(CustomLoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class MessageMixin:

    info_message = ""

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if self.info_message:
            messages.add_message(request, messages.INFO, self.info_message)
        return super().dispatch(request, *args, **kwargs)


class DeleteMixin(DeleteView):

    error_message = ""
    error_url = ""

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.error_message)
            return redirect(self.error_url)
