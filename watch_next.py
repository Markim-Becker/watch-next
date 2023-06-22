import spacy

def find_similar_movie(description, filename):
    nlp = spacy.load('en_core_web_md')

    # Load the movie descriptions from the file
    with open(filename, 'r') as file:
        movie_descriptions = file.readlines()

    # Remove newline characters from each description
    movie_descriptions = [desc.strip() for desc in movie_descriptions]

    # Calculate the similarity scores between the given description and each movie description
    similarities = [nlp(description).similarity(nlp(desc)) for desc in movie_descriptions]

    # Find the index of the most similar movie
    most_similar_index = similarities.index(max(similarities))

    # Retrieve the title of the most similar movie
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if i == most_similar_index:
                return line.strip()
    
    return None  # Return None if no similar movie is found

# Usage example
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
filename = "movies.txt" 

similar_movie = find_similar_movie(description, filename)
if similar_movie:
    print("Next movie recommendation:", similar_movie)
else:
    print("No similar movie found.")

# end
