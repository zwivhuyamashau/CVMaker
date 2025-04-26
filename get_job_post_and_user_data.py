
import os
import json
import boto3

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
model_inference_Id = os.getenv('MODEL_INFERENCE_ID')
region_name = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')

bedrock = boto3.client(
        "bedrock-runtime",
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

def get_bedrock_response(question: str, max_tokens: int = 8000) -> str:
    # Prepare the body for the Bedrock model request
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": max_tokens,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": question
                    }
                ]
            }
        ]
    })
    accept = 'application/json'
    contentType = 'application/json'

    try:
        # Make the API call to Bedrock
        response = bedrock.invoke_model(
            body=body,
            modelId=model_inference_Id,
            accept=accept,
            contentType=contentType
        )

        # Read the response and extract the answer
        response_body = json.loads(response['body'].read())
        answer = response_body['content'][0]['text']  # Adjust based on actual response structure

        return answer

    except Exception as e:
        print(f"Error getting Bedrock response: {str(e)}")
        return "Error occurred while getting response."

# Constants
def generate_resume_data(job_text, candidate_data_path, schema_path):
    """Generate resume data from job description and candidate data."""
    with open(candidate_data_path, 'r') as file:
        candidate_data = json.load(file)
    with open(schema_path, 'r') as file:
        application_schema = json.load(file)
    separator = "\n" + "-" * 34 + "\n"
    prompt = (
        "Look at this job post below:" + separator + job_text + separator +
        "I want to apply for this role. Please give me a JSON response based on the schema below:" + 
        separator + str(application_schema) + separator +
        "Below is my work history. Make sure you highlight my strengths, work experience, and " +
        "tailor the language to the role I'm applying for. Include all the AWS tool builder, " +
        "systems dev engineer, cloud support engineer, Cloud Support Associate and CSIR roles. " +
        "Make sure to include all the AI projects that I worked on:" + 
        "Make sure to use my current Job Title, for example 'Systems development engineer'" + 
        "your response should only be the json file that has my user data"+
        separator + str(candidate_data) + separator
    )

    #response_string = get_groq_response_low(prompt)
    response_string = get_bedrock_response(prompt)

    # Extract JSON from response
    try:
        start_idx = response_string.find('{')
        end_idx = response_string.rfind('}')
        response_data = json.loads(response_string[start_idx:end_idx+1])
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Error parsing JSON: {e}")
        response_data = {}

    return response_data

