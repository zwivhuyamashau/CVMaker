import json
from datetime import datetime

def generate_html_resume(json_file_path, output_file_path='resume.html'):
    # Load JSON data
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    
    # Get current year for footer
    current_year = datetime.now().year
    
    # Generate HTML content
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['personal_info']['name']} | {data['personal_info']['title']}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.0.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/firacode@6.2.0/distr/fira_code.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700&display=swap');
        
        :root {{
            --neon-cyan: #0ff;
            --neon-magenta: #f0f;
            --neon-green: #0f8;
            --dark-bg: #0a0a12;
            --cyberpunk-yellow: #f8ef02;
            --terminal-green: #00ff41;
        }}
        
        body {{
            background-color: var(--dark-bg);
            color: #e0e0e0;
            font-family: 'Fira Code', monospace;
            padding: 0;
            margin: 0;
            position: relative;
            overflow-x: hidden;
        }}
        
        body::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                linear-gradient(0deg, transparent 97%, rgba(0, 255, 255, 0.1) 98%, transparent 100%),
                linear-gradient(90deg, transparent 97%, rgba(0, 255, 255, 0.1) 98%, transparent 100%);
            background-size: 3em 3em;
            z-index: -1;
            opacity: 0.2;
        }}
        
        .matrix-bg {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0.03;
            z-index: -2;
            background-image: url('https://cdn.jsdelivr.net/gh/StephenOrJames/neural-network-animation@1.0.0/dist/neural-network-animation.min.svg');
            background-size: cover;
        }}
        
        .container {{
            max-width: 1200px;
            min-height: 100vh;
        }}
        
        .orbitron {{
            font-family: 'Orbitron', sans-serif;
        }}
        
        .terminal-header {{
            font-family: 'Fira Code', monospace;
            color: var(--terminal-green);
            position: relative;
            padding-left: 1.5rem;
        }}
        
        .terminal-header::before {{
            content: ">";
            position: absolute;
            left: 0;
            color: var(--neon-cyan);
        }}
        
        .neon-border {{
            border: 1px solid rgba(0, 255, 191, 0.3);
            box-shadow: 0 0 10px rgba(0, 255, 191, 0.2);
        }}
        
        .neon-text-cyan {{
            color: var(--neon-cyan);
            text-shadow: 0 0 5px rgba(0, 255, 255, 0.7);
        }}
        
        .neon-text-magenta {{
            color: var(--neon-magenta);
            text-shadow: 0 0 5px rgba(255, 0, 255, 0.7);
        }}
        
        .neon-text-green {{
            color: var(--neon-green);
            text-shadow: 0 0 5px rgba(0, 255, 136, 0.7);
        }}
        
        .neon-text-yellow {{
            color: var(--cyberpunk-yellow);
            text-shadow: 0 0 5px rgba(248, 239, 2, 0.7);
        }}
        
        .glitch {{
            position: relative;
        }}
        
        .glitch::before, .glitch::after {{
            content: attr(data-text);
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }}
        
        .glitch::before {{
            left: 2px;
            text-shadow: -1px 0 var(--neon-magenta);
            animation: glitch-anim-1 2s infinite linear alternate-reverse;
            clip: rect(44px, 450px, 56px, 0);
        }}
        
        .glitch::after {{
            left: -2px;
            text-shadow: -1px 0 var(--neon-cyan);
            animation: glitch-anim-2 3s infinite linear alternate-reverse;
            clip: rect(44px, 450px, 46px, 0);
        }}
        
        .progress-bar {{
            height: 4px;
            border-radius: 2px;
            background: linear-gradient(90deg, var(--neon-cyan), var(--neon-magenta));
            box-shadow: 0 0 8px var(--neon-cyan);
        }}
        
        .skill-percent-90 {{ width: 90%; }}
        .skill-percent-85 {{ width: 85%; }}
        .skill-percent-80 {{ width: 80%; }}
        .skill-percent-75 {{ width: 75%; }}
        
        .cyber-box {{
            background-color: rgba(10, 10, 18, 0.7);
            border: 1px solid rgba(0, 255, 191, 0.3);
            box-shadow: 0 0 10px rgba(0, 255, 191, 0.2);
            backdrop-filter: blur(5px);
        }}
        
        .cyber-box::before {{
            content: "";
            position: absolute;
            top: -2px;
            left: -2px;
            width: 0;
            height: 0;
            border-top: 10px solid var(--neon-cyan);
            border-right: 10px solid transparent;
        }}
        
        .cyber-box::after {{
            content: "";
            position: absolute;
            bottom: -2px;
            right: -2px;
            width: 0;
            height: 0;
            border-bottom: 10px solid var(--neon-cyan);
            border-left: 10px solid transparent;
        }}
        
        .cyber-line {{
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--neon-cyan), transparent);
        }}

        .cyber-timeline-connector {{
            width: 1px;
            background: linear-gradient(180deg, var(--neon-cyan), var(--neon-magenta));
            position: absolute;
            left: 20px;
            top: 25px;
            bottom: 0;
        }}
        
        .timeline-item {{
            position: relative;
            padding-left: 40px;
        }}
        
        .timeline-dot {{
            position: absolute;
            left: 16px;
            top: 6px;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background-color: var(--neon-cyan);
            box-shadow: 0 0 10px var(--neon-cyan);
            z-index: 1;
        }}
        
        @keyframes glitch-anim-1 {{
            0% {{ clip: rect(30px, 9999px, 10px, 0); }}
            20% {{ clip: rect(50px, 9999px, 30px, 0); }}
            40% {{ clip: rect(70px, 9999px, 50px, 0); }}
            60% {{ clip: rect(90px, 9999px, 70px, 0); }}
            80% {{ clip: rect(110px, 9999px, 90px, 0); }}
            100% {{ clip: rect(130px, 9999px, 110px, 0); }}
        }}
        
        @keyframes glitch-anim-2 {{
            0% {{ clip: rect(15px, 9999px, 5px, 0); }}
            20% {{ clip: rect(35px, 9999px, 25px, 0); }}
            40% {{ clip: rect(55px, 9999px, 45px, 0); }}
            60% {{ clip: rect(75px, 9999px, 65px, 0); }}
            80% {{ clip: rect(95px, 9999px, 85px, 0); }}
            100% {{ clip: rect(115px, 9999px, 105px, 0); }}
        }}
        
        @keyframes blink {{
            0%, 49% {{ opacity: 1; }}
            50%, 100% {{ opacity: 0; }}
        }}
        
        .cursor-blink::after {{
            content: "|";
            animation: blink 1s infinite;
            color: var(--neon-cyan);
        }}
    </style>
