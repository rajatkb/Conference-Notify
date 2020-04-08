import { injectable } from "inversify";

@injectable()
export abstract class Database {
    protected abstract dbName:string;
    public abstract async getConnection():Promise<any>;
    public abstract async close():Promise<void>;
}