from base_notifier import BaseNotifier

class ConsoleNotifier(BaseNotifier):
    def notify(self, message):
        print(f"[Console] {message}")
        super().notify(message)
