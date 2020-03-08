import { Connection } from 'mongoose';
export abstract class Model{
    abstract init(connection:Connection):void;
}