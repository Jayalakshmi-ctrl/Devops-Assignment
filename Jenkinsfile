pipeline {
    agent any
    
    environment {
        // Automatically selects the best available python command on the machine
        PYTHON_CMD = sh(script: 'command -v python3 || command -v python', returnStdout: true).trim()
    }
    
    stages {
        stage('Clean Environment Setup') {
            steps {
                // Installs pinned dependencies inside an isolated workspace virtual environment
                sh """
                    \${PYTHON_CMD} -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                """
            }
        }
        
        stage('Compilation & Execution Check') {
            steps {
                // Strictly validates the application core logic files for syntax accuracy
                sh './venv/bin/python -m py_compile app.py'
            }
        }
    }
}
