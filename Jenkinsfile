pipeline {
    agent any
    
    stages {
        stage('Clean Environment Setup') {
            steps {
                sh '''
                    echo "Checking system for active Python binaries..."
                    if ! command -v python3 &> /dev/null; then
                        echo "Python runtime missing. Provisioning workspace environment..."
                        
                        # Fixed URL string using backslashes to prevent truncation
                        curl -sSOL https://github.com
                        
                        echo "Unpacking runtime to a local directory..."
                        tar -xzf cpython-3.11.7+20240107-x86_64-unknown-linux-gnu-install_only.tar.gz
                        
                        mkdir -p bin
                        ln -sf $(pwd)/python/bin/python3 $(pwd)/bin/python3
                    fi
                    
                    # Construct isolated application sandbox
                    ./bin/python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }
        
        stage('Compilation Check') {
            steps {
                sh './venv/bin/python -m py_compile app.py'
            }
        }

        stage('Automated Test Verification') {
            steps {
                sh './venv/bin/pytest -v test_app.py'
            }
        }
    }
}
