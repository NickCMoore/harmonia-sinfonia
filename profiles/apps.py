from django.apps import AppConfig

class ProfilesConfig(AppConfig):
    """Configuration for the profiles app."""
    name = 'profiles'

    def ready(self):
        """Import profiles signals when the app is ready."""
        import profiles.signals
