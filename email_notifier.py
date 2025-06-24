from base_notifier import BaseNotifier

class EmailNotifier(BaseNotifier):
    def notify(self, message):
        print(f"[Email] {message}")
        super().notify(message)
