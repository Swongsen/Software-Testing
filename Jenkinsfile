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
            checkout scm
            docker.image('mysql').withRun('-e "MYSQL_ROOT_PASSWORD=password"') { c ->
                docker.image('mysql').inside("--link ${c.id}:db") {
                    /* Wait until mysql service is up */
                    sh 'while ! mysqladmin ping -hdb --silent; do sleep 1; done'
                }
                docker.image('python:3').inside("--link ${c.id}:db") {
                    /*
                    * Run some tests which require MySQL, and assume that it is
                    * available on the host name `db`
                    */
                    sh 'pytest PPA1/a1test.py'
                }
            }
        }
    }
}