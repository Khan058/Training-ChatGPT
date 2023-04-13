# Define a function to calculate the total cost of token usage
def token_cost(tokens, cost_per_1ktoken, epochs):
    # Calculate the total number of tokens used
    total_tokens = tokens * epochs
    # Convert the total tokens to the number of thousands of tokens
    convert_for_cost = total_tokens/1000
    # Calculate the total cost based on the cost per 1k tokens
    total_cost = convert_for_cost * cost_per_1ktoken
    # Print the total cost
    print(total_cost)

#function to handle the prompt in case of wrong type of data
def get_float_input(prompt):
    while True:
        # Hnadling negative values
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive value.")
        #Handling values other than float or int
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Prompt user to enter the total number of tokens
token_number = get_float_input("Please enter the total number of tokens: ")
# Prompt user to enter the cost of the model per 1k tokens
model_cost = get_float_input("Please enter the cost of the model per 1k tokens: ")
# Prompt user to enter the number of epochs
epochs_number = get_float_input("Please enter the number of epochs: ")

# Call the token_cost function with the user inputs
token_cost(token_number, model_cost, epochs_number)
