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
      steps {
        // run tests with coverage
        sh 'bundle exec rake spec'
      }

      post {
        failure {
          // publish html
          publishHTML target: [
              allowMissing: false,
              alwaysLinkToLastBuild: false,
              keepAll: true,
              reportDir: 'kp',
              reportFiles: 'report.html'
            ]
        }
      }
    }
  }
  }
}
