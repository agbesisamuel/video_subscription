from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "isk_video_subscription.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import isk_video_subscription.users.signals  # noqa F401
        except ImportError:
            pass
