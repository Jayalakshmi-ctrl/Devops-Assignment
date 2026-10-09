pipeline {
    agent any
    
    stages {
        stage('Docker Image Construction') {
            steps {
                // Compiles and packs your Flask app layout cleanly using your local Dockerfile
                sh 'docker build -t aceest-fitness-build:${BUILD_NUMBER} .'
            }
        }
        
        stage('Automated Test Verification') {
            steps {
                // Executes your Pytest validation blocks safely inside the isolated container
                sh 'docker run --rm aceest-fitness-build:${BUILD_NUMBER} pytest -v test_app.py'
            }
        }
        
        stage('Cleanup Local Images') {
            steps {
                // Removes old cache image profiles to optimize your local disk space
                sh "docker rmi aceest-fitness-build:\${BUILD_NUMBER}"
            }
        }
    }
}
