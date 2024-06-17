import abc

class PuppyState(abc.ABC):
  """An abstract class representing the state of a puppy."""
  @abc.abstractmethod
  def feed(self, puppy):
    """Abstract method to make puppy eat"""
    pass

  @abc.abstractmethod
  def play(self, puppy):
    """Abstract method to make puppy play"""
    pass