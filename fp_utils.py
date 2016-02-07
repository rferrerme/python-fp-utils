from multiprocessing import Pool

class Collection:
    """
    Helper to provide a natural Functional Programming approach in Python.
    """
    
    def __init__(self, val):
        self.val = val
        
    def apply(self, f):
        return Collection(f(self.val))
        
    def filter(self, f):
        return Collection(filter(f, self.val))
    
    def reduce(self, f, initial):
        return Collection(reduce(f, self.val, initial))
        
    def map(self, f):
        return Collection(map(f, self.val))
        
    def flatMap(self, f):
        return Collection([item for items in map(f, self.val) for item in items])

    def parallelMap(self, f, maxConcurrency=4):
        pool = Pool(processes=maxConcurrency)
        return Collection(pool.map(f, self.val))
        
    def forEach(self, f):
        for item in self.val:
            f(item)
        # To allow chaining
        return self
        
    def getValue(self):
        return self.val
        
    def __str__(self):
        return "Collection(%s)" % str(self.val)