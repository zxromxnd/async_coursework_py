# Lab 7: Reactive Communication with EventEmitters

Event-driven communication system for reactive programming between entities.

## Task

Implement reactive message-based communication where entities react to and communicate through events.

## Features

- EventEmitter for publish-subscribe pattern
- Subscribe and unsubscribe functionality
- Multiple independent listeners per event
- Entity-to-entity communication through events

## Implementation

### EventEmitter Class

Main class for event-driven communication.

**Methods:**

- `on(event, listener)` - Subscribe to an event
- `off(event, listener)` - Unsubscribe from an event
- `emit(event, *args, **kwargs)` - Trigger event for all subscribers
- `listeners(event)` - Get all listeners for an event
- `remove_all_listeners(event)` - Remove all listeners

### Usage

**Basic subscription:**

```python
from event_emitter import EventEmitter

emitter = EventEmitter()

def handler(message):
    print(f"Received: {message}")

emitter.on('message', handler)
emitter.emit('message', 'Hello!')
```

**Multiple listeners:**

```python
emitter.on('update', listener1)
emitter.on('update', listener2)
emitter.on('update', listener3)

emitter.emit('update', 'Data changed')
```

**Entity communication:**

```python
class User:
    def __init__(self, name, chat):
        self.name = name
        chat.on('message', self.on_message)
    
    def on_message(self, sender, text):
        print(f"{self.name} received: {text}")

chat = EventEmitter()
user1 = User('Alice', chat)
user2 = User('Bob', chat)
```

**Unsubscribe:**

```python
emitter.off('update', listener1)
```

## Examples

Run all examples:

```bash
python lab7/examples.py
```

**Example 1:** Multiple independent listeners reacting to same event

**Example 2:** Chat system with user entities communicating

**Example 3:** System monitoring with multiple service entities

**Example 4:** Subscribe and unsubscribe demonstration

## Files

- `event_emitter.py` - EventEmitter implementation
- `examples.py` - Usage examples

## Requirements

- Python >= 3.8