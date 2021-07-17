from abc import ABC, abstractmethod


class DescentFunction(ABC):
    def __init__(self):
        self.calls = 0

    @abstractmethod
    def run_once(self):
        pass

    @abstractmethod
    def run(self, func, x):
        pass

    @property
    def name(self):
        raise NotImplementedError

    # Это не надо трогать, оно работает
    def _increment_calls(func):
        def wraper(self):
            self.calls += 1
            return func(self)
        return wraper

    def reset_calls(self):
        self.calls = 0
