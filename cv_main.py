from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os
import json

outputFileName = "YOUR_NAME.pdf"
jsonData = rf".\resume_data.json"

class ResumeBuilder:
    def __init__(self, json_file):
        self.load_data(json_file)
        self.setup_styles()
        
    def load_data(self, json_file):
        with open(json_file) as f:
            self.data = json.load(f)
        
    def setup_styles(self):
        self.styles = {
            'title': ParagraphStyle(
                'Title', fontSize=22, textColor=colors.HexColor(self.data['style']['primary_color']),
                fontName='Helvetica-Bold', alignment=1, spaceAfter=4, leading=24
            ),
            'subtitle': ParagraphStyle(
                'Subtitle', fontSize=12, textColor=colors.HexColor(self.data['style']['secondary_color']),
                fontName='Helvetica', alignment=1, spaceAfter=8
            ),
            'section_header': ParagraphStyle(
                'SectionHeader', fontSize=10, textColor=colors.HexColor(self.data['style']['primary_color']),
                fontName='Helvetica-Bold', spaceBefore=8, spaceAfter=6,
                borderLeftWidth=2, borderLeftColor=colors.HexColor(self.data['style']['accent_color']), 
                borderLeftPadding=4, alignment=1  # Added center alignment
            ),
            'body': ParagraphStyle(
                'Body', fontSize=9, textColor=colors.HexColor(self.data['style']['secondary_color']),
                fontName='Helvetica', leading=12, spaceAfter=2
            ),
            'body_bold': ParagraphStyle(
                'BodyBold', parent=ParagraphStyle('Body'),
                fontName='Helvetica-Bold'
            ),
            'centered_body': ParagraphStyle(
                'CenteredBody', parent=ParagraphStyle('Body'),
                alignment=1, spaceAfter=6
            ),
            'references': ParagraphStyle(
                'References', parent=ParagraphStyle('Body'),
                spaceBefore=6, spaceAfter=6,
                allowWidows=0, allowOrphans=0
            )
        }
        
    def create_section_separator(self):
        return [
            Spacer(1, 6),
            Table([[Paragraph(f'<hr width="100%" color="{self.data["style"]["accent_color"]}"/>')]], 
                 colWidths=['100%']),
            Spacer(1, 6)
        ]
        
    def create_header(self):
        header_content = []
        if os.path.exists(self.data['personal_info']['image_path']):
            header_content.append(
                Image(self.data['personal_info']['image_path'], 
                     1.2*inch, 1.2*inch, hAlign='CENTER')
            )
            header_content.append(Spacer(1, 0.2*inch))
        
        header_content += [
            Paragraph(self.data['personal_info']['name'], self.styles['title']),
            Paragraph(self.data['personal_info']['title'], self.styles['subtitle']),
            Table([
                [Paragraph(f"📍 {self.data['personal_info']['location']}", self.styles['centered_body']),
                 Paragraph(f"🇿🇦 {self.data['personal_info']['nationality']}", self.styles['centered_body'])],
                [Paragraph(f"📧 {self.data['personal_info']['email']}", self.styles['centered_body']),
                 Paragraph(f"📱 {self.data['personal_info']['phone']}", self.styles['centered_body'])],
                [Paragraph("", self.styles['centered_body']),
                 Paragraph("", self.styles['centered_body'])]
            ], colWidths=[3*inch, 3*inch], hAlign='CENTER'),
            Spacer(1, 0.2*inch)
        ]
        return header_content
        
    def create_skills_section(self):
        skills_content = []
        skills_content.append(Paragraph("KEY SKILLS", self.styles['section_header']))
        
        for category, items in self.data['skills'].items():
            icon = "☁️" if "Cloud" in category else "💻" if "Programming" in category else "🤖"
            skills_content.append(Paragraph(f"<b>{icon} {category}</b>", self.styles['body']))
            for item in items:
                skills_content.append(Paragraph(f"• {item}", self.styles['body']))
            skills_content.append(Spacer(1, 4))
            
        return skills_content
        
    def create_education_section(self):
        education_content = []
        education_content.append(Paragraph("EDUCATION & CERTIFICATIONS", self.styles['section_header']))
        
        for item in self.data['education']:
            if 'institution' in item:
                education_content.append(Paragraph(
                    f"• {item['degree']}",
                    self.styles['body']
                ))
                education_content.append(Paragraph(
                    f"<font color='{self.data['style']['accent_color']}'>  {item['institution']} ({item['year']})</font>",
                    self.styles['body']
                ))
            else:
                education_content.append(Paragraph(
                    f"• {item['degree']} ({item['year']})",
                    self.styles['body']
                ))
                
        return education_content
        
    def create_experience_section(self):
        experience_content = []
        experience_content.append(Paragraph("WORK EXPERIENCE", self.styles['section_header']))
        
        for company in self.data['experience']:
            experience_content.append(Paragraph(f"<b>{company['company']}</b>", self.styles['body']))
            for position in company['positions']:
                experience_content.append(Paragraph(
                    f"<font color={self.data['style']['accent_color']}>{position['title']} ({position['period']})</font>",
                    self.styles['body']
                ))
                for bullet in position['bullets']:
                    experience_content.append(Paragraph(bullet, self.styles['body']))
                experience_content.append(Spacer(1, 3))
                
        return experience_content
        
    def create_projects_section(self):
        projects_content = []
        projects_content.append(Paragraph("AI/ML PROJECTS", self.styles['section_header']))
        
        for project in self.data['projects']:
            projects_content.append(Paragraph(
                f"<font color={self.data['style']['accent_color']}>{project['title']}</font>",
                self.styles['body']
            ))
            for bullet in project['bullets']:
                projects_content.append(Paragraph(bullet, self.styles['body']))
            projects_content.append(Spacer(1, 3))
            
        return projects_content
        
    def create_references_section(self):
        ref_text = "Ref: " + " | ".join(
            [f"{ref['name']} ({ref['position']} at {ref['company']}) - {ref['contact']}" 
             for ref in self.data['references']]
        )
        return Paragraph(ref_text, self.styles['references'])
        
    def build_resume(self, output_file):
        doc = SimpleDocTemplate(
            output_file,
            pagesize=A4,
            rightMargin=0.3*inch,
            leftMargin=0.3*inch,
            topMargin=0.2*inch,
            bottomMargin=0.2*inch
        )
        
        story = []
        
        # Header
        story.extend(self.create_header())
        #story.extend(self.create_section_separator())
        
        # Professional Summary (centered header and bold text)
        story.append(Paragraph("PROFESSIONAL SUMMARY", self.styles['section_header']))
        story.append(Paragraph(f"<b>{self.data['professional_summary']}</b>", self.styles['body']))
        story.extend(self.create_section_separator())
        
        # Main Content
        left_col = []
        left_col.extend(self.create_skills_section())
        left_col.extend(self.create_section_separator())
        left_col.extend(self.create_education_section())
        left_col.extend(self.create_section_separator())
        
        right_col = []
        right_col.extend(self.create_experience_section())
        right_col.extend(self.create_section_separator())
        right_col.extend(self.create_projects_section())
        
        # Layout
        main_table = Table([[left_col, right_col]], 
                         colWidths=[2.8*inch, 4.4*inch],
                         style=[
                             ('VALIGN', (0,0), (-1,-1), 'TOP'),
                             ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                             ('PADDING', (0,0), (-1,-1), 2),
                             ('LINEAFTER', (0,0), (0,-1), 0.5, colors.HexColor(self.data['style']['accent_color']))
                         ])
        story.append(main_table)
        
        # References
        story.extend(self.create_section_separator())
        story.append(self.create_references_section())
        
        doc.build(story)

if __name__ == "__main__":
    builder = ResumeBuilder(jsonData)
    builder.build_resume(outputFileName)