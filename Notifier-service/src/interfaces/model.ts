import { Database } from './database';
export abstract class Model{
    protected database:Database;
    constructor(database:Database){
        this.database = database;
    }
}