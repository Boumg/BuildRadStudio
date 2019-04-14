pipeline {
    agent {
        node {
            label 'python'
        }
    }
    stages {
        stage('Install') {
            steps {
                bat 'echo Y | pip uninstall rxbuilder'
                bat 'pip install -r requirements.txt'
                bat 'python setup.py install'

            }
        }
        stage('Test') { 
            steps {
                 dir ('test_rxbuilder') {
                    bat 'nose2 --plugin nose2.plugins.junitxml --junit-xml'
                    junit 'nose2-junit.xml'
                 }
            }
        }
    }
}
