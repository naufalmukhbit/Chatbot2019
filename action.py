import logging
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted, ConversationPaused

logger = logging.getLogger(__name__)

# class ActionTanam(Action):
#     def name(self):
#         return 'action_tanam'
#
#     def run(self, dispatcher, tracker, domain):
#         plant = tracker.get_slot('plant')
#
#         response = """cara nanem {} yagitu!""".format(plant)
#         dispatcher.utter_message(response)
#         return [SlotSet('plant', plant)]

class ActionTanamKangkungBotol(Action):
    def name(self):
        return 'action_tanam_kangkung_botol'

    def run(self, dispatcher, tracker, domain):
        plant = tracker.get_slot('plant')

        response = """cara nanem {} bisa dilihat di link https://bibitonline.com/artikel/cara-budidaya-kangkung-hidroponik-menggunakan-botol-bekas""".format(plant)
        dispatcher.utter_message(response)
        return [SlotSet('plant', plant)]

class ActionTanamSawiBotol(Action):
    def name(self):
        return 'action_tanam_sawi_botol'

    def run(self, dispatcher, tracker, domain):
        plant = tracker.get_slot('plant')

        response = """cara nanem {} bisa dilihat di link https://bibitonline.com/artikel/cara-menanam-sawi-hidroponik-dengan-botol-bekas""".format(plant)
        dispatcher.utter_message(response)
        return [SlotSet('plant', plant)]

class ActionTanamTomatBotol(Action):
    def name(self):
        return 'action_tanam_tomat_botol'

    def run(self, dispatcher, tracker, domain):
        plant = tracker.get_slot('plant')

        response = """cara nanem {} bisa dilihat di link http://hidroponikjurnal.blogspot.com/2017/03/menanam-tomat-secara-hidroponik-dalam.html""".format(plant)
        dispatcher.utter_message(response)
        return [SlotSet('plant', plant)]

class ActionTanamCabaiBotol(Action):
    def name(self):
        return 'action_tanam_cabai_botol'

    def run(self, dispatcher, tracker, domain):
        plant = tracker.get_slot('plant')

        response = """cara nanem {} bisa dilihat di link https://bibitonline.com/artikel/cara-menanam-cabe-hidroponik-dalam-botol-6-tahapan""".format(plant)
        dispatcher.utter_message(response)
        return [SlotSet('plant', plant)]

class ActionTanamKangkungPolybag(Action):
    def name(self):
        return 'action_tanam_kangkung_polybag'

    def run(self, dispatcher, tracker, domain):
        plant = tracker.get_slot('plant')

        response = """cara nanem {} bisa dilihat di link https://bibitbunga.com/cara-menanam-kangkung-cabut-dalam-pot-atau-polybag/""".format(plant)
        dispatcher.utter_message(response)
        return [SlotSet('plant', plant)]

class ActionTanamSawiPolybag(Action):
    def name(self):
        return 'action_tanam_sawi_polybag'

    def run(self, dispatcher, tracker, domain):
        plant = tracker.get_slot('plant')

        response = """cara nanem {} bisa dilihat di link https://www.kampustani.com/cara-menanam-sawi-di-polybag/""".format(plant)
        dispatcher.utter_message(response)
        return [SlotSet('plant', plant)]

class ActionTanamTomatPolybag(Action):
    def name(self):
        return 'action_tanam_tomat_polybag'

    def run(self, dispatcher, tracker, domain):
        plant = tracker.get_slot('plant')

        response = """cara nanem {} bisa dilihat di link https://bibitonline.com/artikel/cara-menanam-tomat-hidroponik-dalam-polybag-7-tahapan""".format(plant)
        dispatcher.utter_message(response)
        return [SlotSet('plant', plant)]

class ActionTanamCabaiPolybag(Action):
    def name(self):
        return 'action_tanam_cabai_polybag'

    def run(self, dispatcher, tracker, domain):
        plant = tracker.get_slot('plant')

        response = """cara nanem {} bisa dilihat di link https://bibitbunga.com/cara-menanam-cabe-hidroponik-menggunakan-polybag/""".format(plant)
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






