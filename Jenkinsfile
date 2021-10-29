pipeline {
agent any
  stages {
    stage('build') {
      steps {
        sh ". venv/bin/activate && pip install -r requirements.txt"
      }
    }
    stage('test') {
      steps {
        sh 'venv/bin/python3 test.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }
}