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
    
## Generated Story -2141674802246146226
* greet
    - utter_greet
* greet
    - utter_greet
* ask_tanam{"plant": "tomat"}
    - slot{"plant": "tomat"}
    - utter_ask_pot
* inform_pot{"pot": "polybag"}
    - slot{"pot": "polybag"}
    - action_tanam_tomat_polybag
    - slot{"plant": "tomat"}
* ask_rawat_siram{"plant": "tomat"}
    - slot{"plant": "tomat"}
    - utter_inform_siram_tomat
* thanks
    - utter_thanks

## Generated Story 8000925987041171606
* greet
    - utter_greet
* ask_tanam
    - utter_ask_plant
* inform_plant{"plant": "cabe"}
    - slot{"plant": "cabe"}
    - utter_ask_pot
* inform_pot{"pot": "gelas"}
    - slot{"pot": "gelas"}
    - utter_unclear
* inform_pot{"pot": "polybag"}
    - slot{"pot": "polybag"}
    - action_tanam_cabai_polybag
    - slot{"plant": "cabe"}
* accept
    - utter_tanya_lagi
* thanks
    - utter_thanks

