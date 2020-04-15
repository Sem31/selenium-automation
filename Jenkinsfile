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
                     sh "pwd"
                     publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: true, reportDir: 'kp', 
                                  reportFiles: 'report.html', reportName: 'HTML Report', reportTitles: 'new'])
                   }
                 // post {
                   //always{
                     
                    //}
                 //}
                 }     
  }
  stages{
  
    stage ('Test 12') {
                   agent any
                   steps{
                     sh "pwd"
                     publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: true, reportDir: 'kp', 
                                  reportFiles: 'report.html', reportName: 'HTML Report', reportTitles: 'new'])
                   }
  }
}
