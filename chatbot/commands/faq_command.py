from .base_command import Command

class FAQCommand(Command):
    def __init__(self, handler, question):
        self.handler = handler
        self.question = question

    def execute(self):
        return self.handler.get_response(self.question)