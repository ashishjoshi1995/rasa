## happy path
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## bill_deferment
* bill_deferment
  - deferment_form
  - form{"name": "deferment_form"}
  - form{"name": null} 

## bill_redistribution
* bill_redistribution
  - bill_redistribution_form
  - form{"name": "bill_redistribution_form"}
  - form{"name": null} 
* affirm
  - utter_goodbye

## bill_redistribution
* bill_redistribution
  - bill_redistribution_form
  - form{"name": "bill_redistribution_form"}
  - form{"name": null} 
  - slot{"PHONENUM": 9756475739}
* deny
  - utter_iamabot

## online_charges_waived
* online_charges_waived
  - utter_customer_support_initiatives

## other covid queries
* other_covid_queries
  - utter_other_covid_queries

## are_you_servicing_customers - affirm - meter inspection
* are_you_servicing_customers
  - utter_are_you_servicing_customers
* affirm
  - utter_yes_to_book_request
* affirm
  - utter_bill_redistribution

## are_you_servicing_customers - affirm - movein
* are_you_servicing_customers
  - utter_are_you_servicing_customers
* affirm
  - utter_yes_to_book_request
* deny
  - utter_bill_redistribution


## are_you_servicing_customers - affirm - moveout
* are_you_servicing_customers
  - utter_are_you_servicing_customers
* affirm
  - utter_yes_to_book_request
* goodbye
  - utter_bill_redistribution

## are_you_servicing_customers - deny
* are_you_servicing_customers
  - utter_are_you_servicing_customers
* deny
  - utter_incorrect_bill

## safety_customer_fieldemployees
* safety_customer_fieldemployees
  - utter_safety_customer_fieldemployees

## regular_customer_services -1
* regular_customer_services
  - utter_regular_services
* pay_bill
  - pay_bill_form
  - form{"name": "pay_bill_form"}
  - form{"name": null} 
* affirm 
  - utter_payment_gateway

## regular_customer_services-2
* regular_customer_services
  - utter_regular_services
* pay_bill
  - pay_bill_form
  - form{"name": "pay_bill_form"}
  - form{"name": null} 
* deny 
  - utter_service_request_affirmation
* affirm
  - utter_under_development

## regular_customer_services-3
* regular_customer_services
  - utter_regular_services
* pay_bill
  - pay_bill_form
  - form{"name": "pay_bill_form"}
  - form{"name": null} 
* deny 
  - utter_service_request_affirmation
* deny
  - utter_what_else

## LATE PAYMENT
* late_payment
  - utter_late_payment

## CUSTOMER SUPPORT INITIATIVES
* customer_support_initiatives
  - utter_customer_support_initiatives

## HOW To PAY BILL ONLINE
* how_to_pay_bill_online
  - utter_how_to_pay_bill_online