</head>
<body>
    <div class="matrix-bg"></div>
    <div class="container mx-auto px-4 py-8">
        <!-- Header Section -->
        <header class="mb-8">
            <div class="flex flex-col md:flex-row items-start md:items-end justify-between">
                <div>
                    <h1 class="orbitron text-4xl md:text-5xl font-bold mb-2 glitch neon-text-cyan" data-text="{data['personal_info']['name'].upper()}">{data['personal_info']['name'].upper()}</h1>
                    <h2 class="text-xl md:text-2xl neon-text-green mb-4 cursor-blink">{data['personal_info']['title'].upper()}</h2>
                </div>
                <div class="cyber-box p-4 relative mt-4 md:mt-0">
                    <div class="flex flex-col space-y-2">
                        <div class="flex items-center">
                            <i class="fas fa-map-marker-alt mr-3 neon-text-cyan"></i>
                            <span>{data['personal_info']['location']}</span>
                        </div>
                        <div class="flex items-center">
                            <i class="fas fa-envelope mr-3 neon-text-cyan"></i>
                            <span>{data['personal_info']['email']}</span>
                        </div>
                        <div class="flex items-center">
                            <i class="fas fa-flag mr-3 neon-text-cyan"></i>
                            <span>{data['personal_info']['citizenship']}</span>
                        </div>
                        <div class="flex items-center">
                            <i class="fas fa-phone mr-3 neon-text-cyan"></i>
                            <span>{data['personal_info']['phone']}</span>
                        </div>
                                                <div class="flex items-center">
                            <i class="fas fa-envelope mr-3 neon-text-cyan"></i>
                            <span>{data['personal_info']['github']}</span>
                        </div>
                    </div>
                </div>
            </div>
        </header>

        <!-- Professional Summary Section -->
        <section class="mb-8">
            <h3 class="terminal-header text-xl mb-4">PROFESSIONAL_SUMMARY</h3>
            <div class="cyber-box p-4 relative">
                <p class="text-sm md:text-base leading-relaxed">
                    {data['professional_summary']}
                </p>
            </div>
        </section>

        <!-- Skills Section -->
        <section class="mb-8">
            <h3 class="terminal-header text-xl mb-4">KEY_SKILLS</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Programming Languages -->
                <div class="cyber-box p-4 relative">
                    <h4 class="orbitron text-lg mb-4 neon-text-yellow">PROGRAMMING_LANGUAGES</h4>
                    <div class="space-y-4">
    """

    # Add programming languages with progress bars
    for lang in data['skills']['programming_languages']:
        percent = lang.get('proficiency').replace('%', '')
        html_content += f"""
                        <div>
                            <div class="flex justify-between mb-1">
                                <span>{lang['name']}</span>
                                <span class="neon-text-cyan">{lang.get('proficiency')}</span>
                            </div>
                            <div class="w-full bg-gray-800 rounded-full h-1">
                                <div class="progress-bar skill-percent-{percent}"></div>
                            </div>
                        </div>
        """

    html_content += f"""
                    </div>
                </div>

                <!-- Cloud Technologies -->
                <div class="cyber-box p-4 relative">
                    <h4 class="orbitron text-lg mb-4 neon-text-yellow">CLOUD_TECHNOLOGIES</h4>
                    <div class="grid grid-cols-2 gap-2 text-sm">
    """

    # Add cloud technologies
    for tech in data['skills']['cloud_technologies']:
        html_content += f"""
                        <div class="flex items-center"><i class="fas fa-check neon-text-cyan mr-2"></i>{tech}</div>
        """

    html_content += f"""
                    </div>
                </div>

                <!-- AI/ML -->
                <div class="cyber-box p-4 relative">
                    <h4 class="orbitron text-lg mb-4 neon-text-yellow">AI/ML</h4>
                    <div class="grid grid-cols-2 gap-2 text-sm">
    """

    # Add AI/ML skills
    for ai_skill in data['skills']['ai_ml']:
        html_content += f"""
                        <div class="flex items-center"><i class="fas fa-robot neon-text-magenta mr-2"></i>{ai_skill}</div>
        """

    html_content += f"""
                    </div>
                </div>

                <!-- DevOps -->
                <div class="cyber-box p-4 relative">
                    <h4 class="orbitron text-lg mb-4 neon-text-yellow">DEV_OPS</h4>
                    <div class="grid grid-cols-2 gap-2 text-sm">
    """

    # Add DevOps skills
    for devops_skill in data['skills']['devops']:
        html_content += f"""
                        <div class="flex items-center"><i class="fas fa-cogs neon-text-green mr-2"></i>{devops_skill}</div>
        """

    html_content += f"""
                    </div>
                </div>
            </div>
        </section>

        <!-- Experience Section -->
        <section class="mb-8">
            <h3 class="terminal-header text-xl mb-4">WORK_EXPERIENCE</h3>
            <div class="cyber-box p-4 relative">
                <div class="relative">
                    <div class="cyber-timeline-connector"></div>
    """

    # Add work experience
    for exp in data['work_experience']:
        html_content += f"""
                    <!-- {exp['company']} -->
                    <div class="timeline-item mb-6">
                        <div class="timeline-dot"></div>
                        <h4 class="orbitron text-lg neon-text-yellow mb-2">{exp['company']}</h4>
                        <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-2">
                            <h5 class="font-bold neon-text-cyan">{exp['position']}</h5>
                            <span class="text-sm text-gray-400">{exp['period']}</span>
                        </div>
                        <ul class="list-none space-y-2">
        """

        for responsibility in exp['responsibilities']:
            html_content += f"""
                            <li class="flex items-start">
                                <i class="fas fa-angle-right neon-text-green mt-1 mr-2"></i>
                                <span>{responsibility}</span>
                            </li>
            """

        html_content += """
                        </ul>
                    </div>
        """

    html_content += f"""
                </div>
            </div>
        </section>

        <!-- Two Column Layout for Projects and Education -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
            <!-- Projects Section -->
            <section>
                <h3 class="terminal-header text-xl mb-4">AI/ML_PROJECTS</h3>
                <div class="space-y-4">
    """

    # Add projects
    for project in data['projects']:
        html_content += f"""
                    <div class="cyber-box p-4 relative">
                        <h4 class="orbitron text-lg neon-text-yellow mb-2">{project['name']}</h4>
                        <p class="text-sm mb-2">
                            {project['description']}
                        </p>
                        <div class="flex space-x-2">
        """

        for tech in project['technologies']:
            color_class = "neon-text-cyan"
            if "Stable" in tech or "LLM" in tech:
                color_class = "neon-text-magenta"
            elif "RAG" in tech or "LangChain" in tech:
                color_class = "neon-text-green"
                
            html_content += f"""
                            <span class="bg-gray-800 text-xs px-2 py-1 rounded {color_class}">{tech}</span>
            """

        html_content += """
                        </div>
                    </div>
        """

    html_content += f"""
                </div>
            </section>

            <!-- Education Section -->
            <section>
                <h3 class="terminal-header text-xl mb-4">EDUCATION & CERTIFICATIONS</h3>
                <div class="cyber-box p-4 relative mb-4">
    """

    # Add education
    for edu in data['education']:
        html_content += f"""
                    <div class="mb-4">
                        <div class="flex items-center mb-1">
                            <i class="fas fa-graduation-cap neon-text-yellow mr-2"></i>
                            <h4 class="orbitron text-lg neon-text-yellow">{edu['degree']}</h4>
                        </div>
                        <p class="text-gray-400 text-sm">{edu['year']}</p>
                    </div>
        """

    # Add certifications
    for cert in data['certifications']:
        html_content += f"""
                    <div class="mb-4">
                        <div class="flex items-center mb-1">
                            <i class="fas fa-certificate neon-text-cyan mr-2"></i>
                            <h4 class="text-lg">{cert['name']}</h4>
                        </div>
                        <p class="text-gray-400 text-sm">{cert['year']}</p>
                    </div>
        """

    html_content += f"""
                </div>

                <!-- References Section -->
                <h3 class="terminal-header text-xl mb-4">REFERENCES</h3>
                <div class="cyber-box p-4 relative">
    """

    # Add references
    for i, ref in enumerate(data['references']):
        html_content += f"""
                    <div class="{'mb-4' if i < len(data['references']) - 1 else ''}">
                        <h4 class="orbitron text-lg neon-text-yellow mb-1">{ref['name']}</h4>
                        <p class="text-sm mb-1">{ref['position']}</p>
                        <div class="flex items-center">
                            <i class="fas fa-phone mr-2 neon-text-cyan"></i>
                            <span>{ref['phone']}</span>
                        </div>
                    </div>
        """

    html_content += f"""
                </div>
            </section>
        </div>

        <!-- Footer -->
        <footer class="mt-8 mb-4">
            <div class="cyber-line mb-4"></div>
            <div class="text-center text-xs text-gray-500">
                <p class="mb-2 neon-text-cyan">KERNEL VERSION 2.1.0</p>
                <p class="terminal-header">[EOF] // End of File</p>
            </div>
        </footer>
    </div>
