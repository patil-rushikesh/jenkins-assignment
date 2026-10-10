pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '.venv/bin/python -m pytest -v'
            }
        }
    }

    post {
        success {
            echo 'BUILD SUCCESSFUL'
        }
        failure {
            echo 'BUILD FAILED'
        }
    }
}