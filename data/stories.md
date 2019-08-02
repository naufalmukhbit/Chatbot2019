## stories greet
* greet
   - utter_greet
   
## stories thanks
* thanks
   - utter_thanks

## stories tanya ulang
* accept
   - utter_tanya_lagi

## stories selesai
* enough
   - utter_thanks

## stories tanam tanpa plant & pot
* ask_tanam
   - utter_ask_plant
* inform_plant{"plant": "kangkung"}
   - slot{"plant": "kangkung"}
   - utter_ask_pot
* inform_pot{"pot": ""botol"}
   - slot{"pot": "botol"}
   - action_tanam
   
## stories tanam tanpa pot
* ask_tanam{"plant": "kangkung"}
    - slot{"plant": "kangkung"}
    - utter_ask_pot
* inform_pot{"pot": "botol"}
    - slot{"pot": "botol"}
    - action_tanam
    
## stories tanam
* ask_tanam{"plant": "tomat", "pot": "polybag"}
    - slot{"plant": "tomat"}
    - slot{"pot": "polybag"}
    - action_tanam
    
## stories siram tanpa plant
* ask_rawat_siram
    - utter_ask_plant
* inform_plant{"plant": "sawi"}
   - slot{"plant": "sawi"}
    - action_siram

## stories siram
* ask_rawat_siram{"plant": "cabai"}
    - slot{"plant": "cabai"}
    - action_siram
    
## stories pupuk tanpa plant
* ask_pupuk
    - utter_ask_plant
* inform_plant{"plant": "cabe"}
    - slot{"plant": "sawi"}
    - action_pupuk
    
## stories pupuk
* ask_pupuk{"plant": "cabe"}
    - slot{"plant": "cabe"}
    - action_pupuk
    
## stories ngaco
* ngaco
    - utter_ngaco
    