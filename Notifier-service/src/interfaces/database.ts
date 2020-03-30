import { injectable } from "inversify";

@injectable()
export abstract class Database {
    protected abstract dbName:string;
    public abstract getConnection():Promise<any>;
    public abstract close():void;
}