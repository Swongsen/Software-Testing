pipeline {
    agent none
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
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'pytest PPA1/test-reports/results.xml PPA1/a1test.py'
            }
            post {
                always {
                    junit 'PPA1/test-reports/results.xml'
                }
            }
        }
    }
}