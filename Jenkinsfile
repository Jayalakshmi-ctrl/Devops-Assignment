pipeline {
    agent any
    
    stages {
        stage('Docker Image Construction') {
            steps {
                // Assembles your secure Flask container using your Dockerfile
                sh 'docker build -t aceest-fitness-build:${BUILD_NUMBER} .'
            }
        }
        
        stage('Automated Test Verification') {
            steps {
                // Runs the internal Pytest suite cleanly inside the container
                sh 'docker run --rm aceest-fitness-build:${BUILD_NUMBER} pytest -v test_app.py'
            }
        }
        
        stage('Cleanup Local Images') {
            steps {
                // Removes the temporary build image to save server disk space
                sh "docker rmi aceest-fitness-build:\${BUILD_NUMBER}"
            }
        }
    }
}
