# FE595Midterm

# Sentiment Endpoint (http://ec2-18-191-182-78.us-east-2.compute.amazonaws.com:8080/sentiment)
    To use this endpoint, send a post request containing json in the format {"string: "your string here"}. The API will return json formatted results with the negative, neutral, positive, and compound sentiment scores.

# Definition Endpoint (http://ec2-18-191-182-78.us-east-2.compute.amazonaws.com:8080/definition)
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return json formatted results with defitions for each word in the string passed to it.
    
# Subjectivity Endpoint (http://ec2-18-191-182-78.us-east-2.compute.amazonaws.com:8080/subjectivity)
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return a subjectivity score of the string with 0 being very objective, and 1 being very subjective

# Noun Endpoint (http://ec2-18-191-182-78.us-east-2.compute.amazonaws.com:8080/nouns)
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return all the nouns that are a part of the string

# Verbs Endpoint (http://ec2-18-191-182-78.us-east-2.compute.amazonaws.com:8080/verbs)
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return all instances of verbs (past, present, gerund etc) from the string
    
# Commonwords Endpoint (http://ec2-18-191-182-78.us-east-2.compute.amazonaws.com:8080/commonwords)
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return a dataframe of the 5 most common words using value_counts

# Pluralize Endpoint (http://ec2-18-191-182-78.us-east-2.compute.amazonaws.com:8080/pluralize)
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return the return the plural words associated with each individual token 

# Singularize Endpoint (http://ec2-18-191-182-78.us-east-2.compute.amazonaws.com:8080/singularize)
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return all the singular words associated with the individual tokens in the string
    

# Translate Endpoint (http://ec2-18-191-182-78.us-east-2.compute.amazonaws.com:8080/translate)
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return the string, which could be in English or any other recognized language, back in Spanish. 

# Sentences Endpoint (http://ec2-18-191-182-78.us-east-2.compute.amazonaws.com:8080/sentences)
    To use this endpoint, send a post request containing json in the format {"string": "your string here"}. The API will return all the sentences in a pandas dataframe ranked from the highest compound sentiment score to the least compound sentiment score of each sentence. 

