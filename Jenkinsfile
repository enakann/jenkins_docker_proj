pipeline {
    environment {
    registry = "kannan1985/jenkins_docker_proj"
    registryCredential = 'docker'
	}
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
			
		//	post {
        //       always {
        //           junit 'results.xml'		
        //       }
		//}
		
		
	stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy Image') {
      steps{
         script {
            docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
			#docker pull kannan1985/jenkins_docker_proj:37
          }
        }
      }
    }
    stage('Remove Unused docker image') {
      steps{
        sh "docker rmi $registry:$BUILD_NUMBER"
      }
    }
		
	    
	}
}