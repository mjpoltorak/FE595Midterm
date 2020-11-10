# FE595Midterm

# Definition Endpoint
    To use this endpoint, send a post request containing json in thr format {"string": "your string here"}. The API will return json formatted results with defitions for each word in the string passed to it.
    
# Subjectivity Endpoint
    To use this endpoint, sned a post request containing json in the format {"string": "your string here"}. The API will return a subjectivity score of the string with 0 being very objective, and 1 being very subjective

# Noun Phrases Endpoint
    To use this endpoint, sned a post request containing json in the format {"string": "your string here"}. The API will return all the noun phrases that are a part of the string

# Verbs Endpoint
    To use this endpoint, sned a post request containing json in the format {"string": "your string here"}. The API will return all instances of verbs (past, present, gerund etc) from the string
    
# Commonwords
    To use this endpoint, sned a post request containing json in the format {"string": "your string here"}. The API will return a dataframe of the 5 most common words using value_counts

# Pluralize
    To use this endpoint, sned a post request containing json in the format {"string": "your string here"}. The API will return the return the plural words associated with each individual token 

# Singularize
    To use this endpoint, sned a post request containing json in the format {"string": "your string here"}. The API will return all the singular words associated with the indivual tokens in the string
    
