import * as dotenv from 'dotenv';
import { MongoDb } from './database/mongodb'; 
import { App } from './app';
import { ConferenceController } from './controllers/conference'
import { ConferenceRoute} from './routes/conference';
import { ConferenceModel } from './models/conference';
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


let app = new App(  [
                        new ConferenceRoute()
                    ] , 
                    [   
                        new ConferenceController()
                    ] , 
                    [   
                        new ConferenceModel()
                    ] ,  
                    new MongoDb() );

app.init()
app.start((port) => {
    console.log("Listening on port :"+port);
})

