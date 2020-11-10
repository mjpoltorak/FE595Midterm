# FE595Midterm

# Definition Endpoint
    To use this endpoint, send a post request containing json in thr format {"string": "your string here"}. The API will return json formatted results with defitions for each word in the string passed to it.
    
#Function sentiment(string)
    Takes in a string and will return the negative, neutral, positive, and compound sentiment score using VADER sentiment
    
#Function commonwords(string)
    Takes in a string and will return the 5 most common words using value_counts() and a pandas dataframe.

#Function pluralize(string)
    Takes in a string and will return the plural words associated with each individual token in the string.

#Function singularize(string)
    Takes in a string and will return the singular words associated with each individual token in the string.
    
#Function sentences(string)
    Takes in a string with multiple sentences and will return a pandas dataframe with the sentences and their compound sentiment scores in order from most positive to least. 
