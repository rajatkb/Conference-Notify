export abstract class Database {
    abstract init(dbName:string | undefined):Promise<any>;
}