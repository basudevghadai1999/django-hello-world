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
            <title>Backend Developer Portfolio</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEJ4QJ2nK6FLp4R4X9n6Xg6Vf5X7cm5g6z3ZSH1iF3BzV5V9UjFplzSkIRs4u" crossorigin="anonymous">
        </head>
        <body>
            <div class="container">
                <header class="my-4 text-center">
                    <h1>John Doe</h1>
                    <p class="lead">Backend Developer</p>
                    <p>The current time is {now}.</p>
                </header>

                <!-- About Me Section -->
                <section class="mb-5">
                    <h2>About Me</h2>
                    <p>Hello, I'm John Doe, a passionate backend developer with a strong background in server-side technologies. I specialize in designing scalable and efficient APIs, working with databases, and integrating third-party services. My goal is to create robust backend systems that power high-performing applications.</p>
                </section>

                <!-- Skills Section -->
                <section class="mb-5">
                    <h2>Skills</h2>
                    <div class="row">
                        <div class="col-md-4">
                            <h4>Programming Languages</h4>
                            <ul>
                                <li>Python</li>
                                <li>JavaScript (Node.js)</li>
                                <li>Java</li>
                                <li>PHP</li>
                            </ul>
                        </div>
                        <div class="col-md-4">
                            <h4>Frameworks & Tools</h4>
                            <ul>
                                <li>Django</li>
                                <li>Flask</li>
                                <li>Express.js</li>
                                <li>Spring Boot</li>
                            </ul>
                        </div>
                        <div class="col-md-4">
                            <h4>Databases</h4>
                            <ul>
                                <li>PostgreSQL</li>
                                <li>MySQL</li>
                                <li>MongoDB</li>
                                <li>Redis</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Experience Section -->
                <section class="mb-5">
                    <h2>Experience</h2>
                    <div class="mb-3">
                        <h4>Backend Developer at TechCorp</h4>
                        <p><strong>January 2021 – Present</strong></p>
                        <ul>
                            <li>Designed and implemented RESTful APIs using Django and Flask</li>
                            <li>Optimized database queries for better performance with PostgreSQL</li>
                            <li>Collaborated with frontend developers to ensure seamless integration of backend services</li>
                            <li>Integrated third-party payment and shipping APIs</li>
                        </ul>
                    </div>
                    <div class="mb-3">
                        <h4>Junior Backend Developer at CodeWorks</h4>
                        <p><strong>July 2018 – December 2020</strong></p>
                        <ul>
                            <li>Developed backend services using Node.js and Express</li>
                            <li>Created database schemas and wrote migration scripts for MySQL</li>
                            <li>Maintained and improved existing API endpoints</li>
                        </ul>
                    </div>
                </section>

                <!-- Projects Section -->
                <section class="mb-5">
                    <h2>Projects</h2>
                    <div class="row">
                        <div class="col-md-4 mb-3">
                            <div class="card">
                                <img src="https://via.placeholder.com/150" class="card-img-top" alt="Project 1">
                                <div class="card-body">
                                    <h5 class="card-title">Project Management API</h5>
                                    <p class="card-text">A RESTful API built with Django to manage project tasks, deadlines, and users. It integrates with Slack for notifications.</p>
                                    <a href="#" class="btn btn-primary">View Project</a>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4 mb-3">
                            <div class="card">
                                <img src="https://via.placeholder.com/150" class="card-img-top" alt="Project 2">
                                <div class="card-body">
                                    <h5 class="card-title">E-commerce Backend</h5>
                                    <p class="card-text">A scalable backend system built with Node.js and MongoDB to support an online store, including user authentication and product management.</p>
                                    <a href="#" class="btn btn-primary">View Project</a>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4 mb-3">
                            <div class="card">
                                <img src="https://via.placeholder.com/150" class="card-img-top" alt="Project 3">
                                <div class="card-body">
                                    <h5 class="card-title">Weather API</h5>
                                    <p class="card-text">A weather information API built using Flask that provides current weather data using a third-party service, with caching via Redis.</p>
                                    <a href="#" class="btn btn-primary">View Project</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Contact Section -->
                <section>
                    <h2>Contact</h2>
                    <p>If you're interested in working with me, feel free to reach out through the following:</p>
                    <ul>
                        <li>Email: johndoe@example.com</li>
                        <li>LinkedIn: <a href="https://www.linkedin.com/in/johndoe">linkedin.com/in/johndoe</a></li>
                        <li>GitHub: <a href="https://github.com/johndoe">github.com/johndoe</a></li>
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
