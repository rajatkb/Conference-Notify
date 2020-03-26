import express from 'express';
import { Application , Request , Response } from 'express';
import { Server } from 'http';
import { Logger } from './utility/log';
import { Route } from './interfaces/route';
import { Listener } from './interfaces/listener';
import { AppContainer } from './inversify.config';



export class App {

    private logger = new Logger(this.constructor.name).getLogger();
    private app:Application;
    private server:Server|undefined;
    
    // Routes for registering toe express application
    private routes:Route[] =[];
    // listeners to instantiate for listening
    private listeners:Listener[] = [];


    constructor(private container:AppContainer){
        this.app = express();
        this.routes = container.getRoutes()
        // this.listeners = container.getAll<Listener>(Listener)
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

