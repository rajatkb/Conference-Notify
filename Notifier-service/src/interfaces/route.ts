import {Controller} from './controller';
import {Router} from 'express';
export abstract class Route {
    protected routeName ?:string;
    protected router?:Router
    init(controller:Controller):void{}
    abstract getRouter():Router;
    abstract getRouteName():string;

}