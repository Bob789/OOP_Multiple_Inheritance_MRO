# Multi-Channel Notification System
from idlelib.outwin import OutputWindow

from sms_notifier import SMSNotifier
from email_notifier import EmailNotifier
from console_notifier import ConsoleNotifier
from file_notifier import FileNotifier

# The inheritance order determines the MRO and the execution order
class AlertSystem(SMSNotifier, EmailNotifier, ConsoleNotifier, FileNotifier):
    def notify(self, message):
        print("[AlertSystem] Start Notification")
        super().notify(message)

print(AlertSystem.mro())  # View the actual execution sequence

system = AlertSystem()
system.notify("System failure detected!")

# Output
# [<class '__main__.AlertSystem'>, <class 'sms_notifier.SMSNotifier'>, <class 'email_notifier.EmailNotifier'>, <class 'console_notifier.ConsoleNotifier'>, <class 'file_notifier.FileNotifier'>, <class 'base_notifier.BaseNotifier'>, <class 'object'>]
# [AlertSystem] Start Notification
# [SMS] System failure detected!
# [Email] System failure detected!
# [Console] System failure detected!
# [File Log] System failure detected!
# [BaseNotifier] System failure detected!
