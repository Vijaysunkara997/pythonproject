pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
              bat '"C:\\Users\\DELL\\AppData\\Local\\Python\\bin\\python.exe" --version'

bat '"C:\\Users\\DELL\\AppData\\Local\\Python\\bin\\python.exe" -m pip install --upgrade pip'

bat '"C:\\Users\\DELL\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt'

bat '"C:\\Users\\DELL\\AppData\\Local\\Python\\bin\\python.exe" -m playwright install chromium'

bat '"C:\\Users\\DELL\\AppData\\Local\\Python\\bin\\python.exe" -m pytest -v -s'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\DELL\\AppData\\Local\\Python\\bin\\python.exe" -m pytest -v -s'
            }
        }
    }
}
