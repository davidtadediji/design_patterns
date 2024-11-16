class NotificationSubscriber:

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received log message: {message}")


class NotificationService:

    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber: NotificationSubscriber):
        self.subscribers.append(subscriber)

    def notify_subscribers(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

    def log(self, message):
        self.notify_subscribers(message)


notification_service = NotificationService()
notification_service.add_subscriber(NotificationSubscriber("David"))
notification_service.log("Hello World!")