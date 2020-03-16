import mongoose from 'mongoose';
import { Connection } from 'mongoose';

import { Conference , ConferenceDocument , ConferenceSchema } from '../schemas/conferences';
import { Database } from '../interfaces/database';
import { ConferenceModel } from '../interfaces/models/conference';
import { Logger } from '../utility/log';


export class ConferenceModelI extends ConferenceModel{
    modelName = "conference"
    private model?:mongoose.Model<ConferenceDocument,{}>;
    private connection?:Connection;
    private logger = new Logger(this.constructor.name).getLogger();
    constructor(database:Database){
        super(database)
        database.getConnection()
        .then( (connection:Connection) => {
            this.connection = connection
            this.model = this.connection.model<ConferenceDocument>( this.modelName, ConferenceSchema);
        } )
        .catch((error) => {
            let errstring = "Failed at getting connection :"+error;
            this.logger.error(errstring)
        })
    }
    
    async getOne():Promise<ConferenceDocument | null> {
        let result = new Promise<ConferenceDocument | null>( (resolve , reject) => {
            if(this.model == undefined){
                this.logger.debug("Failed at getOne: this.model == undefined")
                this.logger.error("Failed at getOne : model must have failed to initialize")
                reject(new Error("model failed to be initialised"));
            }else{
                this.model.findOne({} , (err , res) => {
                    if(!err){
                        resolve(res);
                    }
                    else{
                        reject(err);
                    }
                })
            }
        })
        return result
    }

    /*
        TO-DO
    */
    async getConferences(offset:number , range:number):Promise<ConferenceDocument[] | null> {
        return Promise.resolve(null);
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



