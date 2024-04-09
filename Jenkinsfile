pipeline {
    agent any

    environment {
        VENV_PATH = 'myprojectenv'
        FLASK_APP = 'myproject.py'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from a source control management system (e.g., Git)
                git url: 'https://github.com/Geek-shikha/Flask_model_sentiment_analysis.git', branch: 'master'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    // Check for the virtual environment, create it if it doesn't exist
                    sh 'bash -c "python3 -m venv $VENV_PATH"'
                    // Activate the virtual environment
                    sh 'bash -c "source $VENV_PATH/bin/activate"'
                }
            }
        }

        stage('Test') {
            steps {
                 steps {
                // Install any dependencies listed in requirements.txt
                sh 'bash -c "source $VENV_PATH/bin/activate && pip install -r requirements.txt"'
              }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy your Flask app
                    // This step greatly depends on where and how you're deploying your app
                    // For example, if you're deploying to a server you control, you might use scp, rsync, or SSH commands
                    // If you're using a PaaS (Platform as a Service), you might use a specific CLI tool for that platform
                    echo 'Deploying application...'
                    // Example: sh 'scp -r . user@your_server:/path/to/deploy'
                }
            }
        }
    }

    post {
        always {
            // Clean up after the pipeline runs
            echo 'Cleaning up...'
            sh 'rm -rf ${VIRTUAL_ENV_DIR}'
        }
    }
}
