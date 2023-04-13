# Import the OpenAI library
import openai

# Set your OpenAI API key
openai.api_key = "Replace this text with the AIP Key"

# Prompt the user for input and continue asking until a non-empty input is provided
while True:
    prompt = input("Please enter your prompt: ").strip()
    if len(prompt) > 0:
        break
    else:
        print("Error: Empty prompt is not allowed. Please enter a non-empty prompt.")
# Specify the model engine you want to use
model_engine = "davinci:ft-personal-2023-04-06-07-33-01"

# Define the maximum number of tokens to generate
max_tokens = 100

# Send a request to the OpenAI API to generate a completion using the specified parameters
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    n=1,  # Number of completions to generate for each prompt (in this case, generate only 1 completion)
    stop="END",  # The string that indicates when the generated text should stop (here, it stops when it encounters "END")
    temperature=0.7,  # Controls the creativity/randomness of the generated text (higher values = more random, lower values = more focused)
)

# Extract the generated text from the API response
generated_text = response.choices[0].text

# Print the generated text
print(generated_text)
