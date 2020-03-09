import mongoose from 'mongoose';
import { Conference , ConferenceDocument , ConferenceSchema } from '../schemas/conferences';
import { Model } from '../interfaces/model';
import { Connection } from 'mongoose';

export class ConferenceModel extends Model{
    private modelName:string = "conference";
    private model:mongoose.Model<ConferenceDocument , {}> | undefined= undefined
    private connection:Connection | undefined = undefined;
    
    init( connection:Connection){
        this.connection = connection;
        this.model = this.connection.model<ConferenceDocument>( this.modelName, ConferenceSchema);
    } 
    
    async getOne():Promise<ConferenceDocument | null> {
        let result = new Promise<ConferenceDocument | null>( (resolve , reject) => {
            if(this.model == undefined){
                reject({"error": "init() not called for Conference Model , no connection found"});
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
        1. add getConferences query function for the controller
            -> Will get range number of conferences with a given offset
            -> the result will be sorted by deadline

        2. add getConferencesFromCategory query function for the controller
            -> same as above but will have extra parameter of conference category

        3. add getCategories query function for the controller
            -> returns all unique categories acrooss all the entries
    */
}



