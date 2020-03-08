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
    protected routeName :string = "conferences";
    protected router:Router = Router();
    private controller:ConferenceController | undefined = undefined;

    init(controller:ConferenceController) {
        this.controller = controller;

        this.router.get("/" , async (request:Request , response:Response) => {
            response.redirect("/")
        })

        // added for testing routes purposes
        this.router.get("/one", async (request:Request , response:Response) => {
            try{
                let result = await controller.getOne()
                response.json(result);
            }catch(e){
                console.log()
                throw e
            }
        })

        this.router.get("/:offset/:count",async  (request:Request , response:Response) => {
            let offset:string = request.params.offset;
            let count:string = request.params.count;
            try{
                let result:Conference[] =  await controller.getConferences( Number.parseFloat(offset) , Number.parseFloat(count));
                response.json(result);
            }catch(e){
                //TO-DO
                // report error in log
                // Call alternative route
            }
        });
    
        this.router.get("/:category/:offset/:count", async (request:Request , response:Response) => {
            let offset:string = request.params.offset;
            let count:string = request.params.count;
            let category:string = request.params.category;
            try{
                let result:Conference[] = await controller.getConferencesFromCategory( category , Number.parseFloat(offset) , Number.parseFloat(count));
                response.json(result);
            }catch(e){
                //TO-DO
                // report error in log
                // Call alternative route
            }
        });

        this.router.get("/categories", async  (request:Request , response:Response) => {
            let category:string = request.params.category;
            try{
                let result:Array<String> = await controller.getCategories();
                response.json(result);
            }catch(e){
                //TO-DO
                // report error in log
                // Call alternative default
            }
        });
        
    }

    getRouter():Router {
        return this.router;
    }

    getRouteName():string{
        return this.routeName;
    }
} 