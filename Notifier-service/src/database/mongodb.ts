import mongoose from 'mongoose';
import { Database } from '../interfaces/database';

export class MongoDb extends Database  {
   constructor(dbName:string){
      super(dbName)
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
