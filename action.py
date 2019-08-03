import logging
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted, ConversationPaused

logger = logging.getLogger(__name__)

class ActionTanam(Action):
    def name(self):
        return 'action_tanam'

    def run(self, dispatcher, tracker, domain):
        plant = tracker.get_slot('plant')
        pot = tracker.get_slot('pot')

        if plant == "kangkung":
            if pot == "botol":
                response = """Cara menanam {} dengan media {} bisa dilihat di link ini ya kak: https://bibitonline.com/artikel/cara-budidaya-kangkung-hidroponik-menggunakan-botol-bekas""".format(
                    plant, pot)
            else:
                response = """Cara menanam {} dengan media {} bisa dilihat di link ini ya kak: https://bibitbunga.com/cara-menanam-kangkung-cabut-dalam-pot-atau-polybag/""".format(
                    plant, pot)
        elif plant == "sawi":
            if pot == "botol":
                response = """Cara menanam {} dengan media {} bisa dilihat di link ini ya kak: https://bibitonline.com/artikel/cara-menanam-sawi-hidroponik-dengan-botol-bekas""".format(
                    plant, pot)
            else:
                response = """Cara menanam {} dengan media {} bisa dilihat di link ini ya kak: https://www.kampustani.com/cara-menanam-sawi-di-polybag/""".format(
                    plant, pot)
        elif plant == "tomat":
            if pot == "botol":
                response = """Cara menanam {} dengan media {} bisa dilihat di link ini ya kak: http://localhost/plantstore/index.php/Article/index/1""".format(
                    plant, pot)
            else:
                response = """Cara menanam {} dengan media {} bisa dilihat di link ini ya kak: http://localhost/plantstore/index.php/Article/index/2""".format(
                    plant, pot)
        elif plant == "cabai"  or plant == "cabe":
            if pot == "botol":
                response = """Cara menanam {} dengan media {} bisa dilihat di link ini ya kak: https://bibitonline.com/artikel/cara-menanam-cabe-hidroponik-dalam-botol-6-tahapan""".format(
                    plant, pot)
            else:
                response = """Cara menanam {} dengan media {} bisa dilihat di link ini ya kak: https://bibitbunga.com/cara-menanam-cabe-hidroponik-menggunakan-polybag/""".format(
                    plant, pot)
        else:
            response = """ Mohon maaf kak, untuk tanaman {} masih belum tersedia di layanan kami.""".format(plant)

        dispatcher.utter_message(response)
        return [SlotSet('plant', plant), SlotSet('pot',pot)]

class ActionSiram(Action):
    def name(self):
        return 'action_siram'

    def run(self, dispatcher, tracker, domain):
        plant = tracker.get_slot('plant')

        if plant == "kangkung":
            response = """Siram {} 1x tiap hari dengan campuran 1 liter air dan 7-9 ml nutrisi AB Mix.""".format(plant)
        elif plant == "sawi":
            response = """Siram {} 2x tiap hari pada saat pagi dan sore, tetapi jika dilihat masih dalam keadaan lembab, maka tidak perlu disiram lagi, kak.""".format(plant)
        elif plant == "tomat":
            response = """Untuk perawatan {}, kakak bisa menggunakan gembor manual atau selang fertilisasi. Disarankan menggunakan selang fertilisasi karena prosesnya akan lebih mudah.""".format(plant)
        elif plant == "cabai" or plant == "cabe":
            response = """Kakak bisa menyiram {} 1x tiap hari. Bisa juga ditambahkan nutrisi 5 ml nutrisi A + 5 ml nutrisi B dicampur dengan 1 liter air tiap 10 hari sekali""".format(plant)

        dispatcher.utter_message(response)
        return [SlotSet('plant', plant)]

class ActionPupuk(Action):
    def name(self):
        return 'action_pupuk'

    def run(self, dispatcher, tracker, domain):
        plant = tracker.get_slot('plant')

        if plant == "kangkung":
            response = """Pupuk untuk tanaman {} adalah pupuk hidroponik seperti AB Mix hidroponik sayur kak""".format(plant)
        elif plant == "sawi":
            response = """Pupuk yang cocok untuk tanaman {} adalah pupuk organik atau pupuk kandang""".format(plant)
        elif plant == "tomat":
            response = """Untuk tumbuhan {} gunakan pupuk kandang yang sudah didekomposisi dengan EM4 lalu dicmpur dengan PHONSKA dan SP36 dengan perbandingan 2:1""".format(plant)
        elif plant == "cabai" or plant == "cabe":
            response = """Pupuk yang cocok untuk tanaman {} adalah campuran tanah humus, arang sekam, dan pupuk kandang kering""".format(plant)

        dispatcher.utter_message(response)
        return [SlotSet('plant', plant)]

    # Step-by-step running program (jika sebelumnya sudah pernah melakukan step 1 dan 2, langsung skip ke step 3)
    # 1. pip install rasa_nlu[tensorflow]
    # 2. pip install rasa_core
    # 3. run nlu_model
    # 4. run train_rasacore
    # 5. masukkan code syntax dibawah ini di tab terminal yang berbeda
    #       python -m rasa_core_sdk.endpoint --actions action    <- this is bot's brain
    #       python -m rasa_core.run -d models/dialogue -u models/nlu/default/farm_nlu --port 5005 --endpoints endpoints.yml --credentials credentials.yml --cors "*"
    # 6. buka visual studio code untuk menggunakan perintah "yarn"
    #       yarn install (jika sebelumnya belum pernah melakukan ini)
    #       yarn watch
    #       yarn serve
    # 7. setelah itu buka localhost:8081/index.html kalau gabisa 8081, sesuaikan saja dengan yang ada di visual studio codenya
    # selamat mencoba :)

    #untuk generate story:
    # note: gunakan ini setelah menjalankan termilan bot's brain
    # python -m rasa_core.run -d models/dialogue -u models/nlu/default/farm_nlu --port 5005 --endpoints endpoints.yml --credentials credentials.yml
    # python -m rasa_core.train interactive -o models/dialogue -d farm_domain.yml -s data/stories.md --nlu models/nlu/default/farm_nlu --endpoints endpoints.yml

    # note:
    # CTRL+C for export chat, restart chat, etc.