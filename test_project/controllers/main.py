from djangomini.controllers import Controller


class MainController(Controller):
    def get(self, request):
        return self.send('Home page rendered')
