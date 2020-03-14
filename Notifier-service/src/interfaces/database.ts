export abstract class Database {
    protected dbName:string;
    constructor(dbName:string){
        this.dbName = dbName;
    };
    public abstract getConnection():Promise<any>;
}