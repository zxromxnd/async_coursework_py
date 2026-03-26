class BiDirectionalPriorityQueue:
    def __init__(self):
        self.items = []
        self.counter = 0
    
    def enqueue(self, item, priority):
        self.items.append({
            'item': item,
            'priority': priority,
            'order': self.counter
        })
        self.counter += 1

    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self, highest=False, lowest=False, oldest=False, newest=False):
        if self.is_empty():
            return None
        
        if highest:
            max_item = max(self.items, key=lambda x: x['priority'])
            return max_item['item']
        
        elif lowest:
            min_item = min(self.items, key=lambda x: x['priority'])
            return min_item['item']
        
        elif oldest:
            min_order = min(self.items, key=lambda x: x['order'])
            return min_order['item']
        
        elif newest:
            max_order = max(self.items, key=lambda x: x['order'])
            return max_order['item']
        
        return None
    
    def dequeue(self, highest=False, lowest=False, oldest=False, newest=False):
        if self.is_empty():
            return None
        
        if highest:
            max_item = max(self.items, key=lambda x: x['priority'])
            self.items.remove(max_item)
            return max_item['item']
        
        elif lowest:
            min_item = min(self.items, key=lambda x: x['priority'])
            self.items.remove(min_item)
            return min_item['item']
        
        elif oldest:
            min_order = min(self.items, key=lambda x: x['order'])
            self.items.remove(min_order)
            return min_order['item']
        
        elif newest:
            max_order = max(self.items, key=lambda x: x['order'])
            self.items.remove(max_order)
            return max_order['item']
        
        return None