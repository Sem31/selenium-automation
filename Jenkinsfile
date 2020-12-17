#!groovy

pipeline {

  agent {
      label 'docker'
  }
  environment {
    UPLYNK = 'uplynk'
   }
  stages {

    stage('Docker Build and Run Tests') {
        steps {
            sh 'docker build -t sel:latest -f ./cms-ui-automation/Dockerfile.uplynk .'
            sh 'docker volume create data'
            sh 'docker run -v $(pwd)/cms-ui-automation/test_report:/data sel:latest'
        }
        post {
            always {
              // publish html
              publishHTML([allowMissing: false,
                           alwaysLinkToLastBuild: false,
                           keepAll: true,
                           reportDir: './cms-ui-automation/test_report',
                           reportFiles: 'report.html',
                           reportName: 'HTML Report', reportTitles: ''])

                slackSend botUser: false,
                 color: '#BADA55',
                 channel: 'ul-cms-automation',
                 message: "Uplynk ui-automation Testcases (' +${currentBuild.number}+ ') " + "${currentBuild.currentResult}" + "${BUILD_URL}console",
                 token: 'GCGCwiGq9uF1LpS5yz8VBKkD'

                 cleanWs()
            }
        }
    }
  }
}
