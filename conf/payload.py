#create json payload 

#payload for POST method
def car_payload():
    car_json= {
                'name':'Punch',
                'brand':'Tata',
                'price_range':'12-18lacs',
                'car_type':'suv'
               }
    return car_json

#payload for PUT method
def update_car_payload():
    car_json= {
                'name':'Punch',
                'brand':'Tata',
                'price_range':'10-15lacs',
                'car_type':'suv'
               }
    return car_json
