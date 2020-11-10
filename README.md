# FE595Midterm

# Sentiment Endpoint 
    To use this endpoint, send a post request containing json in the format {"string: "your string here"}. The API will return json formatted results with the negative, neutral, positive, and compound sentiment scores.

# Definition Endpoint
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return json formatted results with defitions for each word in the string passed to it.
    
# Subjectivity Endpoint
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return a subjectivity score of the string with 0 being very objective, and 1 being very subjective

# Noun Phrases Endpoint
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return all the noun phrases that are a part of the string

# Verbs Endpoint
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return all instances of verbs (past, present, gerund etc) from the string
    
# Commonwords Endpoint
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return a dataframe of the 5 most common words using value_counts

# Pluralize Endpoint
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return the return the plural words associated with each individual token 

# Singularize Endpoint
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return all the singular words associated with the indivual tokens in the string
    
# Sentences Endpoint
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return all the sentences in a pandas dataframe ranked from the highest compound sentiment score to the least compound sentiment score of each sentence. 
