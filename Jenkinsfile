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
    
    stage('create volume') {
      agent any
            steps {
                sh 'docker volume create data'
            }
        }
   stage('Run Docker') {
     agent any
            steps {
                sh 'docker run -v $(pwd)/kp:/data sel'
            }
        }
                 stage ('Test') {
                   agent any
                   steps{
                     sh "ls"
                     sh "pwd"
                   }
                  post {
                     success{
                      // publish html
                      //publishHTML target: [
                        //  allowMissing: false,
                        //  alwaysLinkToLastBuild: true,
                         // keepAll: true,
                          //reportDir: '/Users/aaa/.jenkins/workspace/docker_container/kp',
                          //reportFiles: 'report.html'
                        //]
                    sh "ls"
                   }
                 }
                 }
  }
}
