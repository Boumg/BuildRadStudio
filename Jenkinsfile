pipeline {
    agent {
        node {
            label 'python'
        }
    }
    stages {
        stage('Test') { 
            steps {
                bat 'echo %WORKSPACE%'
                bat 'echo Y | pip uninstall rxbuilder'
                bat 'pip install -r requirements.txt'
                bat 'python setup.py install'
                 dir ('test_rxbuilder') {
                    bat 'nose2 --plugin nose2.plugins.junitxml --junit-xml'
                 }
            }
        }
    }
}