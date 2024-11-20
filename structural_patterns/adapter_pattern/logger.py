from abc import abstractmethod, ABC


class OldLogService(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

class NewLogService:
    def log_message(self, message: str):
        print("New Log service: ", message)


class LogAdapter(OldLogService):

    def __init__(self, log_service: NewLogService):
        self.new_log_service = log_service

    def log(self, message):
        self.new_log_service.log_message(message)


new_log_service = NewLogService()
adapted_log_service = LogAdapter(new_log_service)
adapted_log_service.log("Hello World!")