from django.apps import AppConfig

import watson


class SearchConfig(AppConfig):

    name = 'search'
    verbose_name = 'Search'

    def ready(self):
        watson.register(self.get_model('JobsData'))