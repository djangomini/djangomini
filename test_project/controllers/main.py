from djangomini.controllers import Controller


class MainController(Controller):
    def get(self):
        return self.html(template='main/main.html')
