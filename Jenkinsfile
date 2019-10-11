pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
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