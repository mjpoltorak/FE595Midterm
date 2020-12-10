# FE595Midterm

# Process String Endpoint
    http://ec2-18-191-182-78.us-east-2.compute.amazonaws.com:8080/process_string
    All functions run through the "/process_string" endpoint (a POST) using valid JSON in the format: 
    {
        "string": "Test this string for our API",
        "methods": ["translate", "sentiment"]
    }
    where string is a string and methods is a list of strings containing the name of the supported methods (listed below)

# Help Endpoint
    http://ec2-18-191-182-78.us-east-2.compute.amazonaws.com:8080/help
    The help endpoint (a GET) explains how to use the API and how to send a post request with valid JSON


# Sentiment Function
    The function will return json formatted results with the negative, neutral, positive, and compound sentiment scores, as well as if the sentence is positive or negative overall.

# Definition Function 
    The function will return json formatted results with defitions for each word in the string passed to it.
    
# Subjectivity Function 
    The function will return a subjectivity score of the string with 0 being very objective, and 1 being very subjective

# Noun Function 
    The function will return all the nouns that are a part of the string

# Verbs Function 
    The function will return all instances of verbs (past, present, gerund etc) from the string
    
# Commonwords Function 
    The function will return a dataframe of the 5 most common words using value_counts

# Pluralize Function 
    The function will return the return the plural words associated with each individual token 

# Singularize Function
    The function will return all the singular words associated with the individual tokens in the string
    

# Translate Function 
    The function will return the string, which could be in English or any other recognized language, back in Spanish. 

# Sentences Function
    The function will return all the sentences in a pandas dataframe ranked from the highest compound sentiment score to the least compound sentiment score, as well as if the sentence is positive or negative overall. 

