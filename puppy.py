import stateasleep

class Puppy():
  """
  A class representing a Puppy object.

  Attributes:
  - name (str): The name of the puppy.
  - age (int): The age of the puppy in months.

  Methods:
  - bark(): Makes the puppy bark.
  - wag_tail(): Makes the puppy wag its tail.
  - eat(food): Makes the puppy eat the specified food.
  - sleep(hours): Makes the puppy sleep for the specified number of hours.
  """
  def __init__(self):
    """ Initializes a new Puppy object."""
    self._state = stateasleep.StateAsleep()
    self._feeds = 0
    self._plays = 0

  def change_state(self, new_state):
    """Changes the state of the puppy to the specified state."""
    self._state = new_state

  def throw_ball(self):
    """Makes the puppy play with the ball."""
    return self._state.play(self)

  def give_food(self):
    """Makes the puppy eat the food."""
    return self._state.feed(self)

  def inc_feeds(self):
    """Increments the number of times the puppy has been fed."""
    self._feeds += 1

  def inc_plays(self):
    """Increments the number of times the puppy has been played with."""
    self._plays += 1

  def reset(self):
    """Resets the number of times the puppy has been fed and played with."""
    self._feeds = 0
    self._plays = 0