# FE595Midterm

# Definition Endpoint
    To use this endpoint, send a post request containing json in thr format {"string": "your string here"}. The API will return json formatted results with defitions for each word in the string passed to it.
    
    
    
#Function commonwords(string)
    Takes in a string and will return the 5 most common words using value_counts() and a pandas dataframe.

#Function pluralize(string)
    Takes in a string and will return the plural words associated with each individual token in the string.

#Function singularize(string)
    Takes in a string and will return the singular words associated with each individual token in the string.
    
#Function translate(string) 
    Take in a string in English or any other language that is recognized by the Google API system underlying the function and then tranlslates that string to Spanish. 
    
