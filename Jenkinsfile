pipeline {
    agent {
        node {
            label 'python'
        }
    }
    stages {
        stage('Test') { 
            steps {
                sh 'echo %WORKSPACE%'
                sh 'echo Y | pip uninstall rxbuilder'
                sh 'pip install -r requirements.txt'
                sh 'python setup.py install'
                 dir ('test_rxbuilder') {
                    sh 'nose2 --plugin nose2.plugins.junitxml --junit-xml'
                 }
            }
        }
    }
}