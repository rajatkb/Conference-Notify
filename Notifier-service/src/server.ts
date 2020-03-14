import * as dotenv from 'dotenv';
import { App } from './app';
/* 
Load the .env file into the process environment variable scope
It's necessary to keep a .env file in the project root
along side package.json
*/
dotenv.config()


/*
    Instantiate the App with
    * Controllers
    * Database instance for sharing connection
    * 
*/


let app = new App();
app.init()
app.start((port) => {
    console.log("Listening on port :"+port);
})

