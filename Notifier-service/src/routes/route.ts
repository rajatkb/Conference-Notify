import {Controller} from '../controllers/controller';
import {Router} from 'express';
export abstract class Route {
    constructor(router:Router , controller:Controller) {}
}