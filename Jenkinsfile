pipeline {
  agent none
  stages {
    stage('Create a virtual environment') {
      agent {
        docker{
          image 'python:3.5.7-alpine3.8'
          args '-u 0:0'
        }
      }
      steps {
        echo 'Create the virtual environment'
        sh 'pip3 install virtualenv'
        sh 'virtualenv env'
        sh 'source env/bin/activate'
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
