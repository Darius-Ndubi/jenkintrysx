pipeline {
  agent {
    kubernetes {
      label 'jenkins-trx'
      defaultContainer 'jnlp'
      yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
  component: ci
spec:
  containers:
  - name: kubepod
    image: python:3.5.7-alpine3.8
    resources:
      requests:
        cpu: "500m"
        memory: "1Gi"
      limits:
        cpu: "800m"
        memory: "2Gi"
    command:
    - cat
    tty: true
"""
    }
  }
  stages {
    stage('Create a virtual environment') {
      steps {
        echo 'Create the virtual environment'
        sh 'echo "Hello world!!"'
        sh 'apk add python3-dev'
        sh 'apk add build-base'
        sh 'apk add gcc'
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
