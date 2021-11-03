CODE_CHANGES = getGitChanges()
pipeline {

  agent any

  stages {

    stage("Clone") {
      when {
        expression {
            BRANCH_NAME == 'master' && CODE_CHANGES == true
        }
      }
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
      when {
           expression {
                BRANCH_NAME == 'master'
           }
      }
      steps {
        echo 'Deploying...'
        sh '. venv/bin/activate && python3 app.py'
      }
    }
  }
}