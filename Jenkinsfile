pipeline {
    agent any
    
    stages {
        stage('Clean Environment Setup') {
            steps {
                // Installs your exact pinned dependencies safely into the workspace
                sh '''
                    python3 -m venv venv || python -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }
        
        stage('Compilation Check') {
            steps {
                // Strictly verifies your Flask application structure for syntax accuracy
                sh './venv/bin/python -m py_compile app.py'
            }
        }

        stage('Automated Test Verification') {
            steps {
                // Executes the full Pytest suite for API endpoint logic routing verification
                sh './venv/bin/pytest -v test_app.py'
            }
        }
    }
}
