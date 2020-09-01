# Government Identity Verification Engine

## Address Verification Service

### Pre-requisites
- [Maven](https://maven.apache.org/) 
- [OpenJDK 8](https://developers.redhat.com/products/openjdk/download)
- [Postman](https://www.postman.com/downloads/)

### Getting started
Run `mvnw spring-boot:run` to build and run the application

This poject was created with [Spring Boot Initializr](https://start.spring.io/)

### Available Scripts

`mvnw clean install`

Builds the .jar files (including aws .jar file for lambda usage)

`mvnw spring-boot:run`

Runs the application.


After successfully running, open Postman and make a post request to `localhost:8080`

Use this sample as the body:
```
{   
   "UUID": "AA97B177-9383-4934-8543-0F91A7A02836",
   "firstName": "Susan", 
   "lastName":"Smith", 
   "streetAddress":"215 Spring Street", 
   "city":"Anytown", 
   "state":"WV", 
   "zipCode":"24986", 
   "emailAddress":"susan.smith@gmail.com" 
   "IPPVersion":"1.5" 
} 
```


### Build/Deployment

The building and deploying of the project is automated using AWS Codebuild and Bitbucket Webhooks.
The resulting API is hosted on AWS API Gateway and can be invoked through a Post request to
https://6ur31p4b3k.execute-api.us-east-1.amazonaws.com/beta/usps-av.


### API Documentation

Endpoints can be viewed using the [Swagger interface](http://localhost:8080/swagger-ui.html)


### Learn More

To learn more about Spring boot, visit [Spring Boot Quickstart](https://spring.io/quickstart)