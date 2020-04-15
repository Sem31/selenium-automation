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
      steps{
                sh 'docker run -v $(pwd)/kp:/data sel'
            }
      post {
           always{
                      sh "pwd"
                     publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: true, reportDir: 'kp', 
                                  reportFiles: 'report.html', reportName: 'HTML Report', reportTitles: 'new'])
                  slackSend color: '#BADA55', message: 'Hello, World!', channel: 'memes'
            }
      }
    
   }
            
  }
}

