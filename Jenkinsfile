pipeline {
    agent {
	docker { image 'python:3' }
    }
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'python -m py_compile PPA1/a1.py'
		sh 'pip install pytest'
		sh 'pip install mysql'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest PPA1/a1test.py'
            }
        }
    }
}