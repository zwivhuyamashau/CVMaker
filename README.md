# Resume Builder

A Python application that generates professional PDF resumes from JSON data using ReportLab.

## Features

- 🖥️ Generate clean, modern resume PDFs from structured JSON data
- 🎨 Customizable color scheme and styling
- 📄 Supports all standard resume sections:
  - Personal information with photo
  - Professional summary
  - Skills categorized by type
  - Education and certifications
  - Work experience with multiple positions
  - Project highlights
  - Professional references
- 📱 Mobile-friendly contact information display
- ✂️ Automatic section separation with accent colors

## Requirements

- Python 3.6+
- ReportLab library

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install reportlab
   ```

## Usage

1. Prepare your resume data in `resume_data.json` following the provided template
2. Place your profile photo in the specified path (optional)
3. Run the script:
   ```bash
   python resume_builder.py
   ```
4. Your PDF resume will be generated as `YOUR_NAME.pdf`

## Customization

Edit the `resume_data.json` file to include your information:

- **Personal Information**: Name, title, contact details
- **Style**: Choose colors (hex codes) for:
  - Primary text (`primary_color`)
  - Secondary text (`secondary_color`)
  - Accent elements (`accent_color`)
- **Content**: Fill in all relevant sections with your professional details

## JSON Structure

The resume builder expects JSON data with these sections:

```json
{
  "personal_info": {},
  "professional_summary": "",
  "skills": {},
  "education": [],
  "experience": [],
  "projects": [],
  "references": [],
  "style": {}
}
```

See the included `resume_data.json` for a complete example.

## Output Example

The generated PDF includes:

- Header with name, title, and contact information
- Professional summary
- Two-column layout with:
  - Left column: Skills and Education
  - Right column: Experience and Projects
- References section

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please open an issue or pull request for any improvements.
