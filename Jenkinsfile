pipeline {
  agent any
  stages {
    stage('Create a virtual environment') {
      steps {
        echo 'Create the virtual environment'
        sh 'python3 -m virtualenv env'
        sh 'source /env/bin/activate'
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('Run_tests') {
      steps {
        sh 'nosetests  --with-coverage --cover-package=resources'
      }
    }
    stage('Deployments') {
      parallel {
        stage('Push to Docker') {
          steps {
            echo 'Image updated!'
          }
        }

        stage('Deploy to heroku') {
          steps {
            echo 'Deployed!'
          }
        }
      }
    }
    }
  }
