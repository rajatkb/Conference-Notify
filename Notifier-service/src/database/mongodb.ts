import { injectable, inject } from 'inversify'
import mongoose from 'mongoose';
import { Database } from '../interfaces/database';


@injectable()
export class MongoDb extends Database  {
   protected dbName:string;
   constructor(){
      super()
      let databaseName = process.env.MONGO_DB_NAME
      if(databaseName == undefined)
         throw new Error("No database name provided in environment")
      this.dbName = databaseName
   }
   public getConnection():Promise<mongoose.Connection>{
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
   };
}
