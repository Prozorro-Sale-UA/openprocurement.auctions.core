from .models import Award
from .utils import add_next_award


class AwardingV1ConfiguratorMixin(object):
    """ Brings methods that are needed for the process of Awarding

        start_awarding - call after auction ends in auction view
        back_to_awarding - call when participant was disqualified
    """
    award_model = Award

    def start_awarding(self):
        """Using add_next_award method from belowThreshold procedure.
           
           add_next_award create 1 award and Awarding process start with
           1 award object
        """
        return add_next_award(self.request)

    def back_to_awarding(self):
        """ Call when we need to qualify another biddder.

            When award created at the first time has unsuccessful status
            add_next_award will create another one award object for another
            bidder
        """
        return add_next_award(self.request)