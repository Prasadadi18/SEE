
pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'BUILD: Installing Flask dependencies'

                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'TEST: Running unit tests'

                sh 'venv/bin/python -m unittest discover -s . -p "test_*.py"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'DEPLOY: Deploying Flask application'

                sh 'mkdir -p deployment'
                sh 'cp app.py requirements.txt deployment/'

                sh 'ls -l deployment/'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
