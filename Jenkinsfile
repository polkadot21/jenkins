pipeline {

  agent any

  stages {

    stage("Clone") {
      steps {
        git branch: "master", url: 'https://github.com/polkadot21/jenkins'
      }
    }

    stage("Train the model") {
      steps {
        sh '. venv/bin/activate && python3 model/model.py'
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
      }

    stage('deploy') {
      steps {
        echo 'Deploying...'
        sh '. venv/bin/activate && python3 app.py'
      }
    }
  }
}