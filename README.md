# Weather-API

## 1. Screenshot

![API Screenshot](https://github.com/lakshitaaS/Weather-API/blob/main/Code%20Screenshot_WeatherAPI.jpeg)

## 2.Architecture Diagram

<!-- Architecture Diagram -->
![Architecture Diagram](https://github.com/lakshitaaS/Weather-API/blob/main/ArchitectureDiagram_WeatherAPI.jpeg)

<!-- Code using Github Pilot -->
![GithubCopilot](https://github.com/lakshitaaS/Weather-API/blob/main/GithubCopilot_WeatherAPI.jpeg)

## 3. Description
In a wider context, the python script will use the OpenWeatherMap API to fetch the weather forecast for a given city, and then display the retrieved information on the command line.

Initially github copilot is installed on visual studio code for code suggestions, completing function signatures, and generating code snippets based on patterns it has learned from existing codebases which makes the coding work easy and user friendly. The GitHub copilot use cases that were implemented are as follow:

1. Code Generation 
 -  In order to parse the response received from the Weather API into json object, we wrote a single comment to do the same. Copilot understood and converted the comment line into the code.

2. Explaining code
 -  To make code readable by the readers, copilot’s auto comment generation was used. By typing a comment prefix(#) the copilot auto generated the comment.
 -  The Open weather API has been used as an external API contact by fetching the x-api-key from the open source API available.

By passing the api key in the url, the response was fetched and further converted to a json object after validating the response code. Out of the response received from the API, which were the details about the weather of the given city entered received in within intervals of 3 hours, parsing was done on the response which was further printed for the required fields.
