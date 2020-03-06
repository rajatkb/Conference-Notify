import { Router , Request , Response } from 'express';
import { ConferenceController } from '../controllers/conference';
import { Conference } from '../schemas/conferences';
import { Route } from './route';

export class ConferenceRoute extends Route{
    private routeName :string = "conferences";

    /**
     *Creates an instance of ConferenceRoute.
     *Registers all the routes for Conference route
     *
     * @param {Router} router
     * @memberof ConferenceRoute
     */
    constructor(private router:Router , private controller:ConferenceController) {
        super(router , controller);
        router.get("/:offset/:count", (request:Request , response:Response) => {
            let offset:string = request.params.offset;
            let count:string = request.params.count;
            try{
                let result:Conference[] =  controller.getConferences( Number.parseFloat(offset) , Number.parseFloat(count));
                response.json(result);
            }catch(e){
                //TO-DO
                // Call alternative route
            }
        });
    
        router.get("/:category/:offset/:count", (request:Request , response:Response) => {
            let offset:string = request.params.offset;
            let count:string = request.params.count;
            let category:string = request.params.category;
            try{
                let result:Conference[] =  controller.getConferences( category , Number.parseFloat(offset) , Number.parseFloat(count));
                response.json(result);
            }catch(e){
                //TO-DO
                // Call alternative route
            }
        });

        router.get("/categories", (request:Request , response:Response) => {
            let category:string = request.params.category;
            let result:Array<String> = controller.getCategories();
            response.json(result);
        });
        
    }

} 