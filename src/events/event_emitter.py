from typing import Callable, Dict, List


class EventEmitter:
    """
    Event-driven communication system.
    
    Allows entities to subscribe to events and react when events are emitted.
    """
    
    def __init__(self):
        """Initialize EventEmitter with empty listeners."""
        self._listeners: Dict[str, List[Callable]] = {}
    
    def on(self, event: str, listener: Callable):
        """
        Subscribe to an event.
        
        Args:
            event: Event name
            listener: Callback function to execute when event occurs
        """
        if event not in self._listeners:
            self._listeners[event] = []
        
        self._listeners[event].append(listener)
    
    def off(self, event: str, listener: Callable):
        """
        Unsubscribe from an event.
        
        Args:
            event: Event name
            listener: Callback function to remove
        """
        if event in self._listeners:
            if listener in self._listeners[event]:
                self._listeners[event].remove(listener)
    
    def emit(self, event: str, *args, **kwargs):
        """
        Emit an event to all subscribers.
    
        Args:
            event: Event name
            *args: Positional arguments for listeners
            **kwargs: Keyword arguments for listeners
        """
        if event in self._listeners:
            for listener in self._listeners[event]:
                try:
                    listener(*args, **kwargs)
                except Exception as e:
                    print(f"Error in listener: {e}")
    
    def listeners(self, event: str) -> List[Callable]:
        """
        Get all listeners for an event.
        
        Args:
            event: Event name
        
        Returns:
            List of listener functions
        """
        return self._listeners.get(event, [])
    
    def remove_all_listeners(self, event: str = None):
        """
        Remove all listeners for an event or all events.
        
        Args:
            event: Event name (if None, removes all listeners for all events)
        """
        if event is None:
            self._listeners.clear()
        elif event in self._listeners:
            del self._listeners[event]