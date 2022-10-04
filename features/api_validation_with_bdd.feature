#bdd feature and scenarios for validating API response for the endpoint https://cars-app.qxf2.com/cars 
#admin and non_admin credentials are taken from properties.ini through configurations.py (conf directory)
#feature scenarioss : 
#1. View existing cars list using GET method
#2. Add new car using POST method
#3. Update price_range of the added car using PUT method
#4. Delete the added car (by name) using DELETE method


Feature: validate the API responses for endpoint https://cars-app.qxf2.com/cars 
   
    #1. get response(cars list) from endpoint using GET method
    Scenario: View existing cars list using GET method and verify status code
    Given I am admin 
    When I make a GET call to url "https://cars-app.qxf2.com/cars"
    Then the response status code is "200"
    
    #2. add new car using POST method
    Scenario: Add new car using POST method and verify status code with added car details
    Given I am admin
    And payload to be added
       """
             {
                "name":"Punch",
                "brand":"Tata",
                "price_range":"12-18lacs",
                "car_type":"suv"
             }
        """
    When I make a POST call to url "https://cars-app.qxf2.com/cars/add" 
    And I make a GET call to url "https://cars-app.qxf2.com/cars/Punch"
    Then new car added successfully and the response status code is "200"
            
    #3. update car data(price_range) by name using PUT method 
    Scenario: Update car data(price_range) by name using PUT method and verify status code with updated car details
    Given I am admin
    And car name to be updated "Punch" and payload
      """
             {
                "name":"Punch",
                "brand":"Tata",
                "price_range":"10-13lacs",
                "car_type":"suv"
             }
        """
    When I make a PUT call to url "https://cars-app.qxf2.com/cars/update/"
    And I make a GET call to url "https://cars-app.qxf2.com/cars/Punch"
    Then car price_range of given car name is updated successfully with status code "200"
   

    #4. delete the added car by name using DELETE method
    Scenario: Delete the added car by name using DELETE method and verify status code 
    Given I am admin
    And car name to be deleted "Punch"
    When I make a DELETE call to url "https://cars-app.qxf2.com/cars/remove/"
    Then car with given name is deleted successfully with status code "200"

    