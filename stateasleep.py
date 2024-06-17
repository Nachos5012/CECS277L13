import puppystate
import stateeat

class StateAsleep(puppystate.PuppyState):
    """Represents the puppy's sleeping state."""
    def feed(self, puppy):
        """Feeds the puppy and changes its state to StateEat."""
        puppy.change_state(stateeat.StateEat())
        puppy.inc_feeds()
        return "The puppy wakes up and comes running to eat."

    def play(self, puppy):
        """Cannot play with the puppy because it is asleep"""
        return "Puppy is asleep and doesn't want to play."