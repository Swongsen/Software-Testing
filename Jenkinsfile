pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.5.1'
                }
            }
            steps {
                sh 'python -m py_compile PPA1/a1.py'
		sh 'pip install pytest'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest PPA1/a1test.py'
            }
        }
    }
}