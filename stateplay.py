import puppystate
import stateasleep

class StatePlay(puppystate.PuppyState):
    """Represents a puppy's playing state."""
    def feed(self, puppy):
        """Cannot feed because too busy playing"""
        return "Puppy is too busy playing with the ball to eat right now."
        
    def play(self, puppy):
        """Plays with the puppy."""
        puppy.inc_plays()
        if puppy._plays > 2:
            puppy.change_state(stateasleep.StateAsleep())
            puppy.reset()
            return "You throw the ball again. Puppy excitedly chases it.\nPuppy is tired and falls asleep."
        else:
            return "You throw the ball again. Puppy excitedly chases it."