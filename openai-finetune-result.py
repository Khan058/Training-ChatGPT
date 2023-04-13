import subprocess

#Replace API KEY with your own API Key
job_id = 'API KEY'

# Run the command and capture the output
output = subprocess.check_output(['openai', 'api', 'fine_tunes.results', '-i', job_id])

# Decode the output from bytes to string
output_str = output.decode('utf-8')

# Write the output to a CSV file
with open('results.csv', 'w') as f:
    f.write(output_str)