</body>
</html>
    """

    # Write to output file
    with open(output_file_path, 'w') as f:
        f.write(html_content)
    
    print(f"Resume generated successfully at {output_file_path}")

def generate_html_resume2(json_file_path, output_file_path='resume.html'):
    # Load JSON data
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    
    # Generate HTML content
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['personal_info']['name']} | {data['personal_info']['title']}</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --neon-green: #39ff14;
            --neon-blue: #1e90ff;
            --neon-cyan: #00ffff;
            --dark-bg: #0a0a0a;
            --terminal-bg: #121212;
        }}
        
        body, html {{
            background-color: var(--dark-bg);
            color: #f0f0f0;
            font-family: 'Rajdhani', sans-serif;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
            position: relative;
        }}
        
        .matrix-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            opacity: 0.15;
        }}
        
        .container {{
            position: relative;
            z-index: 1;
        }}
        
        .tech-mono {{
            font-family: 'Share Tech Mono', monospace;
        }}
        
        .neon-text {{
            text-shadow: 0 0 5px var(--neon-green), 0 0 10px var(--neon-green), 0 0 15px var(--neon-green);
            color: var(--neon-green);
        }}
        
        .neon-blue {{
            text-shadow: 0 0 5px var(--neon-blue), 0 0 10px var(--neon-blue);
            color: var(--neon-blue);
        }}
        
        .neon-cyan {{
            text-shadow: 0 0 5px var(--neon-cyan), 0 0 10px var(--neon-cyan);
            color: var(--neon-cyan);
        }}
        
        .terminal {{
            background-color: var(--terminal-bg);
            border: 1px solid var(--neon-green);
            border-radius: 4px;
            padding: 15px;
            position: relative;
            margin-bottom: 20px;
            box-shadow: 0 0 10px rgba(57, 255, 20, 0.2);
        }}
        
        .terminal::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 25px;
            background-color: rgba(57, 255, 20, 0.1);
            border-bottom: 1px solid var(--neon-green);
            border-radius: 4px 4px 0 0;
        }}
        
        .terminal-header {{
            position: relative;
            height: 25px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            padding-left: 10px;
            z-index: 1;
        }}
        
        .terminal-dots {{
            display: flex;
            gap: 5px;
        }}
        
        .terminal-dot {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
        }}
        
        .skill-badge {{
            background-color: rgba(57, 255, 20, 0.1);
            border: 1px solid var(--neon-green);
            border-radius: 4px;
            padding: 5px 10px;
            margin: 3px;
            display: inline-block;
            transition: all 0.3s ease;
        }}
        
        .skill-badge:hover {{
            background-color: rgba(57, 255, 20, 0.2);
            box-shadow: 0 0 10px var(--neon-green);
            transform: translateY(-2px);
        }}
        
        .skill-category {{
            border-left: 3px solid var(--neon-green);
            padding-left: 10px;
            margin-bottom: 15px;
        }}
        
        .timeline-item {{
            position: relative;
            padding-left: 30px;
            margin-bottom: 30px;
        }}
        
        .timeline-item::before {{
            content: "";
            position: absolute;
            left: 0;
            top: 5px;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background-color: var(--neon-green);
            box-shadow: 0 0 10px var(--neon-green);
        }}
        
        .timeline-item::after {{
            content: "";
            position: absolute;
            left: 5px;
            top: 15px;
            width: 2px;
            height: calc(100% + 15px);
            background-color: var(--neon-green);
            opacity: 0.5;
        }}
        
        .timeline-item:last-child::after {{
            display: none;
        }}
        
        .project-card {{
            border: 1px solid var(--neon-blue);
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
            background-color: rgba(30, 144, 255, 0.05);
            transition: all 0.3s ease;
        }}
        
        .project-card:hover {{
            box-shadow: 0 0 15px rgba(30, 144, 255, 0.3);
            transform: translateY(-5px);
        }}
        
        .typing-effect {{
            overflow: hidden;
            white-space: nowrap;
            margin: 0 auto;
            animation: typing 3.5s steps(40, end);
        }}
        
        @keyframes typing {{
            from {{ width: 0 }}
            to {{ width: 100% }}
        }}
        
        .blink {{
            animation: blink-animation 1s steps(5, start) infinite;
        }}
        
        @keyframes blink-animation {{
            to {{
                visibility: hidden;
            }}
        }}
        
        .code-snippet {{
            font-family: 'Share Tech Mono', monospace;
            padding: 15px;
            background-color: #121212;
            border-radius: 4px;
            color: #f0f0f0;
            overflow: auto;
            max-height: 200px;
            border-left: 3px solid var(--neon-green);
        }}
        
        .code-comment {{
            color: #6272a4;
        }}
        
        .code-keyword {{
            color: #ff79c6;
        }}
        
        .code-function {{
            color: #50fa7b;
        }}
        
        .code-string {{
            color: #f1fa8c;
        }}
        
        .code-number {{
            color: #bd93f9;
        }}
        
        .progress-container {{
            width: 100%;
            background-color: #272727;
            border-radius: 5px;
            margin: 8px 0;
            position: relative;
            height: 10px;
        }}
        
        .progress-bar {{
            position: absolute;
            height: 100%;
            background: linear-gradient(90deg, var(--neon-green), var(--neon-blue));
            border-radius: 5px;
            animation: progress-anim 2s ease-out forwards;
            width: 0;
        }}
        
        @keyframes progress-anim {{
            0% {{ width: 0; }}
            100% {{ width: var(--width); }}
        }}
        
        .glitch {{
            position: relative;
            animation: glitch 1s linear infinite;
        }}
        
        @keyframes glitch {{
            2%, 64% {{
                transform: translate(2px, 0) skew(0deg);
            }}
            4%, 60% {{
                transform: translate(-2px, 0) skew(0deg);
            }}
            62% {{
                transform: translate(0, 0) skew(5deg);
            }}
        }}
        
        .section-divider {{
            position: relative;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--neon-green), transparent);
            margin: 40px 0;
        }}
        
        .section-divider::before {{
            content: "";
            position: absolute;
            left: calc(50% - 10px);
            top: -4px;
            width: 20px;
            height: 10px;
            background-color: var(--neon-green);
            border-radius: 50%;
            box-shadow: 0 0 10px var(--neon-green);
        }}
        
        .header-gap {{
            position: relative;
            z-index: 2;
            background: rgba(10, 10, 10, 0.9);
            backdrop-filter: blur(5px);
        }}
        
        .reference-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }}
        
        .reference-card {{
            flex: 1;
            min-width: 250px;
            background-color: rgba(57, 255, 20, 0.05);
            border: 1px solid var(--neon-green);
            border-radius: 8px;
            padding: 15px;
        }}
        
        .animated-badge {{
            position: relative;
            overflow: hidden;
        }}
        
        .animated-badge::after {{
            content: "";
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(
                to bottom right,
                rgba(255, 255, 255, 0) 0%,
                rgba(255, 255, 255, 0.1) 50%,
                rgba(255, 255, 255, 0) 100%
            );
            transform: rotate(30deg);
            animation: shimmer 3s infinite;
        }}
        
        @keyframes shimmer {{
            0% {{ transform: translateX(-100%) rotate(30deg); }}
            100% {{ transform: translateX(100%) rotate(30deg); }}
        }}
    </style>
</head>
<body>
    <canvas id="matrix" class="matrix-container"></canvas>
    
    <div class="container max-w-5xl mx-auto px-4 py-10">
        <header class="relative mb-16">
            <div class="text-center">
                <h1 class="tech-mono text-5xl md:text-6xl font-bold neon-text mb-2">{data['personal_info']['name'].upper()}<span class="blink">_</span></h1>
                <h2 class="text-2xl md:text-3xl mb-4 neon-blue">{data['personal_info']['title'].upper()}</h2>
                <div class="flex flex-wrap justify-center gap-4 mb-6">
                    <div class="flex items-center">
                        <i class="fas fa-map-marker-alt mr-2 neon-cyan"></i>
                        <span>{data['personal_info'].get('location', '')}</span>
                    </div>
                    <div class="flex items-center">
                        <i class="fas fa-envelope mr-2 neon-cyan"></i>
                        <span>{data['personal_info']['email']}</span>
                    </div>
                    {f'<div class="flex items-center"><i class="fas fa-phone-alt mr-2 neon-cyan"></i><span>{data["personal_info"]["phone"]}</span></div>' if 'phone' in data['personal_info'] else ''}
                    {f'<div class="flex items-center"><i class="fas fa-id-card mr-2 neon-cyan"></i><span>{data["personal_info"]["citizenship"]}</span></div>' if 'citizenship' in data['personal_info'] else ''}
                </div>
            </div>
            
            <div class="terminal mt-8">
                <div class="terminal-header">
                    <div class="terminal-dots">
                        <div class="terminal-dot" style="background-color: #ff5f56;"></div>
                        <div class="terminal-dot" style="background-color: #ffbd2e;"></div>
                        <div class="terminal-dot" style="background-color: #27c93f;"></div>
                    </div>
                    <div class="ml-auto mr-2 tech-mono text-sm opacity-70">bash ~/profile.sh</div>
                </div>
                <div class="tech-mono text-sm">
                    <span class="neon-green">root@{data['personal_info']['name'].lower().replace(' ', '-')}-dev:~$</span> cat profile.txt<br><br>
                    {data['professional_summary']}
                </div>
            </div>
        </header>
        
        <div class="section-divider"></div>
        
        <!-- SKILLS SECTION -->
        <section class="mb-16">
            <h2 class="text-3xl font-bold mb-6 neon-text"><i class="fas fa-code mr-2"></i>TECHNICAL_SKILLS</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="skill-category">
                    <h3 class="text-xl font-semibold mb-3 neon-blue">Programming Languages</h3>
                    <div>
    """

    # Add programming languages
    for lang in data['skills']['programming_languages']:
        html_content += f"""
                        <div class="skill-badge tech-mono">{lang['name']}</div>
        """

    html_content += f"""
                    </div>
                </div>
                
                <div class="skill-category">
                    <h3 class="text-xl font-semibold mb-3 neon-blue">Cloud Technologies</h3>
                    <div>
    """

    # Add cloud technologies
    for tech in data['skills']['cloud_technologies']:
        html_content += f"""
                        <div class="skill-badge tech-mono">{tech}</div>
        """

    html_content += f"""
                    </div>
                </div>
                
                <div class="skill-category">
                    <h3 class="text-xl font-semibold mb-3 neon-blue">AI/ML</h3>
                    <div>
    """

    # Add AI/ML skills
    for ai_skill in data['skills']['ai_ml']:
        html_content += f"""
                        <div class="skill-badge tech-mono">{ai_skill}</div>
        """

    html_content += f"""
                    </div>
                </div>
                
                <div class="skill-category">
                    <h3 class="text-xl font-semibold mb-3 neon-blue">DevOps</h3>
                    <div>
    """

    # Add DevOps skills
    for devops_skill in data['skills']['devops']:
        html_content += f"""
                        <div class="skill-badge tech-mono">{devops_skill}</div>
        """

    html_content += f"""
                    </div>
                </div>
            </div>
            
            <div class="code-snippet mt-6">
                <span class="code-comment">// Skill Proficiency Level</span><br>
                <span class="code-keyword">const</span> <span class="code-function">skillProficiency</span> = {{<br>
    """

    # Add proficiency levels
    for i, lang in enumerate(data['skills']['programming_languages']):
        percent = int(lang.get('proficiency').replace('%', ''))
        level = "Expert" if percent >= 80 else "Advanced" if percent >= 60 else "Intermediate"
        html_content += f"                &nbsp;&nbsp;{lang['name'].lower()}: <span class=\"code-string\">\"{level}\"</span>{',' if i < len(data['skills']['programming_languages']) - 1 else ''}<br>"

    html_content += f"""
                }};<br>
                <br>
                <span class="code-comment">// Years of Experience</span><br>
                <span class="code-keyword">let</span> yearsOfExperience = <span class="code-number">0</span>; <span class="code-comment">// Calculated from work experience</span><br>
                <span class="code-keyword">const</span> <span class="code-function">getFutureSkills</span> = () => [<span class="code-string">"Quantum Computing"</span>, <span class="code-string">"Edge AI"</span>, <span class="code-string">"Web3"</span>];
            </div>
        </section>
        
        <div class="section-divider"></div>
        
        <!-- WORK EXPERIENCE -->
        <section class="mb-16">
            <h2 class="text-3xl font-bold mb-6 neon-text"><i class="fas fa-briefcase mr-2"></i>WORK_EXPERIENCE</h2>
    """

    # Add work experience
    for exp in data['work_experience']:
        html_content += f"""
            <div class="timeline-item">
                <div class="flex flex-wrap justify-between items-start mb-2">
                    <h3 class="text-xl font-bold neon-cyan">{exp['company']}</h3>
                    <div class="tech-mono text-sm neon-green">{exp['period']}</div>
                </div>
                <h4 class="text-lg font-semibold mb-2">{exp['position']}</h4>
                <ul class="list-disc list-inside">
        """

        for responsibility in exp['responsibilities']:
            html_content += f"""
                    <li class="mb-2">{responsibility}</li>
            """

        html_content += """
                </ul>
            </div>
        """

    html_content += f"""
            <div class="terminal mt-8">
                <div class="terminal-header">
                    <div class="terminal-dots">
                        <div class="terminal-dot" style="background-color: #ff5f56;"></div>
                        <div class="terminal-dot" style="background-color: #ffbd2e;"></div>
                        <div class="terminal-dot" style="background-color: #27c93f;"></div>
                    </div>
                    <div class="ml-auto mr-2 tech-mono text-sm opacity-70">achievements.py</div>
                </div>
                <div class="tech-mono text-sm">
                    <span class="code-keyword">def</span> <span class="code-function">key_achievements</span>():<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;<span class="code-keyword">return</span> [<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="code-string">"Significant achievements listed in work experience"</span>,<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="code-string">"Notable contributions to projects and teams"</span>,<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="code-string">"Technical leadership and mentoring"</span><br>
                    &nbsp;&nbsp;&nbsp;&nbsp;]
                </div>
            </div>
        </section>
        
        <div class="section-divider"></div>
        
        <!-- PROJECTS -->
        <section class="mb-16">
            <h2 class="text-3xl font-bold mb-6 neon-text"><i class="fas fa-project-diagram mr-2"></i>AI/ML_PROJECTS</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
    """

    # Add projects
    for project in data['projects']:
        html_content += f"""
                <div class="project-card">
                    <h3 class="text-xl font-bold mb-2 neon-blue">{project['name']}</h3>
                    <p class="mb-3">{project['description']}</p>
                    <div class="flex flex-wrap mb-2">
        """

        for tech in project['technologies']:
            html_content += f"""
                        <div class="skill-badge tech-mono text-xs">{tech}</div>
            """

        html_content += f"""
                    </div>
                    <div class="progress-container">
                        <div class="progress-bar" style="--width: {80 + (hash(project['name']) % 20)}%;"></div>
                    </div>
                </div>
        """

    html_content += f"""
            </div>
            
            <div class="code-snippet mt-8">
                <span class="code-comment"># AI Model Architecture Blueprint</span><br>
                <span class="code-keyword">import</span> tensorflow <span class="code-keyword">as</span> tf<br>
                <span class="code-keyword">from</span> transformers <span class="code-keyword">import</span> AutoModelForCausalLM, AutoTokenizer<br>
                <br>
                <span class="code-keyword">def</span> <span class="code-function">build_project_pipeline</span>(project_name):<br>
                &nbsp;&nbsp;&nbsp;&nbsp;<span class="code-keyword">return</span> <span class="code-string">"Custom implementation based on project requirements"</span><br>
                <br>
                <span class="code-comment"># Typical performance improvements: 30-50% efficiency gains</span>
            </div>
        </section>
        
        <div class="section-divider"></div>
        
        <!-- EDUCATION & CERTIFICATIONS -->
        <section class="mb-16">
            <h2 class="text-3xl font-bold mb-6 neon-text"><i class="fas fa-graduation-cap mr-2"></i>EDUCATION_&_CERTIFICATIONS</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
    """

    # Add education
    for edu in data['education']:
        html_content += f"""
                <div class="terminal">
                    <div class="terminal-header">
                        <div class="terminal-dots">
                            <div class="terminal-dot" style="background-color: #ff5f56;"></div>
                            <div class="terminal-dot" style="background-color: #ffbd2e;"></div>
                            <div class="terminal-dot" style="background-color: #27c93f;"></div>
                        </div>
                    </div>
                    <div class="tech-mono text-center">
                        <div class="text-lg font-bold mb-2">{edu['degree']}</div>
                        <div class="neon-green">{edu['year']}</div>
                    </div>
                </div>
        """

    # Add certifications
    for cert in data['certifications']:
        html_content += f"""
                <div class="terminal">
                    <div class="terminal-header">
                        <div class="terminal-dots">
                            <div class="terminal-dot" style="background-color: #ff5f56;"></div>
                            <div class="terminal-dot" style="background-color: #ffbd2e;"></div>
                            <div class="terminal-dot" style="background-color: #27c93f;"></div>
                        </div>
                    </div>
                    <div class="tech-mono text-center">
                        <div class="text-lg font-bold mb-2">{cert['name']}</div>
                        <div class="neon-green">{cert['year']}</div>
                    </div>
                </div>
        """

    html_content += f"""
            </div>
        </section>
        
        <div class="section-divider"></div>
        
        <!-- REFERENCES -->
        <section class="mb-16">
            <h2 class="text-3xl font-bold mb-6 neon-text"><i class="fas fa-user-check mr-2"></i>REFERENCES</h2>
            
            <div class="reference-container">
    """

    # Add references
    for ref in data['references']:
        html_content += f"""
                <div class="reference-card">
                    <h3 class="text-xl font-bold mb-2 neon-cyan">{ref['name']}</h3>
                    <p class="mb-1">{ref['position']}</p>
                    <div class="flex items-center">
                        <i class="fas fa-phone-alt mr-2 neon-green"></i>
                        <span>{ref['phone']}</span>
                    </div>
                </div>
        """

    html_content += f"""
            </div>
        </section>
        
        <footer class="text-center mt-16">
            <div class="tech-mono text-sm opacity-70">
                <p>// Generated using Matrix-CV Engine v2.0.0</p>
                <p class="neon-text mt-2">[ SYSTEM READY ]</p>
            </div>
        </footer>
    </div>
    
    <script>
        // Matrix rain effect
        const canvas = document.getElementById('matrix');
        const ctx = canvas.getContext('2d');
        
        // Setting canvas size
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        // Characters to be used in matrix
        const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$+-*/=%"\'#&_(),.;:?!\\|{{}}<>[]^~';
        
        // Font size and columns
        const fontSize = 14;
        const columns = Math.floor(canvas.width / fontSize);
        
        // Array to store current y position for each column
        const drops = [];
        
        // Initialize drops array
        for (let i = 0; i < columns; i++) {{
            drops[i] = Math.random() * -100; // Start position above canvas for staggered entry
        }}
        
        // Draw matrix
        function drawMatrix() {{
            // Black background with slight opacity for trail effect
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // Set text color and font
            ctx.fillStyle = '#0f0';
            ctx.font = `${{fontSize}}px monospace`;
            
            // Loop through each column
            for (let i = 0; i < drops.length; i++) {{
                // Generate random character
                const char = chars[Math.floor(Math.random() * chars.length)];
                
                // Brighten some characters randomly
                if (Math.random() > 0.98) {{
                    ctx.fillStyle = '#fff';
                }} else if (Math.random() > 0.95) {{
                    ctx.fillStyle = '#0ff';
                }} else {{
                    ctx.fillStyle = '#0f0';
                }}
                
                // Draw character
                ctx.fillText(char, i * fontSize, drops[i] * fontSize);
                
                // Reset position if drop reaches end or randomly
                if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {{
                    drops[i] = 0;
                }}
                
                // Move drop
                drops[i]++;
            }}
        }}
        
        // Animation loop
        setInterval(drawMatrix, 50);
        
        // Resize canvas on window resize
        window.addEventListener('resize', () => {{
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            // Recalculate columns
            const newColumns = Math.floor(canvas.width / fontSize);
            
            // Adjust drops array
            if (newColumns > columns) {{
                for (let i = drops.length; i < newColumns; i++) {{
                    drops[i] = Math.random() * -100;
                }}
            }}
        }});
        
        // Apply the progressive animation to skill badges
        document.addEventListener('DOMContentLoaded', function() {{
            const skillBadges = document.querySelectorAll('.skill-badge');
            
            skillBadges.forEach((badge, index) => {{
                setTimeout(() => {{
                    badge.classList.add('animated-badge');
                }}, index * 100);
            }});
            
            // Initialize progress bars
            const progressBars = document.querySelectorAll('.progress-bar');
            progressBars.forEach(bar => {{
                const width = bar.style.getPropertyValue('--width');
                bar.style.width = width;
            }});
        }});
    </script>
</body>
</html>
    """

    # Write to output file
    with open(output_file_path, 'w') as f:
        f.write(html_content)
    
    print(f"Resume generated successfully at {output_file_path}")
