import "reflect-metadata"
import * as dotenv from 'dotenv-safe';
import { App } from './app';
import { AppContainer } from './inversify.config'

/* 
Load the .env file into the process environment variable scope
It's necessary to keep a .env file in the project root
along side package.json
*/
dotenv.config({
    example: './.env'
});

/*
    * Creating Application Container for all class
    * Passing the container to App ,  for route attachment
*/

let container = new AppContainer()
let app = new App(container);
app.init()
app.start((port) => {
    console.log("Listening on port :" + port);
})

