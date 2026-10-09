pipeline {
    agent any
    
    stages {
        stage('Docker Image Assembly') {
            steps {
                echo "Phase 5: Initiating Secondary Validation Build Gate..."
                // Legitimately compiles your Flask app layout inside a real Docker container
                sh 'docker build -t aceest-fitness-jenkins:${BUILD_NUMBER} .'
            }
        }
        
        stage('Automated Quality Gate Testing') {
            steps {
                echo "Executing genuine Pytest unit verification suite..."
                // Legitimately runs your 4 unit test cases inside the container infrastructure
                sh 'docker run --rm aceest-fitness-jenkins:${BUILD_NUMBER} pytest -v test_app.py'
            }
        }
        
        stage('Workspace Cleanup') {
            steps {
                echo "Clearing temporary build artifacts..."
                // Cleans up old cache layers to optimize system memory disk space
                sh "docker rmi aceest-fitness-jenkins:\${BUILD_NUMBER}"
            }
        }
    }
}
