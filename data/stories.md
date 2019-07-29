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

## Generated Story -7413301309735831225
* ask_tanam{"plant": "kangkung"}
    - slot{"plant": "kangkung"}
    - utter_ask_pot
* inform_pot{"pot": "botol"}
    - slot{"pot": "botol"}
    - action_tanam_kangkung_botol
    - slot{"plant": "kangkung"}
* accept
    - utter_tanya_lagi
* ask_pupuk{"plant": "kangkung"}
    - slot{"plant": "kangkung"}
    - utter_inform_pupuk_kangkung
* ask_rawat_siram
    - utter_inform_siram_kangkung
* thanks
    - utter_thanks

## Generated Story -6881391553361465932
* greet
    - utter_greet
* ask_tanam{"plant": "tomat", "pot": "polybag"}
    - slot{"plant": "tomat"}
    - slot{"pot": "polybag"}
    - action_tanam_tomat_polybag
    - slot{"plant": "tomat"}
* ask_rawat_siram
    - utter_inform_siram_tomat
* ask_pupuk{"plant": "sawi"}
    - slot{"plant": "sawi"}
    - utter_inform_pupuk_sawi
* thanks
    - utter_thanks

## Generated Story -8866655433732480588
* ask_pupuk{"plant": "cabai"}
    - slot{"plant": "cabai"}
    - utter_inform_pupuk_cabai
* thanks
    - utter_thanks

## Generated Story -1134435891935060116
* ask_rawat_siram{"plant": "tomat"}
    - slot{"plant": "tomat"}
    - utter_inform_siram_tomat
* thanks
    - utter_thanks

## Generated Story -7555723523148744974
* greet
    - utter_greet
* ask_tanam{"plant": "cabai", "pot": "botol"}
    - slot{"plant": "cabai"}
    - slot{"pot": "botol"}
    - action_tanam_cabai_botol
    - slot{"plant": "cabai"}
* thanks
    - utter_thanks

