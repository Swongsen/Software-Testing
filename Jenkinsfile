pipeline {
    agent {
	docker { image 'python:3' }
    }
    options {
        skipStagesAfterUnstable()
    }
    environment {
	db_name = "some-mysql"
	db_user = "root"
	db_pass = "my-secret-pw"
    }
    stages {
        stage('Build') {
            steps {
                sh 'python -m py_compile PPA1/a1.py'
		sh 'pip install pytest'
		sh 'pip install pytest-mock'
		sh 'pip install mysql-connector-python'
		sh 'pip install flask'
            }
        }
        stage('Test Original PPA1 with Database') {
            steps {
                sh 'pytest PPA1/a1test.py'
            }
        }
        stage('Test Web Interface') {
            steps {
                sh 'pytest PPA1/a1webtest.py'
            }
        }
    }
}