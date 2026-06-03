pipeline {

    agent any

    parameters {
        string(
            name: 'TEST_TARGET',
            defaultValue: 'tests/test_fixtures.py',
            description: 'Enter pytest file or test case'
        )
    }

    stages {

        stage('Checkout Code') {
            steps {
                git(
                    url: 'https://github.com/akshayrawat007/Selenium-Automation-Python.git',
                    branch: 'main',
                    credentialsId: 'github_1'
                )
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat "pytest ${params.TEST_TARGET} -v"
            }
        }
    }
}