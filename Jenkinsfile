pipeline {
    agent any
     environment {
        PATH = "C:/WINDOWS/SYSTEM32;C:/Users/Armand/AppData/Local/Programs/Python/Python38;C:/Program Files/Docker/Docker/resources/bin"
    }
    stages {
        stage('Testing') {
            steps {
                echo "Test en cours..."
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install Flask'
                bat 'python -m pip install requests'
                bat 'python -m pip install numpy'
                bat 'python -m pip install tensorflow'
                bat 'python test_main.py'
            }
        }
        stage('Deploy') {
            steps {
                bat 'docker build -t restful-flask-app .'
                bat 'docker run -d restful-flask-app'
            }
        }
    }
}
