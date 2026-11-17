pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                bat 'npm ci'
            }
        }

        stage('Test') {
            steps {
                bat 'npx playwright test'
            }
        }
    }
}
