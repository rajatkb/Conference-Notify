import express from 'express';
import { Application , Request , Response } from 'express';
import { Route } from './interfaces/route';
import { Database} from './interfaces/database';
import { Server } from 'http';
import { Controller } from './interfaces/controller';
import { Model } from './interfaces/model';
import { Logger } from './utility/log';


export class App {

    private logger = new Logger(this.constructor.name).getLogger();


    private app:Application;
    private server:Server|undefined;
    constructor(private routes:Array<Route>,
                private controllers:Array<Controller>,
                private models:Array<Model>,
                private database:Database){
        this.app = express();
    }

    async init(){
        try{
            let connection = await this.database.init(process.env.MONGO_DB_NAME) 

            this.models.forEach(model => {
                model.init(connection)
            })

            this.controllers.forEach((controller , index) => {
                controller.init(this.models[index])
            })

            this.routes.forEach((route,index) => {
                route.init(this.controllers[index])
                this.app.use('/'+route.getRouteName() ,route.getRouter())
            })

            this.app.get("/*", (req:Request, res:Response) => {
                res.json({"error": "route Not available"})
            })
        }catch(e){
            //TO-DO Logg error for not being able to create the mongo db or any of the routes
            console.log(e);

        }
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

