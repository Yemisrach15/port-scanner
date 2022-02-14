from datetime import datetime

class TimeCounter:
    def start(self):
        self.startTime = datetime.now()
    
    def stop(self):
        self.stopTime = datetime.now()

    def total(self):
        return str(self.stopTime - self.startTime)