from djangomini.controllers import Controller


class MainController(Controller):
    """Show main page of polls namespace."""

    def get(self):
        return self.html('Polls home page.')


class AddPollController(Controller):
    """Create new Poll object."""

    def get(self):
        return self.html('Create new poll (show form).')

    def post(self):
        return self.html('Create new poll (handle POST request).')


class ViewPollController(Controller):
    """Show one Poll object."""

    url_params = [':int']

    def get(self):
        return self.html('Show selected Poll object.')


class ViewPollsController(Controller):
    """Show list of Poll objects."""

    url_params = [':int', 'page', ':int']

    def get(self):
        return self.html('Show list of polls (with pagination).')
