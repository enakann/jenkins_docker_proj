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
			post {
                always {
					 sh 'ln -s ./testreports/results.xml $WORKSPACE'
                    junit 'results.xml'
					
                }
		}
	}
}
}