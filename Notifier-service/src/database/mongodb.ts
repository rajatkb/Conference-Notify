import mongoose from 'mongoose';
import { Database } from '../interfaces/database';

export class MongoDb implements  Database{
    dbName:string | undefined = undefined;
    init(dbName:string | undefined):Promise<mongoose.Connection>{
        this.dbName = dbName;
        if(dbName == undefined)
            throw new Error("No db name passed")
        return mongoose.createConnection(`mongodb://${process.env.MONGO_DB_HOST}:${process.env.MONGO_DB_PORT}/${this.dbName}` ,
                         {  useNewUrlParser: true ,
                            useUnifiedTopology: true
                         } )
                         .then((res) => {
                            return Promise.resolve(res)
                         })
                         .catch((err) => {
                            return Promise.reject(err)
                         })
    }
}