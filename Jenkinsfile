pipeline {
agent any
  stages {
    stage('build') {
      steps {
        sh "venv/bin/activate && pip install -r requirements.txt"
      }
    }
    stage('test') {
      steps {
        sh 'python test.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }
}