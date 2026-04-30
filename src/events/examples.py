from event_emitter import EventEmitter


print("Example 1: Multiple independent listeners\n")

events = EventEmitter()

def logger(message):
    print(f"Logger: {message}")

def notifier(message):
    print(f"Notifier: {message}")

def analyzer(message):
    print(f"Analyzer: {message}")

events.on('message', logger)
events.on('message', notifier)
events.on('message', analyzer)

events.emit('message', 'Hello World')
print()


print("Example 2: Chat system with user entities\n")

class User:
    def __init__(self, name, chat_emitter):
        self.name = name
        self.chat = chat_emitter
        self.chat.on('message', self.on_message)
    
    def on_message(self, sender, text):
        if sender != self.name:
            print(f"{self.name} received: '{text}' from {sender}")
    
    def send_message(self, text):
        print(f"{self.name} sends: '{text}'")
        self.chat.emit('message', self.name, text)


chat = EventEmitter()

alice = User('Alice', chat)
bob = User('Bob', chat)
charlie = User('Charlie', chat)

alice.send_message('Hi everyone!')
bob.send_message('Hello Alice!')
charlie.send_message('Hey there!')
print()


print("Example 3: System monitoring with multiple services\n")

class Logger:
    def __init__(self, system):
        system.on('error', self.log_error)
        system.on('warning', self.log_warning)
        system.on('info', self.log_info)
    
    def log_error(self, msg):
        print(f"Error log: {msg}")
    
    def log_warning(self, msg):
        print(f"Warning log: {msg}")
    
    def log_info(self, msg):
        print(f"Info log: {msg}")


class AlertService:
    def __init__(self, system):
        system.on('error', self.send_alert)
    
    def send_alert(self, msg):
        print(f"Alert sent: {msg}")


class MetricsCollector:
    def __init__(self, system):
        self.error_count = 0
        self.warning_count = 0
        system.on('error', self.count_error)
        system.on('warning', self.count_warning)
    
    def count_error(self, msg):
        self.error_count += 1
        print(f"Total errors: {self.error_count}")
    
    def count_warning(self, msg):
        self.warning_count += 1
        print(f"Total warnings: {self.warning_count}")


system = EventEmitter()

logger = Logger(system)
alerts = AlertService(system)
metrics = MetricsCollector(system)

print("Triggering warning:")
system.emit('warning', 'High memory usage')
print()

print("Triggering error:")
system.emit('error', 'Database connection failed')
print()

print("Triggering info:")
system.emit('info', 'Backup completed')
print()


print("Example 4: Subscribe and unsubscribe\n")

events4 = EventEmitter()

def handler1(data):
    print(f"Handler 1: {data}")

def handler2(data):
    print(f"Handler 2: {data}")

events4.on('update', handler1)
events4.on('update', handler2)

print("Both subscribed:")
events4.emit('update', 'First message')
print()

events4.off('update', handler1)

print("Handler 1 unsubscribed:")
events4.emit('update', 'Second message')