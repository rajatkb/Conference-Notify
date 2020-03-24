import { Database } from './database';
import { injectable } from 'inversify';

@injectable()
export abstract class Model{
    protected database:Database;
    constructor(database:Database){
        this.database = database;
    }
}