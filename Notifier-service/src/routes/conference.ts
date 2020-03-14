import { Router , Request , Response } from 'express';
import { ConferenceController } from '../controllers/conference';
import { Conference } from '../schemas/conferences';
import { Route } from '../interfaces/route';


/**
 * Conference Route attaches the Conference controller
 * and handlers to the routes defined
 * @export
 * @class ConferenceRoute
 * @extends {Route}
 */
export class ConferenceRoute extends Route{


    constructor(private controller: ConferenceController){
        super("conferences" , controller)
        this.setRoutes()
    }

    protected setRoutes(){
        this.router.get("/getone",this.controller.getOne)
        this.router.get("/:offset/:count" , this.controller.getConferences)
        this.router.get("/:category/:offset/:count" , this.controller.getConferences)
        this.router.get("/categories" , this.controller.getCategories)
    }
    
} 