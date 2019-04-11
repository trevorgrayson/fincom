Feature: karate 'hello world' example
Scenario: create and retrieve a cat

Given url 'http://trevorgrayson.com/'
# And request { name: 'Billie' }
When method get
Then status 200
# And match response == { id: '#notnull', name: 'Billie' }

# Given path response.id
# When method get
# Then status 200