import json
from datetime import datetime
import hashlib

def generate_html_resume_neural(json_file_path, output_file_path='resume.html'):
    # Load JSON data and validate against schema
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    
    # Generate HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['personal_info']['name']} - AI Neural Network Resume</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300;400;500;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #0f172a;
            color: #e2e8f0;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }}
        
        .code-font {{
            font-family: 'Roboto Mono', monospace;
        }}
        
        .neural-container {{
            min-height: 100vh;
            position: relative;
        }}
        
        .node {{
            cursor: pointer;
            transition: all 0.3s ease;
        }}
        
        .node:hover {{
            filter: brightness(1.5);
        }}
        
        .link {{
            stroke-opacity: 0.6;
            stroke-width: 1.5px;
        }}
        
        .neural-bg {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            opacity: 0.2;
        }}
        
        .content-container {{
            position: relative;
            z-index: 2;
        }}
        
        .experience-node {{
            border-radius: 12px;
            background: rgba(15, 23, 42, 0.7);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(148, 163, 184, 0.2);
            transition: all 0.3s ease;
        }}
        
        .experience-node:hover {{
            box-shadow: 0 0 25px rgba(56, 189, 248, 0.4);
            transform: translateY(-5px);
        }}
        
        .skill-node {{
            position: relative;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            font-weight: 600;
            color: white;
            width: 70px;
            height: 70px;
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.3);
            transition: all 0.3s ease;
        }}
        
        .skill-node:hover {{
            transform: scale(1.1);
            box-shadow: 0 0 25px rgba(56, 189, 248, 0.6);
        }}
        
        .neural-pulse {{
            position: absolute;
            border-radius: 50%;
            z-index: -1;
            animation: pulse 2s infinite;
        }}
        
        @keyframes pulse {{
            0% {{
                transform: scale(1);
                opacity: 0.7;
            }}
            70% {{
                transform: scale(1.5);
                opacity: 0;
            }}
            100% {{
                transform: scale(1);
                opacity: 0;
            }}
        }}
        
        .gradient-text {{
            background: linear-gradient(90deg, #38bdf8, #818cf8);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }}
        
        .hidden-info {{
            display: none;
            position: absolute;
            z-index: 10;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(5px);
            border: 1px solid rgba(148, 163, 184, 0.3);
            border-radius: 8px;
            padding: 12px;
            min-width: 240px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            top: 0;
            left: 100%;
            animation: fadeIn 0.3s ease;
        }}
        
        @keyframes fadeIn {{
            0% {{
                opacity: 0;
                transform: translateY(10px);
            }}
            100% {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        /* Network paths animation */
        .path-animation {{
            stroke-dasharray: 10;
            stroke-dashoffset: 1000;
            animation: dash 15s linear infinite;
        }}
        
        @keyframes dash {{
            to {{
                stroke-dashoffset: 0;
            }}
        }}
        
        /* Progress bars */
        .progress-container {{
            width: 100%;
            height: 6px;
            background: rgba(148, 163, 184, 0.2);
            border-radius: 3px;
            overflow: hidden;
        }}
        
        .progress-bar {{
            height: 100%;
            border-radius: 3px;
            background: linear-gradient(90deg, #38bdf8, #818cf8);
            transition: width 1.5s ease-in-out;
        }}
        
        .badge {{
            display: inline-block;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 500;
            margin-right: 5px;
            margin-bottom: 5px;
            background: rgba(56, 189, 248, 0.2);
            border: 1px solid rgba(56, 189, 248, 0.4);
        }}
        
        .timeline-connector {{
            position: absolute;
            left: 35px;
            top: 0;
            bottom: 0;
            width: 2px;
            background: linear-gradient(to bottom, rgba(56, 189, 248, 0.7), rgba(129, 140, 248, 0.7));
            z-index: -1;
        }}
        
        .timeline-dot {{
            position: absolute;
            left: 28px;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: linear-gradient(45deg, #38bdf8, #818cf8);
            box-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
            z-index: 2;
        }}
        
        .section-title {{
            position: relative;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}
        
        .section-title:after {{
            content: '';
            position: absolute;
            left: 0;
            bottom: 0;
            width: 60px;
            height: 3px;
            background: linear-gradient(90deg, #38bdf8, #818cf8);
        }}
        
        @media print {{
            body {{
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }}
            
            .neural-bg {{
                opacity: 0.1;
            }}
        }}
    </style>
</head>
<body>
    <!-- Neural Network Background -->
    <div id="neuralBg" class="neural-bg"></div>
    
    <div class="neural-container">
        <div class="content-container max-w-6xl mx-auto px-4 py-8">
            <!-- Header Section -->
            <header class="mb-12 relative">
                <div class="flex flex-col md:flex-row items-start md:items-end justify-between">
                    <div>
                        <h1 class="text-4xl md:text-5xl font-bold gradient-text tracking-tight">
                            {data['personal_info']['name']}
                        </h1>
                        <div class="flex items-center mt-2 opacity-80 code-font">
                            <span class="text-sky-400">function</span> 
                            <span class="ml-2 text-xl font-medium text-white">
                                {data['personal_info']['title'].replace(' ', '')}()
                            </span>
                            <span class="ml-2 text-sky-400">;</span>
                        </div>
                        <div class="mt-3 flex flex-wrap text-slate-300">
                            <span class="mr-4 flex items-center">
                                <svg class="w-4 h-4 mr-1 text-sky-400" fill="currentColor" viewBox="0 0 20 20">
                                    <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"></path>
                                </svg>
                                {data['personal_info'].get('location', '')}
                            </span>
                            <span class="mr-4 flex items-center">
                                <svg class="w-4 h-4 mr-1 text-sky-400" fill="currentColor" viewBox="0 0 20 20">
                                    <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"></path>
                                    <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"></path>
                                </svg>
                                {data['personal_info']['email']}
                            </span>"""

    # Add phone if available
    if 'phone' in data['personal_info']:
        html_content += f"""
                            <span class="flex items-center">
                                <svg class="w-4 h-4 mr-1 text-sky-400" fill="currentColor" viewBox="0 0 20 20">
                                    <path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"></path>
                                </svg>
                                {data['personal_info']['phone']}
                            </span>"""

    html_content += f"""
                        </div>
                    </div>
                    
                    <div class="mt-6 md:mt-0 text-right">
                        <div class="inline-block px-4 py-2 bg-sky-800 bg-opacity-30 rounded-lg border border-sky-700 code-font">
                            <div class="text-slate-300">
                                <span class="text-sky-400">citizenship:</span> {data['personal_info'].get('citizenship', '')}
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="mt-6 p-5 rounded-xl bg-slate-800 bg-opacity-40 backdrop-blur-sm border border-slate-700">
                    <h2 class="text-lg font-medium text-sky-300 mb-2 code-font">// Professional Summary</h2>
                    <p class="text-slate-300 leading-relaxed">
                        {data['professional_summary']}
                    </p>
                </div>
            </header>
            
            <!-- Skills Section as Neural Network Nodes -->
            <section class="mb-16">
                <h2 class="text-2xl font-bold gradient-text section-title">Neural Network Skills</h2>
                
                <div class="relative h-[500px] w-full bg-slate-900 bg-opacity-30 rounded-xl border border-slate-800 overflow-hidden" id="skillsNetwork">
                    <!-- D3.js will render skills as neural network here -->
                </div>
                
                <div class="mt-6 grid grid-cols-1 md:grid-cols-3 gap-6">
                    <!-- Programming Languages -->
                    <div class="p-5 rounded-xl bg-slate-800 bg-opacity-40 backdrop-blur-sm border border-slate-700">
                        <h3 class="text-lg font-medium text-sky-300 mb-3 code-font">
                            Programming Languages
                        </h3>
                        <div class="space-y-4">"""

    # Add programming languages with progress bars
    for lang in data['skills']['programming_languages']:
        percent = lang['proficiency'].replace('%', '')
        html_content += f"""
                            <div>
                                <div class="flex justify-between mb-1">
                                    <span class="text-slate-300">{lang['name']}</span>
                                    <span class="text-slate-400">{lang['proficiency']}</span>
                                </div>
                                <div class="progress-container">
                                    <div class="progress-bar" style="width: {percent}%"></div>
                                </div>
                            </div>"""

    html_content += f"""
                        </div>
                    </div>
                    
                    <!-- Cloud Technologies -->
                    <div class="p-5 rounded-xl bg-slate-800 bg-opacity-40 backdrop-blur-sm border border-slate-700">
                        <h3 class="text-lg font-medium text-sky-300 mb-3 code-font">
                            Cloud Technologies
                        </h3>
                        <div class="flex flex-wrap">"""

    # Add cloud technologies
    for tech in data['skills']['cloud_technologies']:
        html_content += f"""
                            <span class="badge">{tech}</span>"""

    html_content += f"""
                        </div>
                        
                        <h3 class="text-lg font-medium text-sky-300 mt-5 mb-3 code-font">
                            DevOps
                        </h3>
                        <div class="flex flex-wrap">"""

    # Add DevOps skills
    for devops_skill in data['skills']['devops']:
        html_content += f"""
                            <span class="badge">{devops_skill}</span>"""

    html_content += f"""
                        </div>
                    </div>
                    
                    <!-- AI/ML Technologies -->
                    <div class="p-5 rounded-xl bg-slate-800 bg-opacity-40 backdrop-blur-sm border border-slate-700">
                        <h3 class="text-lg font-medium text-sky-300 mb-3 code-font">
                            AI & Machine Learning
                        </h3>
                        <div class="flex flex-wrap">"""

    # Add AI/ML skills
    for ai_skill in data['skills']['ai_ml']:
        html_content += f"""
                            <span class="badge">{ai_skill}</span>"""

    html_content += f"""
                        </div>
                        
                        <div class="mt-6 text-center">
                            <div class="inline-block px-4 py-2 bg-indigo-900 bg-opacity-30 rounded-lg border border-indigo-700 code-font">
                                <div class="text-slate-300 text-sm">"""

    # Add certifications if available
    if len(data['certifications']) > 0:
        html_content += f"""
                                    <span class="text-indigo-400">certification:</span> {data['certifications'][0]['name']} ({data['certifications'][0]['year']})"""
        if len(data['certifications']) > 1:
            html_content += f"""<br>
                                    <span class="text-indigo-400">planned:</span> {data['certifications'][1]['name']} ({data['certifications'][1]['year']})"""

    html_content += f"""
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            
            <!-- Experience Section as Data Flows -->
            <section class="mb-16">
                <h2 class="text-2xl font-bold gradient-text section-title">Experience Data Flow</h2>
                
                <div class="relative">
                    <div class="timeline-connector"></div>"""

    # Add work experience
    for exp in data['work_experience']:
        html_content += f"""
                    <!-- {exp['company']} -->
                    <div class="mb-8 relative pl-16">
                        <div class="timeline-dot" style="top: 24px;"></div>
                        <div class="experience-node p-5 rounded-xl">
                            <div class="flex flex-wrap justify-between items-start">
                                <h3 class="text-xl font-semibold text-white">{exp['position']}</h3>
                                <span class="text-sky-400 bg-sky-900 bg-opacity-30 px-3 py-1 rounded-full text-sm">{exp['period']}</span>
                            </div>
                            <div class="text-sky-300 mb-2">{exp['company']}</div>
                            <ul class="mt-3 space-y-2 text-slate-300">"""

        for responsibility in exp['responsibilities']:
            html_content += f"""
                                <li class="flex items-start">
                                    <svg class="w-5 h-5 mr-2 text-sky-400 mt-1 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                    {responsibility}
                                </li>"""

        html_content += """
                            </ul>
                        </div>
                    </div>"""

    html_content += f"""
                </div>
            </section>
            
            <!-- Projects Section as Activation Layers -->
            <section class="mb-16">
                <h2 class="text-2xl font-bold gradient-text section-title">Activation Layer Projects</h2>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">"""

    # Add projects
    for project in data['projects']:
        # Generate a unique color based on project name hash
        project_hash = int(hashlib.sha1(project['name'].encode()).hexdigest(), 16)
        color_variants = [
            ("sky", "400", "500"),
            ("indigo", "400", "500"),
            ("purple", "400", "500"),
            ("blue", "400", "500"),
            ("cyan", "400", "500")
        ]
        color_idx = project_hash % len(color_variants)
        color = color_variants[color_idx]
        
        html_content += f"""
                    <!-- {project['name']} -->
                    <div class="experience-node p-6 rounded-xl relative overflow-hidden">
                        <div class="absolute -right-10 -top-10 w-20 h-20 bg-{color[1]}-500 opacity-20 rounded-full"></div>
                        <div class="absolute -right-5 -top-5 w-10 h-10 bg-{color[1]}-400 opacity-20 rounded-full"></div>
                        
                        <h3 class="text-xl font-semibold text-white mb-2">{project['name']}</h3>
                        <div class="flex mb-3">"""

        for tech in project['technologies']:
            html_content += f"""
                            <span class="badge">{tech}</span>"""

        html_content += f"""
                        </div>
                        <p class="text-slate-300">
                            {project['description']}
                        </p>
                    </div>"""

    html_content += f"""
                </div>
            </section>
            
            <!-- Education and References Section -->
            <section class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div>
                    <h2 class="text-2xl font-bold gradient-text section-title">Education Input Layer</h2>"""

    # Add education
    for edu in data['education']:
        html_content += f"""
                    <div class="experience-node p-5 rounded-xl">
                        <div class="flex flex-wrap justify-between items-start">
                            <h3 class="text-xl font-semibold text-white">{edu['degree']}</h3>
                            <span class="text-sky-400 bg-sky-900 bg-opacity-30 px-3 py-1 rounded-full text-sm">{edu['year']}</span>
                        </div>
                    </div>"""

    html_content += f"""
                </div>
                
                <div>
                    <h2 class="text-2xl font-bold gradient-text section-title">Reference Output Nodes</h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">"""

    # Add references
    for ref in data['references']:
        html_content += f"""
                        <div class="experience-node p-4 rounded-xl">
                            <h3 class="text-lg font-semibold text-white">{ref['name']}</h3>
                            <div class="text-sky-300 text-sm">{ref['position']}</div>
                            <div class="mt-2 text-slate-300 text-sm flex items-center">
                                <svg class="w-4 h-4 mr-1 text-sky-400" fill="currentColor" viewBox="0 0 20 20">
                                    <path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"></path>
                                </svg>
                                {ref['phone']}
                            </div>
                        </div>"""

    html_content += f"""
                    </div>
                </div>
            </section>
            
            <!-- Footer -->
            <footer class="mt-16 text-center text-slate-400 code-font">
                <p>// Built with Neural Network Technology</p>
            </footer>
        </div>
    </div>
    
    <script>
        // Neural Network Background
        function createNeuralBackground() {{
            const width = window.innerWidth;
            const height = window.innerHeight;
            const nodeCount = Math.floor(width * height / 15000);
            
            const svg = d3.select("#neuralBg")
                .append("svg")
                .attr("width", "100%")
                .attr("height", "100%")
                .attr("viewBox", `0 0 ${{width}} ${{height}}`);
            
            // Generate random nodes
            const nodes = Array.from({{ length: nodeCount }}, () => ({{
                x: Math.random() * width,
                y: Math.random() * height,
                r: Math.random() * 2 + 1
            }}));
            
            // Generate links between nodes that are close to each other
            const links = [];
            for (let i = 0; i < nodes.length; i++) {{
                for (let j = i + 1; j < nodes.length; j++) {{
                    const dx = nodes[i].x - nodes[j].x;
                    const dy = nodes[i].y - nodes[j].y;
                    const distance = Math.sqrt(dx * dx + dy * dy);
                    
                    if (distance < 150) {{
                        links.push({{
                            source: i,
                            target: j,
                            distance: distance
                        }});
                    }}
                }}
            }}
            
            // Draw links
            svg.selectAll(".link")
                .data(links)
                .enter()
                .append("line")
                .attr("class", "link")
                .attr("x1", d => nodes[d.source].x)
                .attr("y1", d => nodes[d.source].y)
                .attr("x2", d => nodes[d.target].x)
                .attr("y2", d => nodes[d.target].y)
                .style("stroke", d => `rgba(56, 189, 248, ${{0.2 * (1 - d.distance / 150)}})`);
            
            // Draw nodes
            svg.selectAll(".node")
                .data(nodes)
                .enter()
                .append("circle")
                .attr("class", "node")
                .attr("cx", d => d.x)
                .attr("cy", d => d.y)
                .attr("r", d => d.r)
                .style("fill", () => {{
                    const colors = ["#38bdf8", "#818cf8", "#c084fc"];
                    return colors[Math.floor(Math.random() * colors.length)];
                }});
            
            // Add some animated pulses
            for (let i = 0; i < 10; i++) {{
                const randomNode = nodes[Math.floor(Math.random() * nodes.length)];
                svg.append("circle")
                    .attr("class", "path-animation")
                    .attr("cx", randomNode.x)
                    .attr("cy", randomNode.y)
                    .attr("r", 2)
                    .style("fill", "none")
                    .style("stroke", "#38bdf8")
                    .style("stroke-width", "1px");
            }}
        }}
        
        // Skills Network Visualization
        function createSkillsNetwork() {{
            const width = document.getElementById("skillsNetwork").clientWidth;
            const height = 500;
            
            const svg = d3.select("#skillsNetwork")
                .append("svg")
                .attr("width", "100%")
                .attr("height", "100%")
                .attr("viewBox", `0 0 ${{width}} ${{height}}`);
            
            // Create skill nodes from the schema data
            const programmingSkills = {json.dumps([
                {'name': lang['name'], 'group': 1, 'value': int(lang.get('proficiency').replace('%', ''))}
                for lang in data['skills']['programming_languages']
            ])};
            
            const cloudSkills = {json.dumps([
                {'name': tech, 'group': 2, 'value': 80}
                for tech in data['skills']['cloud_technologies']
            ])};
            
            const aiSkills = {json.dumps([
                {'name': skill, 'group': 3, 'value': 80}
                for skill in data['skills']['ai_ml']
            ])};
            
            const devOpsSkills = {json.dumps([
                {'name': skill, 'group': 4, 'value': 80}
                for skill in data['skills']['devops']
            ])};
            
            // Combine all skills
            const nodes = [
                ...programmingSkills,
                ...cloudSkills,
                ...aiSkills,
                ...devOpsSkills
            ];
            
            // Define links between nodes
            const links = [];
            
            // Link within groups
            for (let i = 0; i < nodes.length; i++) {{
                for (let j = i + 1; j < nodes.length; j++) {{
                    if (nodes[i].group === nodes[j].group) {{
                        links.push({{
                            source: i,
                            target: j,
                            value: 1
                        }});
                    }}
                }}
            }}
            
            // Some cross-group links for interconnectedness
            for (let i = 0; i < nodes.length; i++) {{
                for (let j = 0; j < nodes.length; j++) {{
                    if (nodes[i].group !== nodes[j].group && Math.random() < 0.1) {{
                        links.push({{
                            source: i,
                            target: j,
                            value: 0.5
                        }});
                    }}
                }}
            }}
            
            // Create force simulation
            const simulation = d3.forceSimulation(nodes)
                .force("link", d3.forceLink(links).id(d => nodes.indexOf(d)))
                .force("charge", d3.forceManyBody().strength(-150))
                .force("center", d3.forceCenter(width / 2, height / 2))
                .force("collide", d3.forceCollide().radius(50));
            
            // Add links
            const link = svg.append("g")
                .attr("class", "links")
                .selectAll("line")
                .data(links)
                .enter()
                .append("line")
                .attr("class", "link path-animation")
                .style("stroke", d => {{
                    const colors = ["#38bdf8", "#818cf8", "#c084fc"];
                    return colors[Math.floor(Math.random() * colors.length)];
                }})
                .style("stroke-opacity", d => d.value * 0.5);
            
            // Add nodes
            const node = svg.append("g")
                .attr("class", "nodes")
                .selectAll("g")
                .data(nodes)
                .enter()
                .append("g");
            
            // Add circles for nodes
            node.append("circle")
                .attr("r", d => 20 + d.value / 5)
                .style("fill", d => {{
                    const colors = ["#38bdf8", "#818cf8", "#c084fc", "#6366f1"];
                    return colors[d.group - 1];
                }})
                .style("fill-opacity", 0.8)
                .style("stroke", "#e2e8f0")
                .style("stroke-width", "1px")
                .style("stroke-opacity", 0.5)
                .on("mouseover", function(event, d) {{
                    d3.select(this)
                        .transition()
                        .duration(300)
                        .attr("r", 30 + d.value / 5);
                }})
                .on("mouseout", function(event, d) {{
                    d3.select(this)
                        .transition()
                        .duration(300)
                        .attr("r", 20 + d.value / 5);
                }});
            
            // Add text to nodes
            node.append("text")
                .text(d => d.name)
                .attr("font-size", "10px")
                .attr("text-anchor", "middle")
                .attr("dy", ".35em")
                .attr("fill", "#ffffff");
            
            // Add title for tooltip
            node.append("title")
                .text(d => `${{d.name}} (${{d.value}}%)`);
            
            // Add pulse effects to some nodes
            node.append("circle")
                .attr("r", d => 20 + d.value / 5)
                .style("fill", "none")
                .style("stroke", d => {{
                    const colors = ["#38bdf8", "#818cf8", "#c084fc", "#6366f1"];
                    return colors[d.group - 1];
                }})
                .style("stroke-width", "1px")
                .style("stroke-opacity", 0.5)
                .style("animation", "pulse 2s infinite");
            
            // Update positions in simulation
            simulation.on("tick", () => {{
                // Constrain nodes to the visualization area
                nodes.forEach(d => {{
                    d.x = Math.max(30, Math.min(width - 30, d.x));
                    d.y = Math.max(30, Math.min(height - 30, d.y));
                }});
                
                link
                    .attr("x1", d => d.source.x)
                    .attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x)
                    .attr("y2", d => d.target.y);
                
                node
                    .attr("transform", d => `translate(${{d.x}},${{d.y}})`);
            }});
        }}
        
        // Initialize visualizations when DOM is loaded
        document.addEventListener("DOMContentLoaded", () => {{
            createNeuralBackground();
            createSkillsNetwork();
            
            // Initialize progress bars with animation
            const progressBars = document.querySelectorAll('.progress-bar');
            setTimeout(() => {{
                progressBars.forEach(bar => {{
                    const width = bar.style.width;
                    bar.style.width = "0";
                    
                    setTimeout(() => {{
                        bar.style.width = width;
                    }}, 100);
                }});
            }}, 500);
        }});
    </script>
</body>
</html>"""

    # Write to output file
    with open(output_file_path, 'w') as f:
        f.write(html_content)
    
    print(f"Resume generated successfully at {output_file_path}")


import json
import hashlib

def generate_cyberpunk_cv(json_file_path, output_file_path='cyberpunk_cv.html'):
    # Load JSON data
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    
    # Generate HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['personal_info']['name']} - Cyberpunk CV</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Share+Tech+Mono&family=Rajdhani:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --neon-pink: #ff2a6d;
            --neon-blue: #05d9e8;
            --neon-purple: #9d4edd;
            --neon-green: #39ff14;
            --dark-bg: #0a0a0f;
            --darker-bg: #050508;
            --cyber-blue: #1e90ff;
        }}
        
        html, body {{
            background-color: var(--dark-bg);
            color: #d1d1d1;
            font-family: 'Rajdhani', sans-serif;
            overflow-x: hidden;
            scroll-behavior: smooth;
        }}
        
        .orbitron {{
            font-family: 'Orbitron', sans-serif;
        }}
        
        .mono {{
            font-family: 'Share Tech Mono', monospace;
        }}
        
        .background-circuit {{
            background-image: url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M11 18c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm48 25c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm-43-7c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm63 31c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM34 90c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm56-76c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM12 86c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm28-65c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm23-11c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-6 60c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm29 22c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zM32 63c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm57-13c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-9-21c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM60 91c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM35 41c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM12 60c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2z' fill='rgba(30, 144, 255, 0.1)' fill-rule='evenodd'/%3E%3C/svg%3E");
        }}
        
        .cv-container {{
            position: relative;
            max-width: 1100px;
            margin: 0 auto;
            padding: 40px 20px;
            background-color: var(--darker-bg);
            box-shadow: 0 0 40px rgba(5, 217, 232, 0.2);
            border: 1px solid rgba(30, 144, 255, 0.3);
        }}
        
        .scanlines {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            pointer-events: none;
            z-index: 10;
            opacity: 0.1;
            background: linear-gradient(
                to bottom,
                rgba(255, 255, 255, 0) 50%,
                rgba(0, 0, 0, 0.3) 50%
            );
            background-size: 100% 4px;
        }}
        
        .glitch-container {{
            position: relative;
        }}
        
        .text-glitch {{
            position: relative;
            animation: glitch-skew 1s infinite linear alternate-reverse;
        }}
        
        .text-glitch::before,
        .text-glitch::after {{
            content: attr(data-text);
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }}
        
        .text-glitch::before {{
            left: 2px;
            text-shadow: -2px 0 var(--neon-pink);
            clip: rect(44px, 450px, 56px, 0);
            animation: glitch-anim 5s infinite linear alternate-reverse;
        }}
        
        .text-glitch::after {{
            left: -2px;
            text-shadow: -2px 0 var(--neon-blue);
            clip: rect(44px, 450px, 56px, 0);
            animation: glitch-anim2 5s infinite linear alternate-reverse;
        }}
        
        @keyframes glitch-anim {{
            0% {{
                clip: rect(31px, 9999px, 94px, 0);
                transform: skew(0.85deg);
            }}
            5% {{
                clip: rect(70px, 9999px, 78px, 0);
                transform: skew(0.63deg);
            }}
            10% {{
                clip: rect(65px, 9999px, 7px, 0);
                transform: skew(0.96deg);
            }}
            15% {{
                clip: rect(25px, 9999px, 20px, 0);
                transform: skew(0.32deg);
            }}
            20% {{
                clip: rect(96px, 9999px, 87px, 0);
                transform: skew(0.2deg);
            }}
            25% {{
                clip: rect(99px, 9999px, 33px, 0);
                transform: skew(0.82deg);
            }}
            30% {{
                clip: rect(22px, 9999px, 5px, 0);
                transform: skew(0.15deg);
            }}
            35% {{
                clip: rect(18px, 9999px, 72px, 0);
                transform: skew(0.01deg);
            }}
            40% {{
                clip: rect(71px, 9999px, 78px, 0);
                transform: skew(0.65deg);
            }}
            45% {{
                clip: rect(29px, 9999px, 98px, 0);
                transform: skew(0.4deg);
            }}
            50% {{
                clip: rect(61px, 9999px, 75px, 0);
                transform: skew(0.21deg);
            }}
            55% {{
                clip: rect(62px, 9999px, 59px, 0);
                transform: skew(0.95deg);
            }}
            60% {{
                clip: rect(44px, 9999px, 27px, 0);
                transform: skew(0.25deg);
            }}
            65% {{
                clip: rect(84px, 9999px, 92px, 0);
                transform: skew(0.33deg);
            }}
            70% {{
                clip: rect(5px, 9999px, 33px, 0);
                transform: skew(0.5deg);
            }}
            75% {{
                clip: rect(19px, 9999px, 10px, 0);
                transform: skew(0.51deg);
            }}
            80% {{
                clip: rect(59px, 9999px, 65px, 0);
                transform: skew(0.76deg);
            }}
            85% {{
                clip: rect(90px, 9999px, 32px, 0);
                transform: skew(0.12deg);
            }}
            90% {{
                clip: rect(61px, 9999px, 96px, 0);
                transform: skew(0.02deg);
            }}
            95% {{
                clip: rect(38px, 9999px, 3px, 0);
                transform: skew(0.09deg);
            }}
            100% {{
                clip: rect(79px, 9999px, 93px, 0);
                transform: skew(0.6deg);
            }}
        }}
        
        @keyframes glitch-anim2 {{
            0% {{
                clip: rect(36px, 9999px, 50px, 0);
                transform: skew(0.49deg);
            }}
            5% {{
                clip: rect(50px, 9999px, 73px, 0);
                transform: skew(0.52deg);
            }}
            10% {{
                clip: rect(83px, 9999px, 59px, 0);
                transform: skew(0.75deg);
            }}
            15% {{
                clip: rect(96px, 9999px, 90px, 0);
                transform: skew(0.07deg);
            }}
            20% {{
                clip: rect(35px, 9999px, 72px, 0);
                transform: skew(0.01deg);
            }}
            25% {{
                clip: rect(38px, 9999px, 65px, 0);
                transform: skew(0.65deg);
            }}
            30% {{
                clip: rect(69px, 9999px, 5px, 0);
                transform: skew(0.42deg);
            }}
            35% {{
                clip: rect(57px, 9999px, 12px, 0);
                transform: skew(0.48deg);
            }}
            40% {{
                clip: rect(17px, 9999px, 7px, 0);
                transform: skew(0.68deg);
            }}
            45% {{
                clip: rect(33px, 9999px, 42px, 0);
                transform: skew(0.92deg);
            }}
            50% {{
                clip: rect(4px, 9999px, 89px, 0);
                transform: skew(0.28deg);
            }}
            55% {{
                clip: rect(57px, 9999px, 19px, 0);
                transform: skew(0.85deg);
            }}
            60% {{
                clip: rect(14px, 9999px, 55px, 0);
                transform: skew(0.63deg);
            }}
            65% {{
                clip: rect(12px, 9999px, 57px, 0);
                transform: skew(0.25deg);
            }}
            70% {{
                clip: rect(70px, 9999px, 89px, 0);
                transform: skew(0.18deg);
            }}
            75% {{
                clip: rect(61px, 9999px, 30px, 0);
                transform: skew(0.77deg);
            }}
            80% {{
                clip: rect(86px, 9999px, 32px, 0);
                transform: skew(0.99deg);
            }}
            85% {{
                clip: rect(7px, 9999px, 25px, 0);
                transform: skew(0.44deg);
            }}
            90% {{
                clip: rect(34px, 9999px, 10px, 0);
                transform: skew(0.56deg);
            }}
            95% {{
                clip: rect(57px, 9999px, 10px, 0);
                transform: skew(0.09deg);
            }}
            100% {{
                clip: rect(1px, 9999px, 99px, 0);
                transform: skew(0.88deg);
            }}
        }}
        
        @keyframes glitch-skew {{
            0% {{
                transform: skew(1deg);
            }}
            10% {{
                transform: skew(0deg);
            }}
            20% {{
                transform: skew(1deg);
            }}
            30% {{
                transform: skew(0deg);
            }}
            40% {{
                transform: skew(-0.5deg);
            }}
            50% {{
                transform: skew(-1deg);
            }}
            60% {{
                transform: skew(0deg);
            }}
            70% {{
                transform: skew(-0.8deg);
            }}
            80% {{
                transform: skew(-0.3deg);
            }}
            90% {{
                transform: skew(0.5deg);
            }}
            100% {{
                transform: skew(0deg);
            }}
        }}
        
        .neon-border {{
            position: relative;
            border: 1px solid var(--neon-blue);
            box-shadow: 0 0 10px var(--neon-blue),
                        inset 0 0 10px var(--neon-blue);
            animation: flicker 3s infinite alternate;
        }}
        
        .neon-pink-border {{
            position: relative;
            border: 1px solid var(--neon-pink);
            box-shadow: 0 0 10px var(--neon-pink),
                        inset 0 0 10px var(--neon-pink);
            animation: flicker 4s infinite alternate;
        }}
        
        .neon-green-border {{
            position: relative;
            border: 1px solid var(--neon-green);
            box-shadow: 0 0 10px var(--neon-green),
                        inset 0 0 10px var(--neon-green);
            animation: flicker 5s infinite alternate;
        }}
        
        .neon-purple-border {{
            position: relative;
            border: 1px solid var(--neon-purple);
            box-shadow: 0 0 10px var(--neon-purple),
                        inset 0 0 10px var(--neon-purple);
            animation: flicker 6s infinite alternate;
        }}
        
        @keyframes flicker {{
            0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {{
                opacity: 0.9;
                box-shadow: 0 0 10px currentColor,
                            inset 0 0 10px currentColor;
            }}
            20%, 24%, 55% {{
                opacity: 0.5;
                box-shadow: 0 0 5px currentColor,
                            inset 0 0 5px currentColor;
            }}
        }}
        
        .terminal {{
            background-color: rgba(0, 0, 0, 0.7);
            border: 1px solid var(--cyber-blue);
            box-shadow: 0 0 20px rgba(30, 144, 255, 0.4);
            padding: 10px;
            font-family: 'Share Tech Mono', monospace;
        }}
        
        .terminal-header {{
            border-bottom: 1px solid var(--cyber-blue);
            padding-bottom: 5px;
            margin-bottom: 10px;
            display: flex;
            justify-content: space-between;
        }}
        
        .tech-upgrade {{
            position: relative;
            padding: 15px;
            margin-bottom: 15px;
            background: linear-gradient(to right, rgba(0, 0, 0, 0.7), rgba(10, 10, 15, 0.7));
            border-left: 3px solid;
        }}
        
        .tech-upgrade-blue {{
            border-color: var(--neon-blue);
        }}
        
        .tech-upgrade-pink {{
            border-color: var(--neon-pink);
        }}
        
        .tech-upgrade-green {{
            border-color: var(--neon-green);
        }}
        
        .tech-upgrade-purple {{
            border-color: var(--neon-purple);
        }}
        
        .progress-container {{
            height: 8px;
            background-color: rgba(0, 0, 0, 0.5);
            border-radius: 4px;
            overflow: hidden;
            margin-top: 8px;
        }}
        
        .progress-bar {{
            height: 100%;
            border-radius: 4px;
            position: relative;
            overflow: hidden;
        }}
        
        .progress-bar::after {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(
                90deg,
                rgba(255, 255, 255, 0) 0%,
                rgba(255, 255, 255, 0.5) 50%,
                rgba(255, 255, 255, 0) 100%
            );
            animation: shimmer 2s infinite;
            transform: translateX(-100%);
        }}
        
        @keyframes shimmer {{
            100% {{
                transform: translateX(100%);
            }}
        }}
        
        .grid-lines {{
            background-size: 40px 40px;
            background-image: linear-gradient(to right, rgba(30, 144, 255, 0.1) 1px, transparent 1px),
                              linear-gradient(to bottom, rgba(30, 144, 255, 0.1) 1px, transparent 1px);
            background-position: 0 0;
        }}
        
        .cyber-btn {{
            position: relative;
            display: inline-block;
            padding: 8px 16px;
            color: white;
            text-transform: uppercase;
            background: transparent;
            border: 1px solid;
            letter-spacing: 2px;
            overflow: hidden;
            transition: 0.2s;
            font-family: 'Orbitron', sans-serif;
        }}
        
        .cyber-btn:hover {{
            background: currentColor;
            color: black;
            box-shadow: 0 0 10px currentColor;
            transition-delay: 0.1s;
        }}
        
        .cyber-btn::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                90deg,
                transparent,
                rgba(255, 255, 255, 0.4),
                transparent
            );
            transition: 0.5s;
        }}
        
        .cyber-btn:hover::before {{
            left: 100%;
        }}
        
        .flicker-text {{
            animation: textFlicker 3s infinite alternate;
        }}
        
        @keyframes textFlicker {{
            0%, 19.999%, 22%, 62.999%, 64%, 64.999%, 70%, 100% {{
                opacity: 0.99;
                text-shadow: 0 0 4px #fff, 0 0 11px #fff, 0 0 19px currentColor;
            }}
            20%, 21.999%, 63%, 63.999%, 65%, 69.999% {{
                opacity: 0.4;
                text-shadow: none;
            }}
        }}
        
        .chip {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 2px;
            font-size: 0.8rem;
            margin: 2px;
            background-color: rgba(0, 0, 0, 0.5);
            border: 1px solid;
        }}
        
        .section-header {{
            position: relative;
            padding-bottom: 10px;
            margin-bottom: 20px;
            overflow: hidden;
        }}
        
        .section-header::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: linear-gradient(to right, var(--neon-blue), var(--neon-pink));
        }}
        
        .project-card {{
            padding: 15px;
            margin-bottom: 20px;
            background: rgba(0, 0, 0, 0.5);
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
        }}
        
        .code-overlay {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            opacity: 0.07;
            z-index: 0;
        }}
        
        .flicker-slow {{
            animation: slowFlicker 8s infinite alternate;
        }}
        
        @keyframes slowFlicker {{
            0%, 80%, 100% {{
                opacity: 1;
            }}
            90% {{
                opacity: 0.7;
            }}
        }}
        
        @media print {{
            .cv-container {{
                box-shadow: none !important;
                margin: 0 !important;
                padding: 20px !important;
            }}
            
            body {{
                background: none !important;
            }}
            
            @page {{
                size: A4;
                margin: 0;
            }}
        }}
    </style>
