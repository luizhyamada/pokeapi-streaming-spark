from get_pokemon import pokemonApi

def lambda_handler(event, context):
    # Extract the endpoint from the event, or use a default
    endpoint = event.get("endpoint", "pokemon/pikachu")
    
    # Create an instance of the PokemonApi class
    api = pokemonApi(endpoint)
    
    # Get the data
    data = api.get_data()
    
    # Return the result
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }