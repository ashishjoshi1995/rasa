# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import sqlite3
from bill import BILL
from customer import CUSTOMER
from rasa_sdk.events import SlotSet
#
# class ActionHelloWorld(Action):
#
#    def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class DeferementForm(FormAction):
	def name(self) -> Text:
		return "deferment_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		return ["PHONENUM"]

	def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:
		dispatcher.utter_message(template="utter_submit")
		return []

	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
		return {"PHONENUM": self.from_entity(entity="PHONENUM", intent="my_phone_is"),}

class RedistributionPlanForm(FormAction):
	def name(self) -> Text:
		return "bill_redistribution_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		return ["PHONENUM"]

	def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:
		dispatcher.utter_message("Subscribers to a redistribution plan can forget paying their bill for 2 months. The credit amount will then be charged in equal fractions over the next four months in addition to the regular bill")
		conn = sqlite3.connect('tutorial.db')
		c = conn.cursor()
		print("Hello2")
		c.execute("SELECT * FROM CUSTOMERS WHERE (PHONENUM='"+tracker.get_slot("PHONENUM")+"')")
		customer_data = c.fetchall();
		print("Hello3")
		
		print(c)
		if(len(customer_data)==0):
			message = "Sorry! Did not find any account registered to this number. Please check the number, if you are new on out platform I can help you get started."
			print("Hello4")
		else:
			
			customer_data = CUSTOMER(customer_data[0][0],customer_data[0][1],customer_data[0][2],customer_data[0][3],customer_data[0][4])
			message = "Hi "+customer_data.FIRSTNAME+", please confirm your subscription to our bill redistribution program."
			SlotSet("NAME", customer_data.FIRSTNAME)
			print("Hello5")

		conn.commit()
		c.close()
		conn.close()
		dispatcher.utter_message(message)
		print("Hello6")
		return []

	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
		return {"PHONENUM": self.from_entity(entity="PHONENUM", intent="my_phone_is"),}

class PayBillForm(FormAction):
	def name(self) -> Text:
		return "pay_bill_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		return ["PHONENUM"]

	def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:
		conn = sqlite3.connect('tutorial.db')
		c = conn.cursor()
		
		c.execute("SELECT * FROM BILLS WHERE (PHONENUM='"+tracker.get_slot("PHONENUM")+"' AND BILL_STATUS = 'Pending')")
		bill_data = c.fetchall();

		if(len(bill_data)==0):
			message = "There is no unpaid bill pending"
		else:
			bill_object = BILL(bill_data[0][0], bill_data[0][1], bill_data[0][2], bill_data[0][3], bill_data[0][4], bill_data[0][5], bill_data[0][6], bill_data[0][7])
			message = "Hi "+bill_object.FIRSTNAME+", you have an unpaid bill of "+bill_object.BILLAMOUNT+" due by "+bill_object.PAYMENT_LAST_DATE+". Would you like to make payment?"
			SlotSet("NAME", bill_object.FIRSTNAME)
			SlotSet("METERREADING", bill_object.METERREADING)
			SlotSet("BILLAMOUNT",bill_object.BILLAMOUNT)
		c.execute("SELECT * FROM BILLS WHERE (PHONENUM='"+tracker.get_slot("PHONENUM")+"' AND BILL_STATUS = 'PAID')")
		print(c.fetchall())


		conn.commit()
		c.close()
		conn.close()
		dispatcher.utter_message(message)

		return []

	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
		return {"PHONENUM": self.from_entity(entity="PHONENUM", intent="my_phone_is"),}
