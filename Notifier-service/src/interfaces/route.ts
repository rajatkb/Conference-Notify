import {Controller} from './controller';
import {Router} from 'express';
import { Response, Request } from 'express'
export abstract class Route {
    protected routeName:string;
    protected router:Router;
    constructor(routeName:string , controller:Controller){
        this.routeName = routeName;
        this.router = Router();
        this.router.get("/" , this.default)
    }
    
    getRouter():Router {
        return this.router;
    }

    getRouteName():string{
        return this.routeName;
    }

    default = async (request: Request, response: Response) => {
        response.redirect("/");
    }

}