import * as dotenv from 'dotenv-safe';
import { App } from './app';
import { container } from './inversify.config'

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


let app = new App(container);
app.init()
app.start((port) => {
console.log("Listening on port :"+port);
})

