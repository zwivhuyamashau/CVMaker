import json
from pathlib import Path
from get_job_post_and_user_data import generate_resume_data
from html_to_pdf import html_to_single_page_pdf
from json_to_html import generate_html_resume, generate_html_resume_neural
from jobs import JOB_DESCRIPTIONS
# Constants for file paths
BASE_DIR = Path.cwd()
RESUME_JSON = BASE_DIR / "resume.json"
SCHEMA_JSON = BASE_DIR / "schema.json"
OUTPUT_DIR = BASE_DIR / "temp"
PDF_DIR = BASE_DIR / "pdfs"
OUTPUT_DIR.mkdir(exist_ok=True)
PDF_DIR.mkdir(exist_ok=True)

def save_resume_to_json(resume_data: dict, output_path: Path) -> None:
    try:
        with output_path.open('w', encoding='utf-8') as f:
            json.dump(resume_data, f, indent=4, ensure_ascii=False)
        print(f"Successfully saved resume to {output_path}")
    except Exception as e:
        print(f"Failed to save resume to {output_path}: {str(e)}")
        raise

def sanitize_filename(name: str) -> str:
    """Remove or replace invalid filename characters"""
    return "".join(c if c.isalnum() or c in ('_', '-') else "_" for c in name)

def generate_resume_pipeline(job_dict: dict, candidate_data_path: Path, schema_path: Path) -> None:
    for job_title, job_text in job_dict.items():
        try:
            safe_title = sanitize_filename(job_title)

            # Prepare file paths for each job
            json_output = OUTPUT_DIR / f"{safe_title}_resume.json"
            html_output1 = OUTPUT_DIR / f"{safe_title}_resume_html1.html"
            pdf_output1 = PDF_DIR / f"{safe_title}_resume1.pdf"
            html_output3 = OUTPUT_DIR / f"{safe_title}_resume_html3.html"
            pdf_output3 = PDF_DIR / f"{safe_title}_resume3.pdf"

            print(f"\nProcessing job: {job_title}")

            # Step 1: Generate resume data
            resume_data = generate_resume_data(job_text, str(candidate_data_path), str(schema_path))

            # Step 2: Save to JSON
            save_resume_to_json(resume_data, json_output)

            # Step 3: Convert to HTML
            generate_html_resume(str(json_output), str(html_output1))
            generate_html_resume_neural(str(json_output), str(html_output3))

            # Step 4: Convert to PDF
            html_to_single_page_pdf(str(html_output1), str(pdf_output1))
            html_to_single_page_pdf(str(html_output3), str(pdf_output3))

            print(f"Resume generated for {job_title}: {pdf_output1}, {pdf_output3}")

        except Exception as e:
            print(f"Resume generation failed for {job_title}: {str(e)}")
            raise

if __name__ == "__main__":
    generate_resume_pipeline(JOB_DESCRIPTIONS, RESUME_JSON, SCHEMA_JSON)
