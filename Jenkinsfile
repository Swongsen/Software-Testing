pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
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
                sh 'py.test --verbose --junit-xml PPA1/test-reports/results.xml PPA1/a1test.py'
            }
            post {
                always {
                    junit 'PPA1/test-reports/results.xml'
                }
            }
        }
    }
}