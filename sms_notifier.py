from base_notifier import BaseNotifier

class SMSNotifier(BaseNotifier):
    def notify(self, message):
        print(f"[SMS] {message}")
        super().notify(message)

