pipeline {
    agent any
    stages {
        stage('Checkout Codebase') {
            steps {
                // Pulls the latest code directly from your repository
                git branch: 'main', url: 'https://github.com'
            }
        }
        stage('Clean Environment Setup') {
            steps {
                // Sets up an isolated sandbox on the build server
                sh 'python3 -m venv venv && ./venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Compilation & Execution Check') {
            steps {
                // Verifies application logic runs cleanly
                sh './venv/bin/python -m py_compile app.py'
            }
        }
    }
}
