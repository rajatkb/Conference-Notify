import express from 'express';
import { Application , Request , Response } from 'express';
import { Server } from 'http';
import { Logger } from './utility/log';






import { MongoDb } from './database/mongodb'
import { ConferenceController} from './controllers/conference'
import { ConferenceServiceI } from './services/conference'
import { ConferenceModelI } from './models/conference'
import { ConferenceRoute } from './routes/conference'
import { Route } from './interfaces/route';

export class App {

    private logger = new Logger(this.constructor.name).getLogger();


    private app:Application;
    private server:Server|undefined;
    
    private routes:Route[] =[];

    constructor(){
        this.app = express();


        let databaseName = process.env.MONGO_DB_NAME
        if(databaseName == undefined){
            this.logger.error("missing database name in .env");
            throw new Error("No databas name provided")
        }
        
        let database = new MongoDb(databaseName)

        let conferenceService = new ConferenceServiceI(new ConferenceModelI(database))
        let conferenceController = new ConferenceController(conferenceService)
        let conferenceRoute = new ConferenceRoute(conferenceController)
        this.routes.push(conferenceRoute)

    }

    init():void{
        this.routes.forEach( (route:Route) => {
            this.app.use("/"+route.getRouteName() , route.getRouter())
        })

        /*
            Default path for anything
        */
        this.app.get("/**" , (request , response) => {
            response.json({
                status:404,
                payload:" (ノಠ益ಠ)ノ彡┻━┻ "
            })
        })
    }




    start(callback:(port:Number) => void){
        if(process.env.SERVER_PORT == undefined)
            throw new Error("No proper port for server found , configure in .env file")
        let port = Number.parseInt(process.env.SERVER_PORT)
        this.server = this.app.listen( port , () => {
            this.logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>> APPLICATION STARTED <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
            this.logger.info("Application listening at port :"+ port);
            callback(port);
        })
    }
}

