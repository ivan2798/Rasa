# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionCalculadoraNumeros(Action):
    def name(self) -> Text:
         return "action_calculadora_numeros"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #numeroA = next(tracker.get_latest_entity_values("numeroA"))
        #numeroB = next(tracker.get_latest_entity_values("numeroB"))
        signo = next(tracker.get_latest_entity_values("signo"))
        mensaje = str(signo) 
        #mensaje = "Probando"
        
        dispatcher.utter_message(text=mensaje)

        return []
    
    
