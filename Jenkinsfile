pipeline {
	agent any
	stages {
		stage('tests') {
			steps {
				echo "Running tests in a fully containerized environment..."
				dir('.') {
					sh './run_tests.sh'
					sh 'touch test-reports/results.xml'
				}
			}
			post {
                always {
                    junit 'test-reports/results.xml'
					
                }
		}
	}
}
}