import { injectable, inject } from 'inversify'
import mongoose from 'mongoose';
import { Database } from '../interfaces/database';
import { Logger } from '../utility/log';


@injectable()
export class MongoDb extends Database  {
   private logger = new Logger(this.constructor.name).getLogger();
   protected dbName:string;
   public databaseConnection:Promise<mongoose.Connection>;
   constructor(){
      super()
      let databaseName = process.env.MONGO_DB_NAME
      if(databaseName == undefined)
         throw new Error("No database name provided in environment")
      this.dbName = databaseName
      this.databaseConnection = mongoose.createConnection(`mongodb://${process.env.MONGO_DB_HOST}:${process.env.MONGO_DB_PORT}/${this.dbName}` ,
      {  useNewUrlParser: true ,
         useUnifiedTopology: true
      } )
      .then((res) => {
         return Promise.resolve(res)
      })
      .catch((err) => {
         return Promise.reject(err)
      });
   }
   public async getConnection():Promise<mongoose.Connection>{
      return await this.databaseConnection;
   };
   public async close():Promise<void>{
      await this.databaseConnection.then(database => {
         this.logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>> Connection closed!! <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
         database.close()
      })
   }
}
