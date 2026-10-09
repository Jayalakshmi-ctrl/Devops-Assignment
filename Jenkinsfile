pipeline {
    agent {
        // This tells Jenkins to pull a clean Python container to execute the steps safely
        docker { 
            image 'python:3.11-slim' 
        }
    }
    
    stages {
        stage('Clean Environment Setup') {
            steps {
                // Installs dependencies cleanly inside the isolated runtime space
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }
        
        stage('Compilation & Execution Check') {
            steps {
                // Validates your application module for any syntax structural errors
                sh 'python -m py_compile app.py'
            }
        }

        stage('Automated Test Verification') {
            steps {
                // Runs the complete Pytest validation suite
                sh 'pytest -v test_app.py'
            }
        }
    }
}
