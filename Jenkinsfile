pipeline {
	agent any
	stages {
		stage('tests') {
			steps {
				echo "Running tests in a fully containerized environment..."
				dir('.') {
					sh './run_tests.sh'
				}
			}
		}
	}
}
