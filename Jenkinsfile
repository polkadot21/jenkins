pipeline {
agent any

  stages {

    stage('build') {
      steps {
        echo 'Building...'
        sh ". venv/bin/activate && pip install -r requirements.txt"
      }
    }

    stage('test') {
      steps {
        echo 'Testing...'
        sh '. venv/bin/activate && python3 test.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }

    stage('deploy') {
      steps {
        echo 'Deploying...'
        sh '. venv/bin/activate && python3 app.py'
      }
    }
  }
  }
}