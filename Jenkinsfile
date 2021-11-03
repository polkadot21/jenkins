pipeline {
environment {
registry = "jenkins"
registryCredential = "evsa"
dockerImage = "jenkins"
}
agent any

  stages {

    stage("Clone") {
      steps {
        git branch: "master", url: 'https://github.com/polkadot21/jenkins'
      }
    }

    stage('build an image') {
      steps {
        echo 'Building...'
        script {
            dockerImage = docker.build registry + "5000"
        }
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