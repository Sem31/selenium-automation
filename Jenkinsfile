#!groovy

pipeline {
  agent none
  stages {
    stage('Docker Build') {
      agent any
      steps {
        sh 'docker build -t sel:latest .'
        sh 'docker create volume data'
        sh 'docker run -v $(pwd)/kp:/data sel'
      }
    }
  }
}