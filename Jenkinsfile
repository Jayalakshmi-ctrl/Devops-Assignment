pipeline {
    agent any
    
    stages {
        stage('Clean Environment Setup') {
            steps {
                // Downloads and unpacks a micro standalone Python runtime directly into the workspace
                sh '''
                    echo "Checking system for active Python binaries..."
                    if ! command -v python3 &> /dev/null; then
                        echo "Python runtime missing. Provisioning workspace environment..."
                        
                        # Download official portable Linux x86_64 Python build
                        curl -sSOL https://github.com
                        
                        # Unpack runtime to a local directory
                        tar -xzf cpython-3.11.7+20240107-x86_64-unknown-linux-gnu-install_only.tar.gz
                        
                        # Create symbolic links to standardize references
                        mkdir -p bin
                        ln -s $(pwd)/python/bin/python3 $(pwd)/bin/python3
                        export PATH="$(pwd)/bin:$PATH"
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
                // Strictly verifies application syntax for architectural errors
                sh './venv/bin/python -m py_compile app.py'
            }
        }

        stage('Automated Test Verification') {
            steps {
                // Executes your 4 Pytest blocks to clear the quality gate criteria
                sh './venv/bin/pytest -v test_app.py'
            }
        }
    }
}
