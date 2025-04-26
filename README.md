
# CVMaker

**CVMaker** is an AI-powered resume generation tool that transforms structured JSON data into polished, job-specific resumes. Leveraging advanced language models like Claude 3.7 and AWS Bedrock, CVMaker streamlines the resume creation process, ensuring tailored and professional outputs.

## Features

- **Structured Resume Input**: Utilizes `resume.json` adhering to a defined `schema.json` for consistent data formatting.
- **Job Description Integration**: Incorporates specific job descriptions from `jobs.py` to tailor resumes accordingly.
- **AI-Powered Content Generation**: Employs Claude 3.7 via AWS Bedrock for generating and refining resume content.
- **HTML & PDF Output**: Converts generated resumes into HTML and subsequently into PDF format for easy sharing.
- **Modular Architecture**: Clean separation of concerns across modules like data fetching, HTML generation, and PDF conversion.

## Repository Structure

```
CVMaker/
├── get_job_post_and_user_data.py   # Generates resume data based on user info and job descriptions
├── html_to_pdf.py                  # Converts HTML resumes to PDF format
├── json_to_html.py                 # Transforms JSON resume data into HTML
├── jobs.py                         # Contains predefined job descriptions
├── orchastrate.py                  # Main orchestration script for the resume generation pipeline
├── resume.json                     # Sample resume data adhering to the defined schema
├── schema.json                     # JSON schema defining the structure of resume data
├── temp/                           # Temporary directory for intermediate files
├── pdfs/                           # Output directory for generated PDF resumes
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- AWS account with access to Bedrock and Claude 3.7
- Required Python packages (listed in `requirements.txt`)

### Installation

1. **Clone the repository**:

```bash
git clone https://github.com/zwivhuyamashau/CVMaker.git
cd CVMaker
```

2. **Configure AWS Credentials**:

Ensure your AWS credentials are set up, either via environment variables, AWS CLI configuration, or IAM roles, to access Bedrock and Claude 3.7.
3. **Setup your AWS IAM keys and model inference ID for claude sonnet v3.7 in your terminal**:

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
model_inference_Id = os.getenv('MODEL_INFERENCE_ID')
region_name = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')

### Usage

1. **Prepare Resume Data**:

Edit `resume.json` to include your personal and professional information. Ensure it adheres to the structure defined in `schema.json`.

2. **Select Job Description**:

Choose a job title from the predefined options in `jobs.py` or add your own.

3. **Run the Orchestration Script**:

```bash
python orchastrate.py
```

This script will:

- Generate tailored resume content using Claude 3.7.
- Convert the content into HTML format.
- Transform the HTML into a PDF file.
- Save the final PDF in the `pdfs/` directory.

## AWS Bedrock & Claude 3.7 Integration

CVMaker integrates with AWS Bedrock to utilize the capabilities of Claude 3.7 for advanced language processing.

1. **Access AWS Bedrock Console**:

   Navigate to the [AWS Bedrock Console](https://console.aws.amazon.com/bedrock/home).

2. **Model Access**:

   Ensure you have access to the Claude 3.7 model. If not, request access through the console.

3. **Set Up Permissions**:

   Configure necessary IAM roles and permissions to allow your application to invoke Claude 3.7 via Bedrock.


