pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/<your-username>/smartatm.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t smartatm:v1 .'
            }
        }
        stage('Push to DockerHub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u <your-dockerhub-username> --password-stdin'
                    sh 'docker tag smartatm:v1 <your-dockerhub-username>/smartatm:v1'
                    sh 'docker push <your-dockerhub-username>/smartatm:v1'
                }
            }
        }
        stage('Deploy Container') {
            steps {
                sh 'docker run -d -p 5000:5000 <your-dockerhub-username>/smartatm:v1'
            }
        }
    }
}
