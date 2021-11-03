pipeline {
environment {
registry = "jenkins"
registryCredential = "evsa"
dockerImage = "jenkins"
}
agent {
 dockerfile true
}

  stages {

    stage("Clone") {
      steps {
        git branch: "master", url: 'https://github.com/polkadot21/jenkins'
      }
    }

    stage('build an image') {
      steps {
        echo 'Building...'
        sh 'docker build -t model .'
      }
    }

    stage('test') {
      steps {
        echo 'Testing...'
        sh 'docker run --rm model'
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