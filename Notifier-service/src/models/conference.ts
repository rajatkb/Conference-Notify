import mongoose from 'mongoose';
import { Connection } from 'mongoose';
import { Conference , ConferenceDocument , ConferenceSchema } from '../schemas/conferences';
import { Database } from '../interfaces/database';
import { ConferenceModel } from '../interfaces/models/conference';
import { Logger } from '../utility/log';



export class ConferenceModelI extends ConferenceModel{
    modelName = "conference"
    private model:Promise<mongoose.Model<ConferenceDocument,{}>>;
    private connection:Promise<Connection>;
    private logger = new Logger(this.constructor.name).getLogger();
    constructor(database:Database){
        super(database)
        
        // this.connection = connection
        // this.model = this.connection.model<ConferenceDocument>( this.modelName, ConferenceSchema);

        this.connection = database.getConnection()
        .then( (connection:Connection) => {
            return Promise.resolve(connection);
        } )
        .catch((error) => {
            let errstring = "Failed at getting connection :"+error;
            this.logger.error(errstring);
            return Promise.reject(error);
        })

        this.model = this.connection
        .then( (connection: Connection) =>{
            let model = connection.model<ConferenceDocument>( this.modelName, ConferenceSchema);
            return Promise.resolve(model);
        } )
        .catch((error) => {
            let errstring = "Failed at getting connection for model"+error;
            this.logger.error(errstring);
            return Promise.reject(error);
        })

    }
    
    private async  makeQuery<T>(callback:(model:mongoose.Model<ConferenceDocument,{}>) => Promise<T>):Promise<T> {
        return this.model
        .then(callback)
        .catch(error => {
            this.logger.debug("Failed at getOne: model not initialised error:"+error);
            this.logger.error("Failed at getOne : model must have failed to initialize :"+error);
            return Promise.reject(new Error("model failed to be initialised"));
        });                
    }


    async getOne():Promise<ConferenceDocument | null> {
        let result = this.makeQuery((model) => {
            return new Promise<ConferenceDocument | null>( (resolve , reject) => {
                model.findOne({} , (err , res) => {
                    if(!err){
                        resolve(res);
                    }
                    else{
                        reject(err);
                    }
                })
            })
        })
        return result
    }

    /*
        TO-DO
    */
    async getConferences(offset:number , range:number):Promise<ConferenceDocument[] | null> {
        let result = this.makeQuery((model) => {
            return new Promise<ConferenceDocument[] | null>( (resolve , reject) => {
                model.find({}).limit(range).exec((err , res) => {
                    if(!err){
                        resolve(res);
                    }
                    else{
                        reject(err);
                    }
                })
            })
        })

        return result;
    }

    /*
        TO-DO
    */
    async getConferencesFromCategory(category:string , offset:number , range:number):Promise<ConferenceDocument[] | null> {
        return Promise.resolve(null);
    }


    async getCategories():Promise<any> {
        return Promise.resolve(null);
    }

    /*
        TO-DO 
        1. add getConferences query function for the controller
            -> Will get range number of conferences with a given offset
            -> the result will be sorted by deadline

        2. add getConferencesFromCategory query function for the controller
            -> same as above but will have extra parameter of conference category

        3. add getCategories query function for the controller
            -> returns all unique categories acrooss all the entries
    */
}



