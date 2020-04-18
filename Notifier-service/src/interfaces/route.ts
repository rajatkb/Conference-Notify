import {Controller} from './controller';
import {Router} from 'express';
import { Response, Request } from 'express'
import { injectable } from 'inversify';

@injectable()
export abstract class Route {
    protected abstract routeName:string;
    protected router:Router;
    constructor(controller:Controller){
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