pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/angelhumera/SmartAtm.git'/SmartAtm.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t smartatm:h1 .'
            }
        }
        stage('Push to DockerHub') {
            steps {
                withCredentials([string(credentialsId: 'Humerajenkins', variable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u humeradoc --password-stdin'
                    sh 'docker tag smartatm:v1 humeradoc/smartatm:h1'
                    sh 'docker push humeradoc/smartatm:h1'
                }
            }
        }
        stage('Deploy Container') {
            steps {
                sh 'docker run -d -p 5000:5000 humeradoc/smartatm:v1'
            }
        }
    }
}

 post {
        success {
            echo '✅ Pipeline completed successfully. SmartATM is deployed!'
        }
        failure {
            echo '❌ Pipeline failed. Check console output for errors.'
        }
    }
}
