import * as dotenv from 'dotenv-safe';
import { App } from './app';
/* 
Load the .env file into the process environment variable scope
It's necessary to keep a .env file in the project root
along side package.json
*/
dotenv.config({
    example: './.env'
});


/*
    Instantiate the App with
    * Controllers
    * Database instance for sharing connection
    * 
*/


// Ensure required SERVER_PORT PORT have datatype of number
if(isNaN(Number(process.env.SERVER_PORT))) {
    throw new Error('The SERVER_PORT must be a number!')
} else {
        let app = new App();
        app.init()
        app.start((port) => {
        console.log("Listening on port :"+port);
    })
}

