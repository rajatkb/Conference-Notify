import express from 'express';
import { Application , Request , Response } from 'express';
import { Server } from 'http';
import { Logger } from './utility/log';
import { Route } from './interfaces/route';
import { Container } from 'inversify'
import { ConferenceStream } from './interfaces/services/conferenceStream';


export class App {

    private logger = new Logger(this.constructor.name).getLogger();
    private app:Application;
    private server:Server|undefined;
    
    private routes:Route[] =[];

    constructor(private container:Container){
        this.app = express();
        this.routes = container.getAll<Route>(Route)

        

    }

    init():void{
        this.routes.forEach( (route:Route) => {
            this.app.use("/"+route.getRouteName() , route.getRouter())
        })

        // let stream = this.container.get<ConferenceStream>(ConferenceStream)


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

