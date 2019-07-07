import logging
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted, ConversationPaused

logger = logging.getLogger(__name__)

class ActionTanam(Action):
    def name(self):
        return 'action_tanam'

    def run(self, dispatcher, tracker, domain):
        plant = tracker.get_slot('plant')

        response = """ tanam {} tinggal tanam, goblog!""".format(plant)
        dispatcher.utter_message(response)
        return [SlotSet('plant', plant)]

    # Step-by-step running program
    # 1. pip install rasa_nlu[tensorflow]
    # 2. pip install rasa_core
    # 3. run nlu_model
    # 4. run train_rasacore
    # terminal code syntax
    # python -m rasa_core_sdk.endpoint --actions action    <- this is bot's brain
    # python -m rasa_core.run -d models/dialogue -u models/nlu/default/farm_nlu --port 5002 --endpoints endpoints.yml --credentials credentials.yml
    # python -m rasa_core.train interactive -o models/dialogue -d farm_domain.yml -s data/stories.md --nlu models/nlu/default/farm_nlu --endpoints endpoints.yml

    # note:
    # CTRL+C for export chat, restart chat, etc.






