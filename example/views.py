from django.http import HttpResponse
from datetime import datetime

def index(request):
    # Get the current time
    now = datetime.now()

    # Define the HTML content for the portfolio page
    html = f'''
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Basudev Ghadai - Backend Developer Portfolio</title>
            <!-- Content Security Policy -->
            <meta http-equiv="Content-Security-Policy" content="default-src 'self'; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; script-src 'self' https://cdn.jsdelivr.net;">
            
            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEJ4QJ2nK6FLp4R4X9n6Xg6Vf5X7cm5g6z3ZSH1iF3BzV5V9UjFplzSkIRs4u" crossorigin="anonymous">
        </head>
        <body>
            <div class="container">
                <header class="my-4 text-center">
                    <h1>Basudev Ghadai</h1>
                    <p class="lead">Python Backend Developer | AI Enthusiast</p>
                    <p>The current time is {now}.</p>
                </header>

                <!-- About Me Section -->
                <section class="mb-5">
                    <h2>About Me</h2>
                    <p>Hello, I'm Basudev Ghadai, a skilled Python Backend Developer with experience in Odoo, Flask, AI/ML, and Generative AI. My expertise lies in building scalable backend solutions, integrating APIs, and developing robust systems that solve complex problems efficiently.</p>
                </section>

                <!-- Skills Section -->
                <section class="mb-5">
                    <h2>Skills</h2>
                    <div class="row">
                        <div class="col-md-4">
                            <h4>Programming Languages</h4>
                            <ul>
                                <li>Python</li>
                                <li>JavaScript</li>
                                <li>HTML/CSS</li>
                                <li>SQL</li>
                            </ul>
                        </div>
                        <div class="col-md-4">
                            <h4>Frameworks & Tools</h4>
                            <ul>
                                <li>Django</li>
                                <li>Flask</li>
                                <li>Odoo</li>
                                <li>Generative AI (LangChain, Hugging Face)</li>
                            </ul>
                        </div>
                        <div class="col-md-4">
                            <h4>Databases</h4>
                            <ul>
                                <li>PostgreSQL</li>
                                <li>MySQL</li>
                                <li>MongoDB</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Experience Section -->
                <section class="mb-5">
                    <h2>Experience</h2>
                    <div class="mb-3">
                        <h4>Software Developer at Sapat International Pvt Ltd</h4>
                        <p><strong>April 2024 – Present</strong></p>
                        <ul>
                            <li>Developed and maintained web applications using Python and Flask</li>
                            <li>Customized Odoo ERP modules based on business requirements</li>
                            <li>Worked with OpenedX to create and customize LMS features</li>
                            <li>Collaborated with cross-functional teams to deliver scalable solutions</li>
                        </ul>
                    </div>
                    <div class="mb-3">
                        <h4>Python Backend Developer at Confluex Marketing Pvt Ltd</h4>
                        <p><strong>May 2022 – November 2022</strong></p>
                        <ul>
                            <li>Wrote scalable code to improve application responsiveness</li>
                            <li>Integrated user-facing elements into backend services</li>
                            <li>Developed APIs for seamless communication between systems</li>
                        </ul>
                    </div>
                </section>

                <!-- Projects Section -->
                <section class="mb-5">
                    <h2>Projects</h2>
                    <div class="row">
                        <div class="col-md-4 mb-3">
                            <div class="card">
                                <div class="card-body">
                                    <h5 class="card-title">QR4Order API</h5>
                                    <p class="card-text">Developed an API for streamlining order management in restaurants.</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4 mb-3">
                            <div class="card">
                                <div class="card-body">
                                    <h5 class="card-title">OpenedX LMS Platform</h5>
                                    <p class="card-text">Customized and deployed an LMS using OpenedX, enhancing e-learning experiences.</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4 mb-3">
                            <div class="card">
                                <div class="card-body">
                                    <h5 class="card-title">Self-Driving Car Lane Detection</h5>
                                    <p class="card-text">Implemented a lane detection system using OpenCV, deployed with Streamlit.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Contact Section -->
                <section>
                    <h2>Contact</h2>
                    <p>Interested in working with me? Feel free to reach out:</p>
                    <ul>
                        <li>Email: basudev.ghadai@example.com</li>
                        <li>LinkedIn: <a href="https://www.linkedin.com/in/basudev-ghadai">linkedin.com/in/basudev-ghadai</a></li>
                        <li>GitHub: <a href="https://github.com/biplab-tech-guy">github.com/biplab-tech-guy</a></li>
                    </ul>
                </section>
            </div>

            <!-- Bootstrap JS and Popper.js -->
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz4fnFO9gyb7xD8k6t/dlzdD8e4d6bbT7blFEvBktD2LkGQ4xe6pAkKeiV2" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js" integrity="sha384-pzjw8f+ua7Kw1TIq0tGz1K5u/4osQFeK6hr6kXQ2Yo4CuT3V0z0wiv5u5O0p9C9z" crossorigin="anonymous"></script>
        </body>
    </html>
    '''
    
    return HttpResponse(html)
