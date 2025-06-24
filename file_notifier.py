from base_notifier import BaseNotifier

class FileNotifier(BaseNotifier):
    def notify(self, message):
        print(f"[File Log] {message}")
        super().notify(message)