</head>
<body class="background-circuit">
    <div class="scanlines"></div>
    
    <div class="cv-container mt-8 mb-8 relative">
        <div class="code-overlay mono text-xs text-gray-600">
            # CODE SEGMENT 0x1F4A8
            function inject_skills() {{
                const skill_matrix = [];
                let neural_path = new Path();
                for (const skill of user.skills) {{
                    skill_matrix.push(new NeuralNode(skill));
                    neural_path.connect(skill);
                }}
                return neural_path.optimize();
            }}
            
            class Experience extends MemorySegment {{
                constructor(data) {{
                    super(data);
                    this.encryptionLevel = 'maximum';
                    this.accessLevel = 'restricted';
                }}
                
                async process() {{
                    const result = await this.decrypt();
                    return result.enhance();
                }}
            }}
            
            // INJECT CORE MEMORIES
            const CORE_SYSTEM = new CyberCore({{
                user: "{data['personal_info']['name'].upper().replace(' ', '_')}",
                systemAccess: true,
                enhancementLevel: 10
            }});
            
            CORE_SYSTEM.boot();
        </div>
        
        <!-- HEADER SECTION -->
        <header class="p-6 neon-border grid-lines relative mb-8">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center">
                <div class="glitch-container mb-4 md:mb-0">
                    <h1 class="text-4xl md:text-5xl orbitron font-bold text-white text-glitch" data-text="{data['personal_info']['name'].upper()}">{data['personal_info']['name'].upper()}</h1>
                    <div class="text-xl md:text-2xl mono text-gray-400 flicker-text mt-2" style="color: var(--neon-pink);">{data['personal_info']['title'].upper()}</div>
                </div>
                
                <div class="terminal p-3 w-full md:w-auto">
                    <div class="terminal-header text-xs">
                        <span class="text-green-400">SYSTEM ACCESS GRANTED</span>
                        <span class="text-yellow-400">[ENCRYPTED]</span>
                    </div>
                    <div class="flex flex-col">
                        <span class="text-blue-400">$ cat contact.dat</span>
                        <span class="text-gray-300 text-sm"><i class="fas fa-map-marker-alt mr-2" style="color: var(--neon-blue);"></i>{data['personal_info'].get('location', '')}</span>
                        <span class="text-gray-300 text-sm"><i class="fas fa-envelope mr-2" style="color: var(--neon-blue);"></i>{data['personal_info']['email']}</span>"""

    # Add phone if available
    if 'phone' in data['personal_info']:
        html_content += f"""
                        <span class="text-gray-300 text-sm"><i class="fas fa-phone-alt mr-2" style="color: var(--neon-blue);"></i>{data['personal_info']['phone']}</span>"""

    html_content += f"""
                        <span class="text-gray-300 text-sm"><i class="fas fa-flag mr-2" style="color: var(--neon-blue);"></i>{data['personal_info'].get('citizenship', '')}</span>
                    </div>
                </div>
            </div>
        </header>
        
        <!-- PROFILE SECTION -->
        <section class="mb-10 relative">
            <div class="section-header">
                <h2 class="text-2xl orbitron font-bold mb-4 flicker-text" style="color: var(--neon-blue);">> SYSTEM PROFILE</h2>
            </div>
            
            <div class="terminal p-4">
                <div class="terminal-header text-xs">
                    <span class="text-green-400">profile.exe</span>
                    <span class="text-yellow-400">[ADMIN]</span>
                </div>
                <p class="text-gray-300 mono text-sm leading-relaxed">
                    {data['professional_summary']}
                </p>
            </div>
        </section>
        
        <!-- SKILLS SECTION -->
        <section class="mb-10 relative">
            <div class="section-header">
                <h2 class="text-2xl orbitron font-bold mb-4 flicker-text" style="color: var(--neon-pink);">> AUGMENTATIONS</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Programming Skills -->
                <div class="tech-upgrade tech-upgrade-blue neon-border">
                    <h3 class="text-lg orbitron font-bold mb-3" style="color: var(--neon-blue);">PROGRAMMING MODS</h3>"""

    # Add programming languages with progress bars
    for lang in data['skills']['programming_languages']:
        percent = lang['proficiency'].replace('%', '')
        html_content += f"""
                    <div class="mb-4">
                        <div class="flex justify-between items-center mb-1">
                            <span class="mono text-sm">{lang['name'].upper()}</span>
                            <span class="mono text-xs text-gray-400">v{int(percent)/10:.1f}</span>
                        </div>
                        <div class="progress-container">
                            <div class="progress-bar" style="width: {percent}%; background-color: var(--neon-blue);"></div>
                        </div>
                    </div>"""

    html_content += f"""
                </div>
                
                <!-- Cloud Skills -->
                <div class="tech-upgrade tech-upgrade-pink neon-pink-border">
                    <h3 class="text-lg orbitron font-bold mb-3" style="color: var(--neon-pink);">CLOUD NEURAL IMPLANTS</h3>
                    
                    <div class="grid grid-cols-2 gap-2">"""

    # Add cloud technologies
    for tech in data['skills']['cloud_technologies']:
        html_content += f"""
                        <div class="chip" style="border-color: var(--neon-pink);">
                            <span class="mono text-xs">{tech}</span>
                        </div>"""

    html_content += f"""
                    </div>
                </div>
                
                <!-- AI/ML Skills -->
                <div class="tech-upgrade tech-upgrade-green neon-green-border">
                    <h3 class="text-lg orbitron font-bold mb-3" style="color: var(--neon-green);">AI ENHANCEMENTS</h3>
                    
                    <div class="grid grid-cols-2 gap-2">"""

    # Add AI/ML skills
    for ai_skill in data['skills']['ai_ml']:
        html_content += f"""
                        <div class="chip" style="border-color: var(--neon-green);">
                            <span class="mono text-xs">{ai_skill}</span>
                        </div>"""

    html_content += f"""
                    </div>
                </div>
                
                <!-- DevOps Skills -->
                <div class="tech-upgrade tech-upgrade-purple neon-purple-border">
                    <h3 class="text-lg orbitron font-bold mb-3" style="color: var(--neon-purple);">DEVOPS UPGRADES</h3>
                    
                    <div class="grid grid-cols-2 gap-2">"""

    # Add DevOps skills
    for devops_skill in data['skills']['devops']:
        html_content += f"""
                        <div class="chip" style="border-color: var(--neon-purple);">
                            <span class="mono text-xs">{devops_skill}</span>
                        </div>"""

    html_content += f"""
                    </div>
                </div>
            </div>
        </section>
        
        <!-- EXPERIENCE SECTION -->
        <section class="mb-10 relative">
            <div class="section-header">
                <h2 class="text-2xl orbitron font-bold mb-4 flicker-text" style="color: var(--neon-blue);">> MISSION LOGS</h2>
            </div>"""

    # Add work experience
    for i, exp in enumerate(data['work_experience']):
        # Generate unique color for each experience
        colors = ['green', 'pink', 'blue', 'purple', 'green']
        color = colors[i % len(colors)]
        
        html_content += f"""
            <!-- Experience {i+1} -->
            <div class="mb-6 terminal p-4 flicker-slow">
                <div class="terminal-header text-xs">
                    <span class="text-green-400">{exp['company'].upper().replace(' ', '_')}.log</span>
                    <span class="text-yellow-400">[{exp['period']}]</span>
                </div>
                
                <div class="mb-2">
                    <h3 class="orbitron font-bold text-lg text-white">{exp['company'].upper()}</h3>
                    <div class="text-sm mono" style="color: var(--neon-{color});">{exp['position']}</div>
                </div>
                
                <ul class="list-disc ml-5 text-sm mono text-gray-300 space-y-2 mt-3">"""

        for responsibility in exp['responsibilities']:
            html_content += f"""
                    <li>{responsibility}</li>"""

        html_content += """
                </ul>
            </div>"""

    html_content += f"""
        </section>
        
        <!-- PROJECTS SECTION -->
        <section class="mb-10 relative">
            <div class="section-header">
                <h2 class="text-2xl orbitron font-bold mb-4 flicker-text" style="color: var(--neon-pink);">> SIDE QUESTS</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">"""

    # Add projects
    for i, project in enumerate(data['projects']):
        # Generate unique border color for each project
        border_colors = ['blue', 'pink', 'green', 'purple']
        border_color = border_colors[i % len(border_colors)]
        
        html_content += f"""
                <!-- Project {i+1} -->
                <div class="project-card neon-{border_color}-border">
                    <h3 class="orbitron font-bold text-lg mb-2" style="color: var(--neon-{border_color});">{project['name'].upper()}</h3>
                    <div class="text-xs mono mb-3 text-gray-400">[PROJECT STATUS: {project.get('status', 'COMPLETE').upper()}]</div>
                    
                    <p class="text-sm mono text-gray-300 mb-4">{project['description']}</p>
                    
                    <div class="flex flex-wrap">"""

        for tech in project['technologies']:
            html_content += f"""
                        <div class="chip text-xs" style="border-color: var(--neon-{border_color});">{tech}</div>"""

        html_content += """
                    </div>
                </div>"""

    html_content += f"""
            </div>
        </section>
        
        <!-- EDUCATION & CERTIFICATIONS -->
        <section class="mb-10 relative">
            <div class="section-header">
                <h2 class="text-2xl orbitron font-bold mb-4 flicker-text" style="color: var(--neon-blue);">> NEURAL TRAINING</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Education -->
                <div class="terminal p-4">
                    <div class="terminal-header text-xs">
                        <span class="text-green-400">education.dat</span>
                        <span class="text-yellow-400">[VALIDATED]</span>
                    </div>
                    
                    <div class="mb-2">
                        <h3 class="orbitron font-bold text-lg text-white">EDUCATION</h3>
                    </div>"""

    # Add education
    for edu in data['education']:
        html_content += f"""
                    <div class="flex justify-between items-start mb-3">
                        <div>
                            <div class="mono text-sm text-gray-300">{edu['degree']}</div>
                        </div>
                        <div class="mono text-xs" style="color: var(--neon-green);">{edu['year']}</div>
                    </div>"""

    html_content += f"""
                </div>
                
                <!-- Certifications -->
                <div class="terminal p-4">
                    <div class="terminal-header text-xs">
                        <span class="text-green-400">certifications.dat</span>
                        <span class="text-yellow-400">[VALIDATED]</span>
                    </div>
                    
                    <div class="mb-2">
                        <h3 class="orbitron font-bold text-lg text-white">CERTIFICATIONS</h3>
                    </div>"""

    # Add certifications
    for i, cert in enumerate(data['certifications']):
        colors = ['green', 'pink', 'blue', 'purple']
        color = colors[i % len(colors)]
        
        html_content += f"""
                    <div class="flex justify-between items-start mb-3">
                        <div>
                            <div class="mono text-sm text-gray-300">{cert['name']}</div>
                        </div>
                        <div class="mono text-xs" style="color: var(--neon-{color});">{cert['year']}{' (Planned)' if i > 0 and cert.get('planned', False) else ''}</div>
                    </div>"""

    html_content += f"""
                </div>
            </div>
        </section>
        
        <!-- REFERENCES SECTION -->
        <section class="mb-6 relative">
            <div class="section-header">
                <h2 class="text-2xl orbitron font-bold mb-4 flicker-text" style="color: var(--neon-purple);">> TRUSTED CONTACTS</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">"""

    # Add references
    for i, ref in enumerate(data['references']):
        colors = ['purple', 'blue', 'green', 'pink']
        color = colors[i % len(colors)]
        
        html_content += f"""
                <!-- Reference {i+1} -->
                <div class="tech-upgrade tech-upgrade-{color}">
                    <h3 class="mono font-bold text-base mb-1" style="color: var(--neon-{color});">{ref['name'].upper()}</h3>
                    <div class="text-sm mono text-gray-400 mb-2">{ref['position']}</div>
                    <div class="text-sm mono text-gray-300">
                        <i class="fas fa-phone-alt mr-2" style="color: var(--neon-{color});"></i> {ref['phone']}
                    </div>
                </div>"""

    html_content += f"""
            </div>
        </section>
        
        <!-- FOOTER -->
        <footer class="text-center p-4 border-t border-gray-800 mt-8">
            <div class="text-xs mono text-gray-500">
                [document.classification: public] | [access.level: unrestricted] | [system.status: online]
            </div>
            <div class="text-xs mono text-gray-500 mt-1">
                © {datetime.now().year} {data['personal_info']['name'].upper()} | SYSTEM VERSION 4.7.2
            </div>
        </footer>
    </div>
    
    <script>
        // Add random glitch effect to elements with glitch-text class
        function addRandomGlitch() {{
            const glitchElements = document.querySelectorAll('.text-glitch');
            
            glitchElements.forEach(element => {{
                // Random chance to trigger glitch effect
                if (Math.random() < 0.1) {{
                    element.style.textShadow = `${{Math.random() * 10 - 5}}px ${{Math.random() * 10 - 5}}px rgba(255, 42, 109, 0.7)`;
                    
                    // Reset after a short duration
                    setTimeout(() => {{
                        element.style.textShadow = '';
                    }}, 100 + Math.random() * 200);
                }}
            }});
            
            setTimeout(addRandomGlitch, 2000 + Math.random() * 3000);
        }}
        
        // Start the random glitch effect
        addRandomGlitch();
    </script>
</body>
</html>"""

    # Write to output file
    with open(output_file_path, 'w') as f:
        f.write(html_content)
    
    print(f"Cyberpunk CV generated successfully at {output_file_path}")