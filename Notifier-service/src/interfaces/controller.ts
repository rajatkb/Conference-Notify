import { Model }  from './model'

export abstract class Controller {
    abstract init(model:Model):void;
}