pipeline {
    agent any
    
    stages {
        stage('Initialize Environment') {
            steps {
                // Installs Python directly inside your workspace folder using standard Linux apt tools
                sh '''
                    if ! command -v python3 &> /dev/null; then
                        echo "Python3 not found. Installing system runtime..."
                        sudo apt-get update && sudo apt-get install -y python3 python3-pip python3-venv
                    fi
                '''
            }
        }
        
        stage('Clean Environment Setup') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }
        
        stage('Compilation & Execution Check') {
            steps {
                sh './venv/bin/python -m py_compile app.py'
            }
        }
    }
}
