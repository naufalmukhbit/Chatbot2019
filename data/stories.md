## stories 1
* greet
   - utter_greet
* ask_tanam
   - utter_ask_plant
* inform_plant{"plant": "kangkung"}
   - utter_ask_pot
* inform_pot{"pot": ""botol"}
   - action_tanam_kangkung_botol
* accept
   - utter_tanya_lagi
* enough
   - utter_thanks
   - export

## stories 2
* greet
   - utter_greet
* ask_tanam
   - utter_ask_plant
* inform_plant{"plant": "tomat"}
   - utter_ask_pot
* inform_pot{"pot": ""polybag"}
   - action_tanam_tomat_polybag
* thanks
   - utter_thanks
   - export

## Generated Story -7406484202332198290
* greet
    - utter_greet
* ask_tanam
    - utter_ask_plant
* inform_plant{"plant": "cabai"}
    - slot{"plant": "cabai"}
    - utter_ask_pot
* inform_pot{"pot": "polybag"}
    - slot{"pot": "polybag"}
    - action_tanam_cabai_polybag
    - slot{"plant": "cabai"}
* accept
    - utter_tanya_lagi
* thanks
    - utter_thanks