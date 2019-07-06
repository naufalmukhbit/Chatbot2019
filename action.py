import logging
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted, ConversationPaused

logger = logging.getLogger(__name__)

class ActionTanam(Action):
    def name(self):
        return 'action_tanam'

    def run(self, dispatcher, tracker, domain):

        response = """ tanam tinggal tanam, goblog!""".format()
        dispatcher.utter_message(response)
        return [SlotSet('plant', plant)]


    # terminal code syntax
    # python -m rasa_core_sdk.endpoint --actions action    <- this is bot's brain
    # python -m rasa_core.run -d models/dialogue -u models/nlu/default/weather_nlu --port 5002 --endpoints endpoints.yml --credentials credentials.yml
    # python -m rasa_core.train interactive -o models/dialogue -d weather_domain.yml -s data/stories.md --nlu models/nlu/default/weather_nlu --endpoints endpoints.yml