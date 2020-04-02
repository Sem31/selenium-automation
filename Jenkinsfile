#!groovy

pipeline {
  agent none
  stages {
    stage('Docker Build') {
      agent any
      steps {
        sh 'docker build -t sel:latest .'
        //sh 'docker volume create data'
        //sh 'docker run -v $(pwd)/kp:/data sel'
      }
    }
    agent none
    stage('create volume') {
            steps {
                sh 'docker volume create data'
            }
        }
    agent none
   stage('Run Docker') {
            steps {
                sh 'docker run -v $(pwd)/kp:/data sel'
            }
        }
  }
}
