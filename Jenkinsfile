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
                bat "docker build -t ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                bat "docker-compose down || true"
                bat "docker-compose up -d --build"
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
