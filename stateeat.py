import puppystate
import stateasleep
import stateplay

class StateEat(puppystate.PuppyState):
    """Represents a puppy's eating state"""
    def feed(self, puppy):
        """Feeds the puppy and changes its state to StateAsleep if sleep is greater than 2, otherwise StatePlay"""
        puppy.inc_feeds()
        if puppy._feeds > 2:
            puppy.change_state(stateasleep.StateAsleep())
            puppy.reset()
            return "The puppy continues to eat as you add another scoop of kibble to its bowl.\nThe puppy ate so much it fell asleep."
        else:
            return "The puppy continues to eat as you add another scoop of kibble to its bowl."

    def play(self, puppy):
        """Plays with the puppy and change its state to StatePlay"""
        puppy.change_state(stateplay.StatePlay())
        puppy.inc_plays()
        return "The puppy looks up from its food and chases the ball you threw."