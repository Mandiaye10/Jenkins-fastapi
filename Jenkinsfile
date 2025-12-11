pipeline {
    agent any
    /* agent {
        label 'agent-windows'  // ou 'linux' selon votre agent Jenkins
    }
    */


    environment {
        DOCKERHUB_USER = "encvr1"
        IMAGE_NAME     = "backend-fastapi-gtp"
        IMAGE_TAG      = "1.${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

    

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh "docker-compose down || true"
                sh "docker-compose up -d --build"
            }
        }
    }

    post {
        success {
            echo " Déploiement Backend FastAPI réussi !"
        }
        failure {
            echo " Le pipeline a échoué, vérifiez les logs Jenkins."
        }
    }
}
